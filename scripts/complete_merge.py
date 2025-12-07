#!/usr/bin/env python3
"""
Complete merge script that handles all files, including renaming related files
and copying unpaired files.
"""

import os
import shutil
from pathlib import Path
from typing import Dict, Set, Tuple

def identify_related_files() -> Dict[str, str]:
    """
    Identify files that are related but have different names.
    Returns mapping of extracted_tips filename -> data filename
    """

    # Manual mapping of related files based on analysis
    # Format: extracted_tips_name -> data_name
    related_files = {
        'autocmds.md': 'autocommands.md',
        'integration.md': 'integration_tips.md',
        'filetype.md': 'filetype_specific_tips.md',
        'session-management.md': 'session.md',
        'search_replace.md': 'search.md',
        # search-replace.md is empty (0 tips), skip it
    }

    return related_files


def rename_extracted_files(extracted_dir: Path, rename_map: Dict[str, str]):
    """Rename files in extracted_tips/ to match data/ filenames"""

    print("\n" + "="*80)
    print("STEP 1: Renaming related files in extracted_tips/")
    print("="*80)

    for old_name, new_name in rename_map.items():
        old_path = extracted_dir / old_name
        new_path = extracted_dir / new_name

        if not old_path.exists():
            print(f"  ⚠️  {old_name} not found, skipping")
            continue

        if new_path.exists():
            print(f"  ⚠️  {new_name} already exists in extracted_tips/, skipping rename")
            continue

        # Count tips before rename
        content = old_path.read_text()
        tip_count = content.count('\n## ')

        print(f"  ✓ Renaming: {old_name} → {new_name} ({tip_count} tips)")
        old_path.rename(new_path)


def copy_unpaired_files(data_dir: Path, extracted_dir: Path, merged_dir: Path):
    """Copy files that exist only in data/ directly to merged_tips/"""

    print("\n" + "="*80)
    print("STEP 2: Copying unpaired files from data/")
    print("="*80)

    data_files = set(f.name for f in data_dir.glob('*.md'))
    extracted_files = set(f.name for f in extracted_dir.glob('*.md'))

    # Files only in data/ (no pair in extracted_tips/)
    unpaired = data_files - extracted_files

    print(f"\nFound {len(unpaired)} files only in data/ (will copy as-is)")

    for filename in sorted(unpaired):
        src = data_dir / filename
        dst = merged_dir / filename

        tip_count = src.read_text().count('\n# Title:')
        print(f"  ✓ Copying: {filename} ({tip_count} tips)")
        shutil.copy2(src, dst)


def convert_and_copy_extracted_only(extracted_dir: Path, data_dir: Path, merged_dir: Path):
    """Convert and copy files that exist only in extracted_tips/"""

    print("\n" + "="*80)
    print("STEP 3: Converting and copying unpaired files from extracted_tips/")
    print("="*80)

    data_files = set(f.name for f in data_dir.glob('*.md'))
    extracted_files = set(f.name for f in extracted_dir.glob('*.md'))

    # Files only in extracted_tips/ (no pair in data/)
    unpaired = extracted_files - data_files

    # Filter out empty files
    non_empty_unpaired = []
    for filename in unpaired:
        content = (extracted_dir / filename).read_text()
        tip_count = content.count('\n## ')
        if tip_count > 0:
            non_empty_unpaired.append((filename, tip_count))

    if not non_empty_unpaired:
        print("\n  No unpaired files with tips in extracted_tips/")
        return

    print(f"\nFound {len(non_empty_unpaired)} non-empty files only in extracted_tips/")

    # These need to be converted from new format to old format
    # We'll do this by parsing and converting
    from merge_tips import TipParser

    for filename, tip_count in sorted(non_empty_unpaired):
        src = extracted_dir / filename
        dst = merged_dir / filename

        print(f"  ✓ Converting: {filename} ({tip_count} tips)")

        # Parse new format
        content = src.read_text()
        parser = TipParser()
        tips = parser.parse_new_format(content, filename)

        # Write in old format
        with open(dst, 'w') as f:
            for tip in tips:
                f.write(tip.to_markdown())


def main():
    """Main function"""

    data_dir = Path('data')
    extracted_dir = Path('scripts/extracted_tips')
    merged_dir = Path('scripts/merged_tips')

    print("="*80)
    print("COMPLETE MERGE - All Files")
    print("="*80)
    print(f"\nSource directories:")
    print(f"  data/: {len(list(data_dir.glob('*.md')))} files")
    print(f"  extracted_tips/: {len(list(extracted_dir.glob('*.md')))} files")

    # Clean merged_tips directory
    print(f"\nCleaning merged_tips/ directory...")
    if merged_dir.exists():
        shutil.rmtree(merged_dir)
    merged_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Rename related files
    rename_map = identify_related_files()
    rename_extracted_files(extracted_dir, rename_map)

    # Step 2: Copy unpaired data/ files
    copy_unpaired_files(data_dir, extracted_dir, merged_dir)

    # Step 3: Convert and copy unpaired extracted_tips/ files
    convert_and_copy_extracted_only(extracted_dir, data_dir, merged_dir)

    # Step 4: Run merge script on matched pairs
    print("\n" + "="*80)
    print("STEP 4: Running merge script on all matching file pairs")
    print("="*80)
    print("\nThis will take 10-15 minutes...")
    print("(The merge script will handle files that exist in BOTH directories)\n")

    # Import and run the merge
    import subprocess
    result = subprocess.run(
        ['python', 'scripts/merge_tips.py'],
        capture_output=True,
        text=True
    )

    # Print merge output
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

    # Final summary
    print("\n" + "="*80)
    print("COMPLETE MERGE SUMMARY")
    print("="*80)

    total_files = len(list(merged_dir.glob('*.md')))
    total_tips = 0

    for file in merged_dir.glob('*.md'):
        content = file.read_text()
        tips = content.count('\n# Title:')
        total_tips += tips

    print(f"\nFinal result in scripts/merged_tips/:")
    print(f"  Total files: {total_files}")
    print(f"  Total tips: {total_tips}")
    print(f"\nOriginal data/ had: {len(list(data_dir.glob('*.md')))} files")
    print(f"Original extracted_tips/ had: {len(list(extracted_dir.glob('*.md')))} files")
    print(f"\n✓ Complete merge finished!")


if __name__ == '__main__':
    main()
