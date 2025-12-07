#!/usr/bin/env python3
"""
Hybrid deduplication using embeddings + AI verification.

Stage 1: Use embeddings to find similar tips (fast, cheap/free)
Stage 2: Use AI only to verify high-similarity pairs (expensive but selective)

This reduces API costs by 90-95% compared to full AI comparison.
"""

import os
import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass
from anthropic import Anthropic
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import time

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

    def get_text_for_embedding(self) -> str:
        """Get combined text for embedding"""
        # Combine title, explanation, and code for better matching
        parts = [
            self.title,
            self.explanation,
            self.vimscript[:200] if self.vimscript else '',
            self.lua[:200] if self.lua else ''
        ]
        return ' '.join(parts)


class TipParser:
    """Parse tips from merged files"""

    @staticmethod
    def parse_file(file_path: Path) -> List[Tip]:
        """Parse tips from a file"""
        content = file_path.read_text()
        tips = []

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

            # Extract explanation
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

            line_offset += section.count('\n') + 1

        return tips


class EmbeddingGenerator:
    """Generate embeddings for tips using sentence-transformers (FREE)"""

    def __init__(self):
        try:
            from sentence_transformers import SentenceTransformer
            print("Loading sentence-transformers model (first time may download ~400MB)...")
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.method = 'local'
            print("✓ Using local embeddings (FREE)")
        except ImportError:
            print("⚠️  sentence-transformers not installed")
            print("Install with: pip install sentence-transformers")
            print("Falling back to simple TF-IDF...")
            self.model = None
            self.method = 'tfidf'

    def generate_embeddings(self, tips: List[Tip]) -> np.ndarray:
        """Generate embeddings for all tips"""
        texts = [tip.get_text_for_embedding() for tip in tips]

        if self.method == 'local':
            # Use sentence-transformers (FREE, runs locally)
            embeddings = self.model.encode(texts, show_progress_bar=True)
            return embeddings

        elif self.method == 'tfidf':
            # Fallback: Simple TF-IDF (FREE, basic)
            from sklearn.feature_extraction.text import TfidfVectorizer
            vectorizer = TfidfVectorizer(max_features=384)
            embeddings = vectorizer.fit_transform(texts).toarray()
            return embeddings


class HybridDeduplicator:
    """Hybrid deduplication: embeddings + AI verification"""

    def __init__(self, similarity_threshold: float = 0.7):
        self.similarity_threshold = similarity_threshold
        self.embedding_gen = EmbeddingGenerator()
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        # Cost tracking
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_calls = 0
        self.pairs_filtered = 0
        self.pairs_verified = 0

    def find_similar_pairs(self, tips: List[Tip]) -> List[Tuple[int, int, float]]:
        """Find similar tip pairs using embeddings"""
        print(f"\n  Generating embeddings for {len(tips)} tips...")
        embeddings = self.embedding_gen.generate_embeddings(tips)

        print(f"  Calculating cosine similarity...")
        similarity_matrix = cosine_similarity(embeddings)

        # Find pairs above threshold
        similar_pairs = []
        for i in range(len(tips)):
            for j in range(i + 1, len(tips)):
                similarity = similarity_matrix[i][j]
                if similarity >= self.similarity_threshold:
                    similar_pairs.append((i, j, similarity))

        # Sort by similarity (highest first)
        similar_pairs.sort(key=lambda x: x[2], reverse=True)

        print(f"  Found {len(similar_pairs)} similar pairs (threshold: {self.similarity_threshold})")
        self.pairs_filtered = len(tips) * (len(tips) - 1) // 2 - len(similar_pairs)

        return similar_pairs

    def verify_with_ai(self, tip1: Tip, tip2: Tip) -> Dict:
        """Verify similarity using AI"""
        prompt = f"""Compare these two tips and determine their relationship:

TIP 1:
Title: {tip1.title}
Explanation: {tip1.explanation[:300]}...

TIP 2:
Title: {tip2.title}
Explanation: {tip2.explanation[:300]}...

Return JSON only:
{{
  "relationship": "duplicate|similar|different",
  "confidence": 0.0-1.0,
  "reason": "brief explanation",
  "recommendation": "keep_first|keep_second|merge|keep_both"
}}

- duplicate: Essentially the same tip
- similar: Related but different enough to keep both
- different: Unrelated
"""

        try:
            response = self.client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            self.total_input_tokens += response.usage.input_tokens
            self.total_output_tokens += response.usage.output_tokens
            self.total_calls += 1
            self.pairs_verified += 1

            response_text = response.content[0].text.strip()

            # Remove markdown if present
            if response_text.startswith('```'):
                import re
                response_text = re.sub(r'^```(?:json)?\n', '', response_text)
                response_text = re.sub(r'\n```$', '', response_text)

            return json.loads(response_text)

        except Exception as e:
            print(f"    Error: {e}")
            return {
                "relationship": "different",
                "confidence": 0.0,
                "reason": f"Error: {str(e)}",
                "recommendation": "keep_both"
            }

    def process_file(self, file_path: Path) -> Dict:
        """Process a single file"""
        print(f"\n{'='*80}")
        print(f"Processing: {file_path.name}")
        print(f"{'='*80}")

        # Parse tips
        parser = TipParser()
        tips = parser.parse_file(file_path)
        print(f"  Found {len(tips)} tips")

        if len(tips) < 2:
            return {
                'file': file_path.name,
                'tips': len(tips),
                'duplicates': [],
                'similar': [],
                'all_tips': []
            }

        # Stage 1: Find similar pairs using embeddings
        similar_pairs = self.find_similar_pairs(tips)

        if not similar_pairs:
            print(f"  No similar pairs found - all tips are unique!")
            return {
                'file': file_path.name,
                'tips': len(tips),
                'duplicates': [],
                'similar': [],
                'all_tips': [{'id': t.id, 'title': t.title, 'line': t.line_number} for t in tips]
            }

        # Stage 2: Verify with AI (only high-similarity pairs)
        print(f"  Verifying {len(similar_pairs)} pairs with AI...")

        duplicates = []
        similar = []

        for idx, (i, j, cosine_sim) in enumerate(similar_pairs):
            if (idx + 1) % 10 == 0:
                print(f"    [{idx+1}/{len(similar_pairs)}]")

            result = self.verify_with_ai(tips[i], tips[j])
            result['tip1_id'] = tips[i].id
            result['tip2_id'] = tips[j].id
            result['tip1_title'] = tips[i].title
            result['tip2_title'] = tips[j].title
            result['tip1_line'] = tips[i].line_number
            result['tip2_line'] = tips[j].line_number
            result['cosine_similarity'] = float(cosine_sim)

            if result['relationship'] == 'duplicate':
                duplicates.append(result)
            elif result['relationship'] == 'similar':
                similar.append(result)

            time.sleep(0.2)  # Small delay

        print(f"\n  Results:")
        print(f"    Duplicates: {len(duplicates)}")
        print(f"    Similar: {len(similar)}")
        print(f"    Different: {len(similar_pairs) - len(duplicates) - len(similar)}")

        return {
            'file': file_path.name,
            'tips': len(tips),
            'pairs_filtered': self.pairs_filtered,
            'pairs_verified': len(similar_pairs),
            'duplicates': duplicates,
            'similar': similar,
            'all_tips': [{'id': t.id, 'title': t.title, 'line': t.line_number} for t in tips]
        }

    def print_summary(self):
        """Print cost summary"""
        input_cost_per_mtok = 0.25
        output_cost_per_mtok = 1.25

        input_cost = (self.total_input_tokens / 1_000_000) * input_cost_per_mtok
        output_cost = (self.total_output_tokens / 1_000_000) * output_cost_per_mtok
        total_cost = input_cost + output_cost

        print(f"\n{'='*80}")
        print("HYBRID DEDUPLICATION SUMMARY")
        print(f"{'='*80}")
        print(f"Pairs filtered by embeddings: {self.pairs_filtered:,} (saved ${self.pairs_filtered * 0.00265:.2f})")
        print(f"Pairs verified with AI: {self.pairs_verified:,}")
        print(f"API calls: {self.total_calls}")
        print(f"Input tokens: {self.total_input_tokens:,}")
        print(f"Output tokens: {self.total_output_tokens:,}")
        print(f"Total cost: ${total_cost:.2f}")
        print(f"{'='*80}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Hybrid deduplication with embeddings + AI')
    parser.add_argument('--input-dir', type=str, default='scripts/merged_tips',
                       help='Input directory')
    parser.add_argument('--output', type=str, default='scripts/dedup_report_hybrid.json',
                       help='Output report file')
    parser.add_argument('--threshold', type=float, default=0.7,
                       help='Cosine similarity threshold (0.0-1.0)')
    parser.add_argument('--file', type=str, default=None,
                       help='Process single file for testing')

    args = parser.parse_args()

    deduplicator = HybridDeduplicator(similarity_threshold=args.threshold)
    results = []

    if args.file:
        # Test on single file
        file_path = Path(args.input_dir) / args.file
        result = deduplicator.process_file(file_path)
        results.append(result)
    else:
        # Process all files
        files = sorted(Path(args.input_dir).glob('*.md'))
        print(f"Processing {len(files)} files...\n")

        for file_path in files:
            result = deduplicator.process_file(file_path)
            results.append(result)

    # Save report
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ Report saved to: {output_path}")
    deduplicator.print_summary()


if __name__ == '__main__':
    main()
