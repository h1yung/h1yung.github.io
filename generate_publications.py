import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List


def parse_bibtex(bib_file: str) -> List[Dict]:
    """Parse a BibTeX file into a list of entry dictionaries."""
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()

    entries: List[Dict] = []
    pattern = r"@(\w+)\{([^,]+),\s*([\s\S]*?)\n\}"

    for match in re.finditer(pattern, content):
        entry_type = match.group(1).lower()
        entry_key = match.group(2)
        fields_text = match.group(3)

        fields: Dict[str, str] = {"type": entry_type, "key": entry_key}
        field_pattern = r"(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*\"([^\"]*)\""

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
    if not author_string:
        return ""
    authors = [a.strip() for a in author_string.split(" and ")]
    formatted = []
    for author in authors:
        if "," in author:
            parts = author.split(",")
            formatted.append(f"{parts[1].strip()} {parts[0].strip()}")
        else:
            formatted.append(author)
    if len(formatted) <= 6:
        return ", ".join(formatted)
    return ", ".join(formatted[:7]) + ", ..."


def to_sentence_case(title: str) -> str:
    if not title:
        return ""
    return title[0].upper() + title[1:]


def entry_text(entry: Dict) -> str:
    authors = format_authors(entry.get("author", ""))
    title = to_sentence_case(entry.get("title", "Untitled"))
    journal = entry.get("journal", "").strip()
    book = entry.get("booktitle", "").strip()
    address = entry.get("address", "").strip()
    status = entry.get("status", "").strip()
    note = entry.get("note", "").strip()
    doi = entry.get("doi", "").strip()
    url = entry.get("url", "").strip()
    month = entry.get("month", "").strip()
    year = entry.get("year", "").strip()

    parts = []
    if authors:
        parts.append(authors)
    if title:
        parts.append(f"<span class=\"pub-title\">{title}</span>")

    venue_bits = []
    if journal:
        venue_bits.append(journal)
    if book:
        venue_bits.append(book)
    if address:
        venue_bits.append(address)

    if status:
        parts.append(f"(under review at {journal if journal else status})")
    elif note:
        parts.append(f"({note})")

    if venue_bits:
        parts.append(" – ".join(venue_bits))

    if month and year:
        parts.append(f"{month.capitalize()} {year}")
    elif year:
        parts.append(year)

    if doi:
        parts.append(f"doi:{doi}")
    if url:
        parts.append(url)

    return " ".join(parts)


def render_cards(grouped: Dict[str, List[Dict]]) -> str:
    html = []
    for year in sorted(grouped.keys(), reverse=True):
        html.append('<div class="year-row">')
        html.append(f'  <div class="year-label">{year}</div>')
        html.append('  <div class="year-stack">')
        for entry in grouped[year]:
            html.append('    <div class="publication-card">')
            html.append(f"      <div class=\"publication-body\">{entry_text(entry)}</div>")
            html.append('    </div>')
        html.append('  </div>')
        html.append('</div>')
    return "\n".join(html)


def generate_publications_page(bib_files: List[str], output_file: str) -> None:
    grouped: Dict[str, List[Dict]] = defaultdict(list)

    for bib_file in bib_files:
        if os.path.exists(bib_file):
            entries = parse_bibtex(bib_file)
            for e in entries:
                year = e.get("year", "n.d.").strip() or "n.d."
                grouped[year].append(e)

    # Stable sort inside each year: keep file order but ensure articles before others
    for year_entries in grouped.values():
        year_entries.sort(key=lambda x: (0 if x.get("type") == "article" else 1, x.get("title", "")))

    html_parts = [
        "---",
        "layout: archive",
        "title: \"Publications\"",
        "permalink: /publications/",
        "author_profile: true",
        "---",
        "",
        "<style>",
        ".year-row { display: grid; grid-template-columns: 5rem 1fr; gap: 1rem; align-items: start; margin: 1rem 0; }",
        ".year-label { font-weight: 700; color: #444; text-align: right; padding-top: 0.35rem; }",
        ".year-stack { display: grid; gap: 0.75rem; }",
        ".publication-card { border: 1px solid #e8e8e8; border-radius: 6px; background: #fff; padding: 0.75rem 1rem; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }",
        ".publication-body { line-height: 1.55; }",
        ".publication-body .pub-title { font-weight: 700; font-style: italic; }",
        "@media (max-width: 640px) { .year-row { grid-template-columns: 1fr; } .year-label { text-align: left; } }",
        "</style>",
        "",
    ]

    html_parts.append(render_cards(grouped))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))

    total = sum(len(v) for v in grouped.values())
    print(f"Generated {output_file} with {total} entries across {len(grouped)} years")


def main() -> None:
    root = Path(__file__).parent
    bib_files = [
        str(root / "markdown_generator" / "pubs.bib"),
        str(root / "markdown_generator" / "proceedings.bib"),
    ]
    output_file = str(root / "_pages" / "publications.md")
    generate_publications_page(bib_files, output_file)


if __name__ == "__main__":
    main()
