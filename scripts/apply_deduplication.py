#!/usr/bin/env python3
"""
Apply deduplication results to create cleaned tip files.

Supports two modes:
- conservative: Only remove clear duplicates, keep similar tips
- merge: Auto-merge similar tips using AI
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Set
from dataclasses import dataclass
from anthropic import Anthropic
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv('.env.scripts')


@dataclass
class Tip:
    """Represents a single tip"""
    id: str
    title: str
    category: str
    tags: List[str]
    explanation: str
    vimscript: str
    lua: str
    source: str
    line_number: int


class TipParser:
    """Parse tips from merged files"""

    @staticmethod
    def parse_file(file_path: Path) -> List[Tip]:
        """Parse tips from a file"""
        content = file_path.read_text()
        tips = []

        # Split by separator
        sections = content.split('***')
        line_offset = 1

        for idx, section in enumerate(sections):
            section = section.strip()
            if not section:
                continue

            # Extract title
            title_lines = [l for l in section.split('\n') if l.startswith('# Title:')]
            if not title_lines:
                continue

            title = title_lines[0].replace('# Title:', '').strip()

            # Extract other fields
            category_lines = [l for l in section.split('\n') if l.startswith('# Category:')]
            category = category_lines[0].replace('# Category:', '').strip() if category_lines else ''

            tags_lines = [l for l in section.split('\n') if l.startswith('# Tags:')]
            tags = tags_lines[0].replace('# Tags:', '').strip().split(',') if tags_lines else []
            tags = [t.strip() for t in tags]

            # Extract explanation (text between --- and code blocks)
            lines = section.split('\n')
            explanation_lines = []
            in_code = False
            past_separator = False

            for line in lines:
                if line.strip() == '---':
                    past_separator = True
                    continue
                if line.startswith('```'):
                    in_code = not in_code
                    continue
                if line.startswith('**Source:**'):
                    break
                if past_separator and not in_code and not line.startswith('#') and line.strip():
                    explanation_lines.append(line)

            explanation = '\n'.join(explanation_lines).strip()

            # Extract source
            source_lines = [l for l in section.split('\n') if l.startswith('**Source:**')]
            source = source_lines[0].replace('**Source:', '').strip() if source_lines else ''

            # Extract code blocks
            import re
            vim_blocks = re.findall(r'```vim\n(.*?)```', section, re.DOTALL)
            lua_blocks = re.findall(r'```lua\n(.*?)```', section, re.DOTALL)

            vimscript = '\n'.join(vim_blocks).strip() if vim_blocks else ''
            lua = '\n'.join(lua_blocks).strip() if lua_blocks else ''

            tips.append(Tip(
                id=f"tip_{idx}",
                title=title,
                category=category,
                tags=tags,
                explanation=explanation,
                vimscript=vimscript,
                lua=lua,
                source=source,
                line_number=line_offset
            ))

            # Track line offset
            line_offset += section.count('\n') + 1

        return tips


class TipMerger:
    """Merge similar tips using AI"""

    def __init__(self):
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.merge_count = 0

    def merge_tips(self, tip1: Tip, tip2: Tip, reason: str) -> Tip:
        """Merge two similar tips into one comprehensive tip"""

        prompt = f"""Merge these two similar Vim/Neovim tips into ONE comprehensive tip.

IMPORTANT RULES:
1. Preserve ALL unique information from both tips
2. Combine explanations to be more comprehensive
3. Keep BOTH code examples if they show different approaches
4. Merge tags (remove duplicates)
5. Prefer more detailed title
6. Keep both sources (combine with " and ")

TIP 1:
Title: {tip1.title}
Tags: {', '.join(tip1.tags)}
Explanation: {tip1.explanation}
Vimscript: {tip1.vimscript[:200] if tip1.vimscript else 'None'}
Lua: {tip1.lua[:200] if tip1.lua else 'None'}
Source: {tip1.source}

TIP 2:
Title: {tip2.title}
Tags: {', '.join(tip2.tags)}
Explanation: {tip2.explanation}
Vimscript: {tip2.vimscript[:200] if tip2.vimscript else 'None'}
Lua: {tip2.lua[:200] if tip2.lua else 'None'}
Source: {tip2.source}

REASON FOR MERGING: {reason}

Return ONLY valid JSON (no markdown code blocks):
{{
  "title": "merged title",
  "tags": ["tag1", "tag2"],
  "explanation": "comprehensive explanation combining both",
  "vimscript": "combined vimscript code or best version",
  "lua": "combined lua code or best version",
  "source": "combined sources"
}}
"""

        try:
            response = self.client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=2000,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            response_text = response.content[0].text.strip()

            # Remove markdown code blocks if present
            if response_text.startswith('```'):
                import re
                response_text = re.sub(r'^```(?:json)?\n', '', response_text)
                response_text = re.sub(r'\n```$', '', response_text)

            result = json.loads(response_text)

            self.merge_count += 1

            # Create merged tip (preserve tip1's metadata)
            return Tip(
                id=tip1.id,
                title=result['title'],
                category=tip1.category,
                tags=result['tags'] if isinstance(result['tags'], list) else [result['tags']],
                explanation=result['explanation'],
                vimscript=result['vimscript'],
                lua=result['lua'],
                source=result['source'],
                line_number=tip1.line_number
            )

        except Exception as e:
            print(f"Error merging tips: {e}")
            # Fallback: keep first tip
            return tip1


def tip_to_markdown(tip: Tip) -> str:
    """Convert tip to markdown format"""
    tags_str = ', '.join(tip.tags)

    md = f"# Title: {tip.title}\n"
    md += f"# Category: {tip.category}\n"
    md += f"# Tags: {tags_str}\n"
    md += "---\n"
    md += f"{tip.explanation}\n\n"

    if tip.vimscript:
        md += "```vim\n"
        md += f"{tip.vimscript}\n"
        md += "```\n"

    if tip.lua:
        md += "```lua\n"
        md += f"{tip.lua}\n"
        md += "```\n"

    if tip.source:
        md += f"\n**Source:** {tip.source}\n"

    md += "***\n"
    return md


def apply_deduplication(report_path: Path, input_dir: Path, output_dir: Path,
                       mode: str = 'conservative'):
    """
    Apply deduplication results.

    Modes:
    - conservative: Only remove clear duplicates (confidence >= 0.9), keep similar
    - merge: Auto-merge similar tips with confidence >= 0.8
    """

    print(f"\n{'='*80}")
    print(f"Applying Deduplication (mode: {mode})")
    print(f"{'='*80}\n")

    # Load report
    with open(report_path) as f:
        report = json.load(f)

    output_dir.mkdir(exist_ok=True)

    merger = TipMerger() if mode == 'merge' else None
    total_removed = 0
    total_merged = 0

    for file_result in report:
        filename = file_result['file']
        print(f"\nProcessing: {filename}")

        file_path = input_dir / filename
        tips = TipParser.parse_file(file_path)

        # Track which tips to remove
        tips_to_remove: Set[str] = set()

        # Track which tips to merge (tip_id -> (other_tip_id, reason))
        tips_to_merge: Dict[str, tuple] = {}

        # Process duplicates (always remove)
        for dup in file_result.get('duplicates', []):
            if dup['confidence'] >= 0.9:
                # Remove the second tip (keep first)
                tips_to_remove.add(dup['tip2_id'])
                total_removed += 1
                print(f"  Remove duplicate: {dup['tip2_title']}")

        # Process similar tips based on mode
        if mode == 'conservative':
            # Keep all similar tips
            print(f"  Keeping {len(file_result.get('similar', []))} similar tips")

        elif mode == 'merge':
            # Merge similar tips with high confidence
            for sim in file_result.get('similar', []):
                if sim['confidence'] >= 0.8 and sim['recommendation'] == 'merge':
                    tip1_id = sim['tip1_id']
                    tip2_id = sim['tip2_id']

                    # Only merge if neither is already marked for removal or merge
                    if tip1_id not in tips_to_remove and tip2_id not in tips_to_remove:
                        if tip1_id not in tips_to_merge and tip2_id not in tips_to_merge:
                            tips_to_merge[tip1_id] = (tip2_id, sim['reason'])
                            tips_to_remove.add(tip2_id)
                            total_merged += 1
                            print(f"  Merge: {sim['tip1_title']} + {sim['tip2_title']}")

        # Build tip lookup
        tip_lookup = {tip.id: tip for tip in tips}

        # Perform merges if needed
        if mode == 'merge' and tips_to_merge:
            print(f"  Performing {len(tips_to_merge)} AI merges...")
            for tip1_id, (tip2_id, reason) in tips_to_merge.items():
                tip1 = tip_lookup[tip1_id]
                tip2 = tip_lookup[tip2_id]
                merged = merger.merge_tips(tip1, tip2, reason)
                tip_lookup[tip1_id] = merged

        # Filter out removed tips
        kept_tips = [tip for tip in tips if tip.id not in tips_to_remove]

        # Write output
        output_file = output_dir / filename
        content = ''.join(tip_to_markdown(tip_lookup[tip.id]) for tip in kept_tips)
        output_file.write_text(content)

        print(f"  Result: {len(tips)} → {len(kept_tips)} tips")

    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Mode: {mode}")
    print(f"Tips removed (duplicates): {total_removed}")
    if mode == 'merge':
        print(f"Tips merged: {total_merged}")
        print(f"AI merge calls: {merger.merge_count}")
    print(f"Output directory: {output_dir}")
    print(f"{'='*80}\n")


def main():
    parser = argparse.ArgumentParser(description='Apply deduplication results')
    parser.add_argument('--report', type=str, default='scripts/dedup_report.json',
                       help='Deduplication report JSON file')
    parser.add_argument('--input-dir', type=str, default='scripts/merged_tips',
                       help='Input directory with merged tips')
    parser.add_argument('--output-dir', type=str, default='scripts/merged_tips_cleaned',
                       help='Output directory for cleaned tips')
    parser.add_argument('--mode', type=str, choices=['conservative', 'merge'],
                       default='conservative',
                       help='Deduplication mode: conservative (keep similar) or merge (auto-merge similar)')

    args = parser.parse_args()

    apply_deduplication(
        report_path=Path(args.report),
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        mode=args.mode
    )


if __name__ == '__main__':
    main()
