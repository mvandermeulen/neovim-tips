#!/usr/bin/env python3
"""
Fix source links in tip files to use proper markdown format.
Changes from: **Source:** ** https://vim.fandom.com/wiki/...
To: **Source:** [vim.fandom.com](https://vim.fandom.com/wiki/...)
"""

import re
from pathlib import Path

def fix_source_links(data_dir: Path, dry_run: bool = False):
    """Fix all source links to use proper markdown format"""

    # Pattern to match: **Source:** ** https://vim.fandom.com/wiki/...
    pattern = re.compile(r'\*\*Source:\*\* \*\* (https://vim\.fandom\.com/wiki/\S+)')

    files_modified = 0
    links_fixed = 0

    for md_file in sorted(data_dir.glob('*.md')):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all matches
        matches = pattern.findall(content)
        if not matches:
            continue

        # Replace with proper markdown links
        new_content = pattern.sub(r'**Source:** [vim.fandom.com](\1)', content)

        if dry_run:
            print(f"Would fix {len(matches)} link(s) in {md_file.name}")
        else:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed {len(matches)} link(s) in {md_file.name}")

        files_modified += 1
        links_fixed += len(matches)

    print(f"\n{'Would fix' if dry_run else 'Fixed'} {links_fixed} links across {files_modified} files")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Fix source links to markdown format')
    parser.add_argument('--data-dir', type=Path, default=Path('data'),
                        help='Directory containing tip files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be changed without modifying files')

    args = parser.parse_args()

    fix_source_links(args.data_dir, dry_run=args.dry_run)
