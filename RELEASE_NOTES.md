# Release Notes v0.8.0

## 🎉 Major Updates

### Massive Content Expansion
- **Added 2,000+ new tips** from vim.fandom.com (extracted from 3,397 pages)
- Merged with existing 1,038 tips for a total of **2,770 unique tips**
- **167% growth** - increased from 1,038 to 2,770 tips (1,732 new unique tips)
- All new tips include both Vimscript and Lua code examples

### Revolutionary Hybrid Deduplication
- Developed breakthrough cost-effective deduplication approach
- Uses sentence-transformers embeddings + cosine similarity pre-filtering
- Only AI-verifies high-similarity pairs (>0.75 threshold)
- **99.82% cost savings** ($0.20 vs $112 for full AI comparison)
- Removed 484 duplicate tips (409 cross-file + 75 within-file duplicates)

### PDF Book Improvements
- **Language labels**: Code examples now labeled as "Example (Vim)" or "Example (Neovim)"
  - 2,500 Vimscript examples
  - 1,944 Neovim Lua examples
- **Blue hyperlinks**: All links now display in standard blue color (RGB 0,102,204)
- **Fixed PDF generation**: Resolved LaTeX compilation errors
  - Smart markdown parsing for underscores and asterisks
  - Fixed code fence handling
- **Enhanced formatting**: Support for bold, italic, and hyperlinks
- **Removed ligatures** from code blocks for better readability
- Updated book cover design
- Final PDF: **1,604 pages, 6.5 MB**

## ✨ New Features

- Language-specific labels for code examples in PDF book (#0f96638)
- Bulk buffer closing tips (#d499215)
- File operation tips (#f506e99)
- UI, exit, and marks tips (#70157bb)
- Option to remove footer from daily tip (#118af52)
- Community contribution from Julian Frenzel (#7318eb4, #29)

## 🐛 Bug Fixes

### PDF Generation
- Fixed LaTeX compilation errors that halted at various pages (#8cf870d)
- Improved markdown-to-LaTeX conversion for special characters
- Fixed handling of `snake_case`, `* registers`, and other edge cases
- Resolved unclosed backtick issues in code examples

### Tips Quality
- Removed 75 duplicate titles across different files (#3efa5f3)
- Fixed duplicate titles (#347c45b, #061a468)
- Improved yank+delete+clipboard interaction tip (#bedbc45)
- Fixed extmark conceal property documentation (#63aa4f9)
- Fixed extmarks tips errors (#2383b5a)

### Source Formatting
- Formatted 1,686 source links as proper markdown links (#8e0875f)
- Cleaned up 355 community contributed source lines (#0c13a90)
- Removed trailing whitespace (#a640b8f)

### Plugin Functionality
- Fixed lazy loading issue: `:NeovimTipsRandom` now works immediately (#655408a)

## 📚 Documentation Improvements

- Added missing Lua examples in:
  - `builtin_functions.md` (#ca9c36a)
  - `autocommands.md` (#88ac590)
  - `advanced_options.md` (#c10f6b6)
  - `advanced_mappings.md` (#12d8228)
- Added Lua snippets where only Vimscript was present (#b2cb106)
- Clarified lazy loading configuration (#a60ba91, #84d044b)
- Added note about empty `opts` table requirement (#001de6b)
- Fixed `vim.keymap.set` documentation (noremap by default) (#2e84efa)
- Fixed typos in UI chapter (#81b6173)
- Style fixes (#2802088)

## 🛠️ Development & Infrastructure

### Reusable Scripts
Added powerful, reusable scripts for tip management:
- **`dedup_hybrid.py`**: Cost-effective hybrid deduplication (99.82% savings)
- **`apply_deduplication.py`**: Apply dedup results (conservative/merge modes)
- **`complete_merge.py`**: Intelligent tip merging with file renaming
- **`cleanup_and_finalize.sh`**: Automated deployment workflow
- **`dedup_across_files.py`**: Remove duplicate titles across files
- **`fix_source_links.py`**: Convert URLs to markdown format
- **`fix_community_sources.py`**: Clean up source formatting

### Build System
- Updated PDF build script with improved LaTeX generation (#build_tex.py)
- Added Python dependencies tracking (#7498224)
- Improved `.gitignore` for log files and build artifacts (#3d9c5ce, #a6d85a0)

## 📊 Statistics

### Content Growth
- **Before**: 1,038 tips across 64 files
- **After**: 2,770 tips across 69 files
- **Growth**: 167% increase (1,732 new unique tips)

### Sources
- 1,686 tips from [vim.fandom.com](https://vim.fandom.com)
- 355 community contributed tips
- 729 curated original tips

### Cost Efficiency
Total project cost for extraction and deduplication: **$4.36**
- Extraction from 3,397 pages: $3.56
- Merging tips: $0.60
- Hybrid deduplication: $0.20 (saved $107.64!)

### PDF Book
- **Pages**: 1,604 pages
- **Size**: 6.5 MB
- **Chapters**: 69
- **Code Examples**: 4,444 total (2,500 Vim + 1,944 Neovim)

## 🙏 Contributors

- **saxon** - Core development, tip extraction, deduplication
- **Nicolas Battisti** (@NickP-Devops) - Documentation improvements, Lua examples
- **qiine** - Bug fixes, typo corrections
- **AndyG** - Documentation fixes
- **Julian Frenzel** - Community tip contribution
- **Claude Code** - AI-assisted development and extraction

## 🔧 Breaking Changes

None. All changes are backward compatible.

## 📝 Notes

- The hybrid deduplication approach can be reused for future tip additions from other sources
- All scripts are documented in `scripts/README.md`
- PDF book generation is now stable and tested with 2,770 tips
- Recommended to use lazy loading with key bindings for optimal performance

## 🚀 What's Next

This release significantly expands the Neovim tips collection, making it one of the most comprehensive resources available. The hybrid deduplication approach and reusable scripts make it easy to continue growing the collection in the future.

---

**Full Changelog**: v0.7.4...v0.8.0
