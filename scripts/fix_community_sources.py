#!/usr/bin/env python3
"""
Fix community contributed source lines to remove extra asterisks.
Changes from: **Source:** ** Community contributed
To: **Source:** Community contributed
"""

import re
from pathlib import Path

def fix_community_sources(data_dir: Path, dry_run: bool = False):
    """Fix community contributed source lines"""

    pattern = re.compile(r'\*\*Source:\*\* \*\* Community contributed')

    files_modified = 0
    lines_fixed = 0

    for md_file in sorted(data_dir.glob('*.md')):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all matches
        matches = pattern.findall(content)
        if not matches:
            continue

        # Replace with clean format
        new_content = pattern.sub('**Source:** Community contributed', content)

        if dry_run:
            print(f"Would fix {len(matches)} line(s) in {md_file.name}")
        else:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed {len(matches)} line(s) in {md_file.name}")

        files_modified += 1
        lines_fixed += len(matches)

    print(f"\n{'Would fix' if dry_run else 'Fixed'} {lines_fixed} lines across {files_modified} files")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Fix community contributed source lines')
    parser.add_argument('--data-dir', type=Path, default=Path('data'),
                        help='Directory containing tip files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be changed without modifying files')

    args = parser.parse_args()

    fix_community_sources(args.data_dir, dry_run=args.dry_run)
