#!/usr/bin/env python3
"""
Script to migrate markdown files from HTML comment metadata to YAML frontmatter
"""
import os
import re
from pathlib import Path
from typing import Dict, Optional


def extract_html_metadata(content: str) -> Dict[str, str]:
    """Extract metadata from HTML comments"""
    metadata = {}

    # Pattern to match HTML comments with key: value
    pattern = r'<!--\s*(\w+):\s*([^-]+?)\s*-->'
    matches = re.findall(pattern, content)

    for key, value in matches:
        metadata[key.strip()] = value.strip()

    return metadata


def remove_html_comments(content: str) -> str:
    """Remove HTML comment metadata from content"""
    # Remove HTML comments that contain metadata
    pattern = r'<!--\s*\w+:\s*[^-]+?\s*-->\n?'
    content = re.sub(pattern, '', content)
    return content


def create_frontmatter(metadata: Dict[str, str], title: str) -> str:
    """Create YAML frontmatter from metadata"""
    frontmatter_lines = ['---', f'title: "{title}"']

    # Map old metadata keys to new frontmatter keys
    key_mapping = {
        'description': 'description',
        'date': 'date',
        'tags': 'tags',
        'status': 'status',
        'team_size': 'team_size',
        'company': 'company',
        'role': 'role',
        'technologies': 'technologies',
        'category': 'category',
    }

    for old_key, new_key in key_mapping.items():
        if old_key in metadata:
            value = metadata[old_key]

            # Handle tags as array
            if old_key == 'tags':
                tags = [tag.strip() for tag in value.split(',')]
                frontmatter_lines.append(f'{new_key}:')
                for tag in tags:
                    frontmatter_lines.append(f'  - {tag}')
            elif old_key == 'technologies':
                techs = [tech.strip() for tech in value.split(',')]
                frontmatter_lines.append(f'{new_key}:')
                for tech in techs:
                    frontmatter_lines.append(f'  - {tech}')
            else:
                # Escape quotes in values
                value = value.replace('"', '\\"')
                frontmatter_lines.append(f'{new_key}: "{value}"')

    frontmatter_lines.append('---')
    frontmatter_lines.append('')

    return '\n'.join(frontmatter_lines)


def extract_title_from_content(content: str) -> Optional[str]:
    """Extract title from markdown H1 heading"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def migrate_file(file_path: Path, dry_run: bool = False) -> bool:
    """Migrate a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has frontmatter
        if content.startswith('---'):
            print(f"  ⊘ {file_path.name} - Already has frontmatter")
            return False

        # Extract metadata from HTML comments
        metadata = extract_html_metadata(content)

        # Extract title
        title = extract_title_from_content(content)
        if not title:
            title = file_path.stem.replace('-', ' ').replace('_', ' ').title()

        # Remove HTML comments from content
        clean_content = remove_html_comments(content)

        # Remove the H1 title if it exists (we'll have it in frontmatter)
        clean_content = re.sub(r'^#\s+.+$\n?', '', clean_content, count=1, flags=re.MULTILINE)
        clean_content = clean_content.lstrip()

        # Create new content with frontmatter
        frontmatter = create_frontmatter(metadata, title)
        new_content = frontmatter + clean_content

        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ {file_path.name}")
        else:
            print(f"  ○ {file_path.name} - Would migrate")

        return True

    except Exception as e:
        print(f"  ✗ {file_path.name} - Error: {e}")
        return False


def migrate_directory(directory: Path, dry_run: bool = False):
    """Migrate all markdown files in a directory"""
    markdown_files = list(directory.rglob('*.md'))

    print(f"\nMigrating {len(markdown_files)} files in {directory.name}/")
    print("=" * 60)

    migrated = 0
    for md_file in markdown_files:
        if migrate_file(md_file, dry_run):
            migrated += 1

    print(f"\nMigrated: {migrated}/{len(markdown_files)}")


def main():
    """Main migration function"""
    import argparse

    parser = argparse.ArgumentParser(description='Migrate markdown files to Astro frontmatter')
    parser.add_argument('--dry-run', action='store_true', help='Run without making changes')
    parser.add_argument('--notes', action='store_true', help='Migrate notes directory')
    parser.add_argument('--projects', action='store_true', help='Migrate projects directory')
    parser.add_argument('--interviews', action='store_true', help='Migrate interviews directory')
    parser.add_argument('--all', action='store_true', help='Migrate all directories')

    args = parser.parse_args()

    base_dir = Path(__file__).parent

    if args.dry_run:
        print("\n🔍 DRY RUN MODE - No files will be modified\n")

    if args.all or args.notes:
        notes_dir = base_dir / 'notes'
        if notes_dir.exists():
            migrate_directory(notes_dir, args.dry_run)

    if args.all or args.projects:
        projects_dir = base_dir / 'projects'
        if projects_dir.exists():
            migrate_directory(projects_dir, args.dry_run)

    if args.all or args.interviews:
        interviews_dir = base_dir / 'interviews'
        if interviews_dir.exists():
            migrate_directory(interviews_dir, args.dry_run)

    if not (args.notes or args.projects or args.interviews or args.all):
        parser.print_help()


if __name__ == '__main__':
    main()
