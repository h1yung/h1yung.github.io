# Usage Guide for Software and Publications Pages

## Software Page

The software page ([_pages/software.md](/_pages/software.md)) uses expandable sections (HTML `<details>` tags) to create collapsible content with image previews.

### Adding a New Software Project

Add a new `<div class="software-item">` block following this template:

```html
<div class="software-item">
  <details>
    <summary>
      <div class="software-preview">
        <img src="/images/your-project-preview.png" alt="Preview" onerror="this.style.display='none'">
        <div>
          <strong>Your Project Name</strong>
          <div class="software-meta">Brief one-line description</div>
        </div>
      </div>
    </summary>
    <div class="software-content">
      <p>Detailed description of your project goes here.</p>
      
      <h3>Features</h3>
      <ul>
        <li>Feature 1</li>
        <li>Feature 2</li>
      </ul>
      
      <img src="/images/screenshot-1.png" alt="Screenshot">
      
      <h3>Technical Details</h3>
      <p>Stack, architecture, etc.</p>
      
      <div class="software-links">
        <a href="https://github.com/user/repo" target="_blank">GitHub</a>
        <a href="https://demo.com" target="_blank">Live Demo</a>
      </div>
    </div>
  </details>
</div>
```

### Features

- **Collapsible sections**: Click to expand/collapse each project
- **Image previews**: Shows a thumbnail in the collapsed view
- **Full content**: Expanded view shows detailed descriptions, screenshots, and links
- **Graceful degradation**: Images that don't exist are automatically hidden using `onerror`

---

## Publications Page

The publications page is **automatically generated** from BibTeX files using the Python script `generate_publications.py`.

### How It Works

1. BibTeX entries are stored in:
   - `markdown_generator/pubs.bib`
   - `markdown_generator/proceedings.bib`

2. Run the generation script:
   ```bash
   python3 generate_publications.py
   ```

3. This creates/updates `_pages/publications.md` with expandable publication entries sorted by year (newest first)

### Adding New Publications

1. Edit your `.bib` files in `markdown_generator/`:

```bibtex
@article{smith2024example,
  title={Example Publication Title},
  author={Smith, John and Doe, Jane},
  journal={Journal Name},
  volume={10},
  number={2},
  pages={123-145},
  year={2024},
  publisher={Publisher Name},
  doi={10.1234/example},
  url={https://example.com/paper},
  abstract={Optional abstract text goes here...},
  keywords={machine learning, data science}
}
```

2. Run the generator:
```bash
python3 generate_publications.py
```

3. The script will:
   - Parse all BibTeX entries
   - Sort by year (descending)
   - Generate expandable HTML sections
   - Create formatted citations
   - Add Google Scholar search links
   - Include DOI and URL links if available

### Supported BibTeX Entry Types

- `@article` - Journal articles
- `@inproceedings` / `@conference` - Conference papers
- `@book` - Books
- Others - Basic formatting

### Optional Fields

- `abstract` - Displays in the expanded section
- `keywords` - Shows below the abstract
- `doi` - Creates a DOI link button
- `url` - Creates a URL link button

### Features

- **Auto-formatting**: Proper citation format based on entry type
- **Google Scholar**: Automatic search links for all publications
- **Expandable**: Click to see abstract, keywords, and full details
- **Sorted**: Publications are sorted by year (newest first)
- **Links**: DOI, URL, and Google Scholar buttons

---

## Styling

Both pages use consistent styling:
- Blue accent color: `#0366d6`
- Border color: `#e8e8e8`
- Hover effects on summaries
- Animated expand/collapse arrows
- Responsive layout

To customize colors, edit the `<style>` blocks in:
- `_pages/software.md`
- The `generate_publications.py` script (which generates the styles for publications)

---

## Local Development

To see your changes locally:

1. Ensure Ruby and Jekyll are set up (see README.md)
2. Run the local server:
   ```bash
   export PATH="/usr/local/opt/ruby/bin:$PATH"
   bundle exec jekyll serve --livereload
   ```
3. Visit http://localhost:4000/software/ or http://localhost:4000/publications/

The `--livereload` flag will automatically refresh your browser when files change.

---

## Tips

### Software Page
- Use high-quality preview images (recommended: 150x100px or larger)
- Keep the meta description brief (one line)
- Add multiple screenshots in the expanded content
- Include relevant links (GitHub, Demo, Paper, etc.)

### Publications Page
- Keep your `.bib` files well-organized
- Use consistent author name formatting
- Include abstracts when available (very helpful for readers)
- Add DOIs whenever possible
- Re-run `generate_publications.py` after any `.bib` changes

### Images
- Store images in `/images/` directory
- Use descriptive filenames
- Optimize images for web (compress before uploading)
- The `onerror="this.style.display='none'"` attribute hides broken images
