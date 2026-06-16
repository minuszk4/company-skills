---
name: company-doc-processor
description: "Scrape a webpage using local Playwright and convert the content to HTML via local Pandoc."
version: 1.0.0
author: company-admin
license: Proprietary
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Web, Playwright, Pandoc, Scraper, Converter]
---

# Company Document Processor

This skill uses local Playwright and local Pandoc to scrape a webpage and convert it.

## Usage

```bash
python <SKILL_DIR>/process_doc.py <url> <output_html>
```
Substitute `<SKILL_DIR>` with the folder where this skill is located, or simply run `process_doc.py` in its local directory.

## Examples

```bash
# Fetch and convert a page
python C:/Users/tranv/Downloads/skills-shared/company/company-doc-processor/process_doc.py https://example.com example.html
```
