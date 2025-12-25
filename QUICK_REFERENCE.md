# Quick Reference Guide

## Starting the Development Server

Simply run:
```bash
./serve.sh
```

Or manually:
```bash
export PATH="/usr/local/opt/ruby/bin:$PATH"
bundle exec jekyll serve --livereload
```

Then visit: http://localhost:4000/

---

## Software Page

**Location:** `_pages/software.md`

**Features:**
- ✅ Expandable/collapsible sections
- ✅ Image previews in collapsed view
- ✅ Full content with screenshots when expanded
- ✅ Graceful handling of missing images

**To add a project:** Edit `_pages/software.md` and add a new `<div class="software-item">` block (see USAGE_GUIDE.md for template)

---

## Publications Page

**Location:** `_pages/publications.md` (AUTO-GENERATED)

**Source Files:**
- `markdown_generator/pubs.bib`
- `markdown_generator/proceedings.bib`

**Features:**
- ✅ Expandable/collapsible sections
- ✅ Automatic citation formatting
- ✅ Google Scholar links
- ✅ DOI and URL links (when available)
- ✅ Sorted by year (newest first)

**To add publications:**
1. Edit `.bib` files in `markdown_generator/`
2. Run: `python3 generate_publications.py`
3. Done! The page is regenerated automatically

---

## BibTeX Fields Supported

Required:
- `title`, `author`, `year`

Optional (but recommended):
- `abstract` - Shows in expanded view
- `doi` - Creates DOI link
- `url` - Creates URL link
- `keywords` - Listed below abstract
- `journal`, `booktitle`, `volume`, `number`, `pages` - For citation formatting

---

## Files Created/Modified

**New Files:**
- `generate_publications.py` - BibTeX parser and page generator
- `USAGE_GUIDE.md` - Detailed usage instructions
- `serve.sh` - Quick start script for Jekyll
- `QUICK_REFERENCE.md` - This file

**Modified Files:**
- `_pages/software.md` - Updated with expandable sections
- `_pages/publications.md` - Auto-generated with expandable publications
- `Gemfile` - Added `webrick` gem for Ruby 3.x compatibility

---

## Troubleshooting

**Jekyll won't start:**
```bash
# Ensure you're using Homebrew Ruby
which ruby  # Should show /usr/local/opt/ruby/bin/ruby

# If not, run:
export PATH="/usr/local/opt/ruby/bin:$PATH"
```

**Bundle install fails:**
```bash
# Set SDK paths for native extensions
export SDKROOT="/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk"
export CPLUS_INCLUDE_PATH="$SDKROOT/usr/include/c++/v1"
bundle install
```

**Publications not updating:**
```bash
# Regenerate from BibTeX
python3 generate_publications.py

# Jekyll should auto-reload, or restart it
./serve.sh
```

---

## Next Steps

1. **Add your software projects** to `_pages/software.md`
2. **Add/update publications** in `.bib` files and regenerate
3. **Add images** to `/images/` directory
4. **Customize colors** in the `<style>` blocks
5. **Push to GitHub** to deploy

---

## Permanent Setup (Optional)

To avoid setting PATH each time, add to your `~/.zshrc`:

```bash
# Add this line manually
export PATH="/usr/local/opt/ruby/bin:$PATH"
```

Then:
```bash
source ~/.zshrc
```
