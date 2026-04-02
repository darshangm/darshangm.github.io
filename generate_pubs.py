#!/usr/bin/env python3
"""
generate_pubs.py
Reads journal_papers.bib and conf_papers.bib and writes _pages/publications.md.

Usage:
    python generate_pubs.py

Optional per-entry extras (add these fields to any .bib entry to get links):
    arxiv     = {2602.21429}
    url       = {https://ieeexplore.ieee.org/...}
    pdf       = {/files/mypaper.pdf}
    webpage   = {/papers/active-probing-multimodal-predictions/}
    video     = {https://www.youtube.com/watch?v=...}
    code      = {https://github.com/darshangm/...}
"""

import bibtexparser
import re
import os

# ── paths ────────────────────────────────────────────────────────────────────
JOURNAL_BIB = "_publications/journal_papers.bib"
CONF_BIB    = "_publications/conf_papers.bib"
OUT_FILE    = "_pages/publications.md"

# ── helpers ───────────────────────────────────────────────────────────────────
def clean(s):
    """Strip LaTeX commands (\\textbf{}, braces, etc.) from a string."""
    if not s:
        return ""
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\textit\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\{([^}]*)\}', r'\1', s)
    s = s.replace("\\&", "&").replace("D`sa", "D'sa")
    return s.strip().strip(',').strip()

def parse_authors(raw):
    """
    Return a formatted author string, bolding 'D. Gadginmath' and
    abbreviating first names.  Handles 'Last, First' and 'First Last'.
    """
    parts = [a.strip() for a in raw.split(" and ") if a.strip()]
    formatted = []
    for p in parts:
        p = clean(p)
        p = p.strip().strip(',').strip()
        # normalise: if already 'Last, First' flip it
        if ',' in p:
            last, first = p.split(',', 1)
            name = f"{first.strip()} {last.strip()}"
        else:
            name = p
        # bold Darshan
        if re.search(r'Gadginmath', name, re.I):
            name = f"**{name}**"
        formatted.append(name)
    if len(formatted) == 0:
        return ""
    if len(formatted) == 1:
        return formatted[0]
    return ", ".join(formatted[:-1]) + ", and " + formatted[-1]

def infer_status(venue):
    """Return one of: 'arxiv', 'review', 'published'."""
    v = venue.lower()
    if "arxiv" in v:
        return "arxiv"
    if "under review" in v or "to appear" in v:
        return "review"
    return "published"

def venue_display(e, pub_type):
    """Return a clean venue string, stripping status suffixes."""
    raw = e.get('journal') or e.get('booktitle') or ""
    v = clean(raw)
    v = re.sub(r'\s*\(under review\)', '', v, flags=re.I)
    v = re.sub(r'\s*\(to appear\)', '', v, flags=re.I)
    v = re.sub(r'\s*\(under review\)', '', v, flags=re.I)
    return v.strip()

def build_links(e):
    """Build list of (label, url) from optional bib fields."""
    links = []
    if 'arxiv' in e:
        links.append(("arXiv", f"https://arxiv.org/abs/{clean(e['arxiv'])}"))
    elif 'journal' in e and 'arxiv preprint arxiv:' in e['journal'].lower():
        m = re.search(r'arXiv:(\S+)', e['journal'], re.I)
        if m:
            links.append(("arXiv", f"https://arxiv.org/abs/{m.group(1)}"))
    if 'url' in e:
        links.append(("Paper", clean(e['url'])))
    if 'pdf' in e:
        links.append(("PDF", clean(e['pdf'])))
    if 'webpage' in e:
        links.append(("Project page", clean(e['webpage'])))
    if 'video' in e:
        links.append(("Video", clean(e['video'])))
    if 'code' in e:
        links.append(("Code", clean(e['code'])))
    return links

def status_badge(status):
    if status == "arxiv":
        return '<span class="pub-badge pub-badge--arxiv">preprint</span>'
    if status == "review":
        return '<span class="pub-badge pub-badge--review">under review</span>'
    return ""

def render_entry(e, number, pub_type):
    title   = clean(e.get('title', ''))
    authors = parse_authors(e.get('author', ''))
    year    = clean(e.get('year', ''))
    venue   = venue_display(e, pub_type)
    status  = infer_status(e.get('journal', '') + e.get('booktitle', ''))
    links   = build_links(e)

    vol   = clean(e.get('volume', ''))
    num   = clean(e.get('number', ''))
    pages = clean(e.get('pages', ''))
    vol_str = ""
    if vol:
        vol_str = f" {vol}"
        if num:
            vol_str += f"({num})"
        if pages:
            vol_str += f", pp. {pages}"

    link_html = ""
    if links:
        parts = [f'<a href="{url}" class="pub-link">{label}</a>' for label, url in links]
        link_html = "\n  " + " ".join(parts)

    badge = status_badge(status)
    badge_html = f"\n  {badge}" if badge else ""

    return (
        f'<div class="pub-entry">\n'
        f'  <span class="pub-number">{number}.</span>\n'
        f'  <div class="pub-body">\n'
        f'    <p class="pub-title">{title}</p>\n'
        f'    <p class="pub-authors">{authors}</p>\n'
        f'    <p class="pub-venue"><em>{venue}</em>{", " + year if year else ""}{vol_str}</p>'
        f'{badge_html}'
        f'{link_html}\n'
        f'  </div>\n'
        f'</div>\n'
    )

def load_bib(path):
    with open(path) as f:
        return bibtexparser.load(f).entries

def sort_entries(entries):
    """Sort descending by year, keeping order within year."""
    return sorted(entries, key=lambda e: int(e.get('year', 0)), reverse=True)

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    journals = sort_entries(load_bib(JOURNAL_BIB))
    confs    = sort_entries(load_bib(CONF_BIB))

    lines = []
    lines.append("""\
---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
.pub-section-title {
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #888;
  margin: 2rem 0 1rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid #2a2a2a;
}
.pub-entry {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1.4rem;
  align-items: flex-start;
}
.pub-number {
  font-size: 0.75rem;
  color: #666;
  min-width: 1.5rem;
  padding-top: 0.15rem;
  text-align: right;
}
.pub-body { flex: 1; }
.pub-title {
  font-size: 0.9rem;
  font-weight: 500;
  margin: 0 0 0.2rem;
  line-height: 1.4;
}
.pub-authors {
  font-size: 0.8rem;
  color: #aaa;
  margin: 0 0 0.2rem;
}
.pub-venue {
  font-size: 0.8rem;
  color: #888;
  margin: 0 0 0.4rem;
}
.pub-badge {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 500;
  padding: 1px 7px;
  border-radius: 10px;
  margin-right: 4px;
  vertical-align: middle;
}
.pub-badge--arxiv  { background: #1e1e2e; color: #AFA9EC; }
.pub-badge--review { background: #2a2010; color: #EF9F27; }
.pub-link {
  display: inline-block;
  font-size: 0.72rem;
  color: #5DCAA5;
  border: 0.5px solid #2a4a3e;
  border-radius: 4px;
  padding: 1px 8px;
  margin-right: 4px;
  text-decoration: none;
}
.pub-link:hover { background: #1a2a24; }
</style>

<p style="font-size:0.85rem; color:#aaa;">
  Full list also on <a href="https://scholar.google.com/citations?user=FYkk5xUAAAAJ&hl=en">Google Scholar</a>.
</p>
""")

    lines.append('<div class="pub-section-title">Journal articles</div>\n')
    for i, e in enumerate(journals, 1):
        lines.append(render_entry(e, i, "journal"))

    lines.append('\n<div class="pub-section-title">Conference proceedings</div>\n')
    for i, e in enumerate(confs, 1):
        lines.append(render_entry(e, i, "conf"))

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, 'w') as f:
        f.write("\n".join(lines))

    print(f"Wrote {len(journals)} journal + {len(confs)} conference entries → {OUT_FILE}")

if __name__ == "__main__":
    main()