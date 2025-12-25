#!/usr/bin/env python3
"""
Generate publications.md from BibTeX files with expandable sections.
This script parses .bib files and creates an expandable publication list
similar to the software page format.
"""

import re
import os
from pathlib import Path
from typing import Dict, List
from urllib.parse import quote


def parse_bibtex(bib_file: str) -> List[Dict]:
    """Parse BibTeX file and extract publication entries."""
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match @article, @inproceedings, @book, etc.
    entries = []
    pattern = r'@(\w+)\{([^,]+),\s*([\s\S]*?)\n\}'
    
    for match in re.finditer(pattern, content):
        entry_type = match.group(1)
        entry_key = match.group(2)
        fields_text = match.group(3)
        
        # Parse fields
        fields = {'type': entry_type, 'key': entry_key}
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*"([^"]*)"'
        
        for field_match in re.finditer(field_pattern, fields_text):
            if field_match.group(1):
                field_name = field_match.group(1).lower()
                field_value = field_match.group(2)
            else:
                field_name = field_match.group(3).lower()
                field_value = field_match.group(4)
            
            fields[field_name] = field_value.strip()
        
        entries.append(fields)
    
    return entries


def format_authors(author_string: str) -> str:
    """Format author names from BibTeX format."""
    if not author_string:
        return ""
    
    # Split by 'and'
    authors = [a.strip() for a in author_string.split(' and ')]
    
    # Format each author (assume "Last, First" or "First Last" format)
    formatted = []
    for author in authors:
        if ',' in author:
            parts = author.split(',')
            formatted.append(f"{parts[1].strip()} {parts[0].strip()}")
        else:
            formatted.append(author)
    
    if len(formatted) == 1:
        return formatted[0]
    elif len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    else:
        return ', '.join(formatted[:-1]) + f", and {formatted[-1]}"


def generate_citation(entry: Dict) -> str:
    """Generate a formatted citation string."""
    authors = format_authors(entry.get('author', ''))
    title = entry.get('title', 'Untitled')
    year = entry.get('year', 'n.d.')
    
    citation = f"{authors}. \"{title}.\""
    
    if entry['type'] == 'article':
        journal = entry.get('journal', '')
        volume = entry.get('volume', '')
        number = entry.get('number', '')
        pages = entry.get('pages', '')
        
        if journal:
            citation += f" <em>{journal}</em>"
        if volume:
            citation += f" {volume}"
        if number:
            citation += f" ({number})"
        if pages:
            citation += f": {pages}"
        citation += f", {year}."
    
    elif entry['type'] == 'inproceedings' or entry['type'] == 'conference':
        booktitle = entry.get('booktitle', '')
        if booktitle:
            citation += f" In <em>{booktitle}</em>, {year}."
        else:
            citation += f" {year}."
    
    elif entry['type'] == 'book':
        publisher = entry.get('publisher', '')
        if publisher:
            citation += f" {publisher}, {year}."
        else:
            citation += f" {year}."
    
    else:
        citation += f" {year}."
    
    return citation


def create_google_scholar_link(title: str) -> str:
    """Create a Google Scholar search link for the publication."""
    query = quote(title)
    return f"https://scholar.google.com/scholar?q={query}"


def generate_html_entry(entry: Dict, index: int) -> str:
    """Generate HTML for a single publication entry with expandable section."""
    title = entry.get('title', 'Untitled')
    authors = format_authors(entry.get('author', ''))
    year = entry.get('year', 'n.d.')
    venue = entry.get('journal', entry.get('booktitle', entry.get('publisher', '')))
    citation = generate_citation(entry)
    scholar_link = create_google_scholar_link(title)
    
    # Get additional metadata for expanded section
    abstract = entry.get('abstract', '')
    doi = entry.get('doi', '')
    url = entry.get('url', '')
    keywords = entry.get('keywords', '')
    
    # Create preview text (authors + venue + year)
    preview_text = f"{authors[:80]}{'...' if len(authors) > 80 else ''}"
    if venue:
        preview_text += f" • {venue}"
    preview_text += f" • {year}"
    
    html = f'''<div class="publication-item">
  <details>
    <summary>
      <div class="publication-preview">
        <div>
          <strong>{title}</strong>
          <div class="publication-meta">{preview_text}</div>
        </div>
      </div>
    </summary>
    <div class="publication-content">
      <p class="citation">{citation}</p>
'''
    
    if abstract:
        html += f'''      
      <h4>Abstract</h4>
      <p class="abstract">{abstract}</p>
'''
    
    if keywords:
        html += f'''      
      <p><strong>Keywords:</strong> {keywords}</p>
'''
    
    html += '''      
      <div class="publication-links">
'''
    
    if doi:
        html += f'''        <a href="https://doi.org/{doi}" target="_blank">DOI</a>
'''
    
    if url:
        html += f'''        <a href="{url}" target="_blank">URL</a>
'''
    
    html += f'''        <a href="{scholar_link}" target="_blank">Google Scholar</a>
      </div>
    </div>
  </details>
</div>

'''
    
    return html


def generate_publications_page(bib_files: List[str], output_file: str):
    """Generate the publications.md file from BibTeX files."""
    
    # Parse all BibTeX files
    all_entries = []
    for bib_file in bib_files:
        if os.path.exists(bib_file):
            entries = parse_bibtex(bib_file)
            all_entries.extend(entries)
    
    # Sort by year (descending)
    all_entries.sort(key=lambda x: int(x.get('year', '0')), reverse=True)
    
    # Generate HTML
    html_content = '''---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
.publication-item {
  margin: 0.75em 0;
  border: 1px solid #e8e8e8;
  border-radius: 4px;
  overflow: hidden;
}

.publication-item details {
  background: #f9f9f9;
}

.publication-item summary {
  padding: 0.75em 1em;
  cursor: pointer;
  font-size: 0.95em;
  background: #fff;
  border-bottom: 1px solid #e8e8e8;
  transition: background 0.3s;
  list-style: none;
  display: flex;
  align-items: center;
}

.publication-item summary::-webkit-details-marker {
  display: none;
}

.publication-item summary::before {
  content: "▶";
  display: inline-block;
  transition: transform 0.3s;
  margin-right: 0.5em;
  flex-shrink: 0;
}

.publication-item details[open] summary::before {
  transform: rotate(90deg);
}

.publication-item summary:hover {
  background: #f5f5f5;
}

.publication-preview {
  display: flex;
  align-items: flex-start;
  gap: 1em;
}

.publication-content {
  padding: 0.75em 1em;
  background: #fff;
  line-height: 1.4;
  font-size: 0.9em;
}

.publication-meta {
  color: #666;
  font-size: 0.85em;
  margin-top: 0.25em;
}

.citation {
  font-size: 0.85em;
  line-height: 1.4;
  margin-bottom: 0.75em;
  padding: 0.5em 0.75em;
  background: #f8f8f8;
  border-left: 2px solid #0366d6;
}

.abstract {
  text-align: justify;
  margin: 0.5em 0;
  font-size: 0.9em;
}

.publication-content h4 {
  margin-top: 0.75em;
  margin-bottom: 0.35em;
  color: #333;
  font-size: 1em;
}

.publication-links {
  margin-top: 0.75em;
  padding-top: 0.5em;
  border-top: 1px solid #e8e8e8;
}

.publication-links a {
  display: inline-block;
  margin-right: 0.5em;
  margin-bottom: 0.25em;
  padding: 0.35em 0.75em;
  background: #0366d6;
  color: white;
  text-decoration: none;
  border-radius: 3px;
  font-size: 0.85em;
  transition: background 0.3s;
}

.publication-links a:hover {
  background: #0256c2;
}
</style>

'''
    
    # Add publication entries
    for i, entry in enumerate(all_entries):
        html_content += generate_html_entry(entry, i)
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated {output_file} with {len(all_entries)} publications")


def main():
    """Main function to generate publications page."""
    # Set paths
    script_dir = Path(__file__).parent
    bib_files = [
        script_dir / 'markdown_generator' / 'pubs.bib',
        script_dir / 'markdown_generator' / 'proceedings.bib',
    ]
    
    output_file = script_dir / '_pages' / 'publications.md'
    
    # Generate the page
    generate_publications_page(bib_files, output_file)


if __name__ == '__main__':
    main()
