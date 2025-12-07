# Reusable Vim/Neovim Tips Management Scripts

This directory contains reusable scripts for managing, merging, and deduplicating Vim/Neovim tips.

## Available Scripts

### 1. complete_merge.py
Merge tips from different sources with intelligent file renaming and duplicate detection.

```bash
python scripts/complete_merge.py \
  --source-dir <source_directory> \
  --target-dir <target_directory> \
  --output-dir scripts/merged_tips
```

**Features:**
- Automatically renames related files (e.g., autocmds.md → autocommands.md)
- Merges overlapping files
- Copies unpaired files to output directory
- Preserves tip format (# Title: / # Category: / # Tags:)

### 2. dedup_hybrid.py (Highly Recommended)
**Cost-effective hybrid deduplication using embeddings + AI verification**

This breakthrough approach reduced deduplication costs by **99.82%** compared to full AI comparison.

```bash
# Install dependencies first
pip install sentence-transformers scikit-learn anthropic python-dotenv

# Run deduplication on all files
python -u scripts/dedup_hybrid.py \
  --input-dir scripts/merged_tips \
  --output scripts/dedup_report_hybrid.json \
  --threshold 0.75 \
  2>&1 | tee scripts/dedup_hybrid.log

# Or test on single file
python scripts/dedup_hybrid.py \
  --file advanced_mappings.md \
  --threshold 0.75
```

**How it works:**
- **Stage 1:** Generate local embeddings using sentence-transformers (FREE)
- **Stage 2:** Calculate cosine similarity between all pairs (FREE, instant)
- **Stage 3:** Only verify high-similarity pairs (>0.75) with AI

**Cost comparison:**
- Full AI comparison: ~$112 for 69 files
- Hybrid approach: ~$0.20 for 69 files
- **Savings: 99.82%**

**Parameters:**
- `--threshold`: Cosine similarity threshold (0.0-1.0, default: 0.7)
  - 0.75 recommended for good balance
  - Higher = fewer AI calls, may miss some duplicates
  - Lower = more AI calls, more thorough

### 3. apply_deduplication.py
Apply deduplication results to create cleaned tip files.

```bash
# Conservative mode (recommended): Only remove clear duplicates
python scripts/apply_deduplication.py \
  --report scripts/dedup_report_hybrid.json \
  --input-dir scripts/merged_tips \
  --output-dir scripts/merged_tips_cleaned \
  --mode conservative

# Merge mode: Auto-merge similar tips with AI
python scripts/apply_deduplication.py \
  --mode merge
```

**Modes:**
- `conservative`: Only removes duplicates with confidence ≥ 0.9, keeps similar tips
- `merge`: Auto-merges similar tips with confidence ≥ 0.8 using AI

### 4. cleanup_and_finalize.sh
Automated deployment script for finalizing tip collection.

```bash
./scripts/cleanup_and_finalize.sh
```

**Actions:**
1. Backs up current `data/` directory to `data.backup/`
2. Replaces `data/*.md` with cleaned files from `scripts/merged_tips_cleaned/`
3. Archives temporary extraction files
4. Displays summary and suggested commit message

## Typical Workflow

When you have new tips to merge with existing collection:

```bash
# 1. Merge new tips with existing
python scripts/complete_merge.py \
  --source-dir <new_tips_directory> \
  --target-dir data \
  --output-dir scripts/merged_tips

# 2. Run hybrid deduplication
python -u scripts/dedup_hybrid.py \
  --input-dir scripts/merged_tips \
  --threshold 0.75 \
  2>&1 | tee scripts/dedup_hybrid.log

# 3. Apply deduplication results
python scripts/apply_deduplication.py \
  --report scripts/dedup_report_hybrid.json \
  --mode conservative

# 4. Finalize deployment
./scripts/cleanup_and_finalize.sh

# 5. Commit changes
git add data/*.md
git commit -m "feat(tips): Add new tips with hybrid deduplication"
```

## Environment Setup

Create `.env.scripts` file with your Anthropic API key:

```bash
ANTHROPIC_API_KEY=your_api_key_here
```

**Note:** Use `.env.scripts` (not `.env`) to avoid Claude Code using your API key.

## Previous Project Results

The hybrid deduplication approach was used successfully to extract and merge 2,000+ tips from vim.fandom.com:

| Metric | Value |
|--------|-------|
| Original tips | 1,038 |
| Extracted from vim.fandom.com | 2,111 |
| After merge | 3,078 |
| Duplicates found | 409 |
| **Final collection** | **2,770 unique tips** |
| **Net growth** | **167% (1,732 new tips)** |

| Cost Item | Amount |
|-----------|--------|
| Extraction (one-time) | $3.56 |
| Merge | $0.60 |
| Hybrid deduplication | $0.20 |
| **Total project cost** | **$4.36** |

## Tips for Cost Optimization

1. **Use hybrid deduplication** instead of full AI comparison (99.82% savings)
2. **Adjust threshold**: Start with 0.75, increase to 0.80 if too many AI calls
3. **Test first**: Use `--file` parameter to test on one file before full run
4. **Monitor costs**: Check API balance during long runs
5. **Use Haiku**: Scripts use Claude 3.5 Haiku (cheapest model)
