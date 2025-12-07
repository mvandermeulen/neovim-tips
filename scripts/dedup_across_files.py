#!/usr/bin/env python3
"""
Find and remove duplicate tips across different files based on titles.
Automatically decides which version to keep based on quality scoring.
"""

import re
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

class Tip:
    def __init__(self, title: str, content: str, file_path: Path, start_line: int):
        self.title = title
        self.content = content
        self.file_path = file_path
        self.start_line = start_line
        self.category = self._extract_category()
        self.tags = self._extract_tags()

    def _extract_category(self) -> str:
        match = re.search(r'# Category:\s*(.+)', self.content)
        return match.group(1).strip() if match else ""

    def _extract_tags(self) -> List[str]:
        match = re.search(r'# Tags:\s*(.+)', self.content)
        if match:
            return [t.strip() for t in match.group(1).split(',')]
        return []

    def has_vimscript(self) -> bool:
        return '```vim' in self.content or '```viml' in self.content

    def has_lua(self) -> bool:
        return '```lua' in self.content

    def get_code_length(self) -> int:
        """Get total length of code blocks"""
        code_blocks = re.findall(r'```(?:vim|lua|viml).*?```', self.content, re.DOTALL)
        return sum(len(block) for block in code_blocks)

    def get_explanation_length(self) -> int:
        """Get length of explanation text (non-code)"""
        no_code = re.sub(r'```.*?```', '', self.content, flags=re.DOTALL)
        return len(no_code.strip())

    def get_score(self) -> int:
        """Comprehensive quality score"""
        score = 0

        # Content length (base score)
        score += len(self.content)

        # Code completeness
        if self.has_vimscript() and self.has_lua():
            score += 1000  # Both languages!
        elif self.has_vimscript() or self.has_lua():
            score += 300  # At least one

        # Code quality (longer code = more detailed)
        score += self.get_code_length() * 2

        # Explanation quality
        score += self.get_explanation_length()

        # Tag count (more tags = better categorized)
        score += len(self.tags) * 50

        # Bonus for detailed explanations (multiple paragraphs)
        paragraphs = [p for p in self.content.split('\n\n') if p.strip() and not p.strip().startswith('```')]
        score += len(paragraphs) * 100

        return score

    def get_decision_reason(self, other: 'Tip') -> str:
        """Explain why this tip is better than the other"""
        reasons = []

        # Code comparison
        if self.has_vimscript() and self.has_lua() and not (other.has_vimscript() and other.has_lua()):
            reasons.append("has both Vim+Lua code")
        elif self.has_lua() and not other.has_lua():
            reasons.append("has Lua code")
        elif self.has_vimscript() and not other.has_vimscript():
            reasons.append("has Vimscript code")

        # Content comparison
        if self.get_code_length() > other.get_code_length() * 1.5:
            reasons.append("more detailed code examples")
        if self.get_explanation_length() > other.get_explanation_length() * 1.5:
            reasons.append("longer explanation")

        # Tags comparison
        if len(self.tags) > len(other.tags):
            reasons.append(f"{len(self.tags)} tags vs {len(other.tags)}")

        # Overall length
        if len(self.content) > len(other.content) * 1.3:
            reasons.append(f"longer overall ({len(self.content)} vs {len(other.content)} chars)")

        return ", ".join(reasons) if reasons else "slightly better overall score"

def parse_tips_from_file(file_path: Path) -> List[Tip]:
    """Parse all tips from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tips = []
    lines = content.split('\n')
    current_tip_lines = []
    current_title = None
    current_start = 0

    for i, line in enumerate(lines, 1):
        if line.startswith('# Title:'):
            # Save previous tip if exists
            if current_title and current_tip_lines:
                tip_content = '\n'.join(current_tip_lines)
                tips.append(Tip(current_title, tip_content, file_path, current_start))

            # Start new tip
            current_title = line.replace('# Title:', '').strip()
            current_tip_lines = [line]
            current_start = i
        elif current_title is not None:
            current_tip_lines.append(line)

    # Don't forget the last tip
    if current_title and current_tip_lines:
        tip_content = '\n'.join(current_tip_lines)
        tips.append(Tip(current_title, tip_content, file_path, current_start))

    return tips

def find_duplicates(data_dir: Path) -> Dict[str, List[Tip]]:
    """Find all tips grouped by title"""
    all_tips = defaultdict(list)

    for md_file in sorted(data_dir.glob('*.md')):
        tips = parse_tips_from_file(md_file)
        for tip in tips:
            all_tips[tip.title].append(tip)

    # Filter to only duplicates
    duplicates = {title: tips for title, tips in all_tips.items() if len(tips) > 1}

    return duplicates

def remove_duplicates(data_dir: Path, dry_run: bool = False):
    """Remove duplicate tips, keeping the best version"""
    duplicates = find_duplicates(data_dir)

    if not duplicates:
        print("✓ No duplicate titles found!")
        return

    print(f"Found {len(duplicates)} duplicate titles across files\n")
    print("Reviewing each duplicate and making decisions...\n")
    print("="*80)

    tips_to_remove = []

    for title, tips in sorted(duplicates.items()):
        print(f"\n📝 '{title}' ({len(tips)} occurrences)")

        # Sort by score (best first)
        tips.sort(key=lambda t: t.get_score(), reverse=True)

        # Keep the first (best), mark others for removal
        keeper = tips[0]
        print(f"   ✓ KEEP: {keeper.file_path.name}:{keeper.start_line}")
        print(f"      Score: {keeper.get_score()}, Vim: {'✓' if keeper.has_vimscript() else '✗'}, Lua: {'✓' if keeper.has_lua() else '✗'}")

        for tip in tips[1:]:
            reason = keeper.get_decision_reason(tip)
            print(f"   ✗ REMOVE: {tip.file_path.name}:{tip.start_line}")
            print(f"      Score: {tip.get_score()}, Vim: {'✓' if tip.has_vimscript() else '✗'}, Lua: {'✓' if tip.has_lua() else '✗'}")
            print(f"      Reason: {reason}")
            tips_to_remove.append(tip)

    print(f"\n{'='*80}")
    print(f"SUMMARY: Keeping {len(duplicates)} best versions, removing {len(tips_to_remove)} duplicates")
    print(f"{'='*80}\n")

    if dry_run:
        print("🔍 DRY RUN - No files modified")
        return

    # Group removals by file
    removals_by_file = defaultdict(list)
    for tip in tips_to_remove:
        removals_by_file[tip.file_path].append(tip)

    # Process each file
    for file_path, tips in removals_by_file.items():
        # Sort by start line descending (remove from bottom up to preserve line numbers)
        tips.sort(key=lambda t: t.start_line, reverse=True)

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for tip in tips:
            # Find the tip boundaries
            start_idx = tip.start_line - 1
            end_idx = start_idx

            # Find end of this tip (next "# Title:" or end of file)
            for i in range(start_idx + 1, len(lines)):
                if lines[i].startswith('# Title:'):
                    end_idx = i
                    break
            else:
                end_idx = len(lines)

            # Remove the tip
            del lines[start_idx:end_idx]

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print(f"✓ Updated {file_path.name} (removed {len(tips)} duplicate(s))")

    print(f"\n✅ Successfully removed {len(tips_to_remove)} duplicate tips across {len(removals_by_file)} files")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Remove duplicate tips across files')
    parser.add_argument('--data-dir', type=Path, default=Path('data'),
                        help='Directory containing tip files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be removed without actually removing')

    args = parser.parse_args()

    remove_duplicates(args.data_dir, dry_run=args.dry_run)
