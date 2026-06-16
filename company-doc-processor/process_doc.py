import sys
import os
import asyncio
from playwright.async_api import async_playwright
import subprocess

async def main():
    if len(sys.argv) < 3:
        print("Usage: python process_doc.py <url> <output_html>")
        sys.exit(1)
        
    url = sys.argv[1]
    output_html = sys.argv[2]
    
    print(f"Fetching {url} using Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        title = await page.title()
        # Get a clean text representation of the page
        body_text = await page.locator("body").inner_text()
        await browser.close()
        
    print(f"Fetched page title: {title}")
    
    # Save a temporary markdown file
    temp_md = "temp_doc.md"
    with open(temp_md, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Processed from URL: {url}\n\n")
        f.write("## Page Content\n\n")
        f.write(body_text)
        
    print("Converting Markdown to HTML using Pandoc...")
    try:
        subprocess.run(["pandoc", temp_md, "-o", output_html], check=True)
        print(f"Successfully converted to {output_html} using Pandoc!")
    except Exception as e:
        print(f"Pandoc conversion failed: {e}")
    finally:
        if os.path.exists(temp_md):
            os.remove(temp_md)

if __name__ == "__main__":
    asyncio.run(main())
