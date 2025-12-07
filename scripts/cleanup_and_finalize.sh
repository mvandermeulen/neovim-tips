#!/bin/bash
# Cleanup and finalize after deduplication

set -e  # Exit on error

echo "========================================="
echo "Cleanup and Finalize Tip Collection"
echo "========================================="
echo ""

# Check if cleaned tips exist
if [ ! -d "scripts/merged_tips_cleaned" ]; then
    echo "ERROR: scripts/merged_tips_cleaned/ does not exist!"
    echo "Run apply_deduplication.py first."
    exit 1
fi

# 1. Backup current data
echo "1. Backing up current data/ directory..."
if [ -d "data.backup" ]; then
    rm -rf data.backup.old
    mv data.backup data.backup.old
fi
cp -r data/ data.backup/
echo "   ✓ Backup created: data.backup/"

# 2. Replace data files
echo ""
echo "2. Replacing data/ with cleaned tips..."
rm -f data/*.md
cp scripts/merged_tips_cleaned/*.md data/
echo "   ✓ Copied $(ls data/*.md | wc -l | xargs) cleaned files"

# 3. Archive temporary files
echo ""
echo "3. Archiving temporary files..."
mkdir -p archive
tar -czf "archive/extraction_$(date +%Y%m%d_%H%M%S).tar.gz" \
    scripts/extracted_tips/ \
    scripts/merged_tips/ \
    scripts/processed_urls.json \
    scripts/vim_wiki_urls.txt \
    scripts/merge_checkpoints/ \
    scripts/dedup_checkpoints/ 2>/dev/null || true
echo "   ✓ Archive created: archive/extraction_*.tar.gz"

# 4. Keep valuable files
echo ""
echo "4. Keeping valuable scripts and results..."
echo "   ✓ scripts/deduplicate_within_files.py"
echo "   ✓ scripts/apply_deduplication.py"
echo "   ✓ scripts/extract_vim_tips.py"
echo "   ✓ scripts/merge_tips.py"
echo "   ✓ scripts/complete_merge.py"
echo "   ✓ scripts/crawl_vim_wiki.py"
echo "   ✓ scripts/dedup_report.json"
echo "   ✓ scripts/dedup.log"

# 5. Remove temporary directories (optional - uncomment to auto-delete)
# echo ""
# echo "5. Removing temporary directories..."
# rm -rf scripts/extracted_tips/
# rm -rf scripts/merged_tips/
# rm -rf scripts/merged_tips_cleaned/
# rm -f scripts/processed_urls.json
# rm -f scripts/vim_wiki_urls.txt
# rm -rf scripts/merge_checkpoints/
# rm -rf scripts/dedup_checkpoints/
# echo "   ✓ Temporary files removed"

# 6. Summary
echo ""
echo "========================================="
echo "SUMMARY"
echo "========================================="
echo "Tips in data/: $(ls data/*.md | wc -l | xargs) files"
echo "Total tips: $(grep -c '^# Title:' data/*.md | awk -F: '{sum+=$2} END {print sum}')"
echo "Backup: data.backup/"
echo "Archive: archive/extraction_*.tar.gz"
echo ""
echo "Ready to commit!"
echo ""
echo "Suggested commit message:"
echo "  feat(tips): Add 2,000+ new tips from vim.fandom.com with AI deduplication"
echo ""
echo "To commit:"
echo "  git add data/*.md scripts/*.py .gitignore"
echo "  git commit -m 'feat(tips): Add 2,000+ new tips from vim.fandom.com'"
echo "========================================="
