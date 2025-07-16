import argparse
import os
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD


def download_webpage(url: str, output_dir: str):
=======
from fpdf import FPDF
import json
import csv

# Directory where scraped information is stored by default
SCRAP_DIR = "scrapped"

# Exported symbols
__all__ = [
    "download_webpage",
    "print_file",
    "store_content",
]


def store_content(text: str, name: str, output_dir: str):
    """Save scraped text to PDF, JSON, and CSV."""
    os.makedirs(output_dir, exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.splitlines():
        pdf.multi_cell(0, 10, txt=line)
    pdf.output(os.path.join(output_dir, f"{name}.pdf"))

    with open(os.path.join(output_dir, f"{name}.json"), "w", encoding="utf-8") as f_json:
        json.dump({"content": text}, f_json, ensure_ascii=False, indent=2)

    with open(os.path.join(output_dir, f"{name}.csv"), "w", newline="", encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["content"])
        for line in text.splitlines():
            writer.writerow([line])


def download_webpage(url: str, output_dir: str = SCRAP_DIR):
>>>>>>> 4f26e73ccf843b81ba0a9bbe292a6c3b627bb5f7
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    html_path = os.path.join(output_dir, "page.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
<<<<<<< HEAD
    file_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.search(r"\.(pdf|docx?|xlsx?|csv|jpg|png|gif|txt)$", href, re.IGNORECASE):
=======
    page_text = soup.get_text(separator="\n")
    file_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.search(r"\.(pdf|docx?|xlsx?|csv|jpg|png|gif|txt|json)$", href, re.IGNORECASE):
>>>>>>> 4f26e73ccf843b81ba0a9bbe292a6c3b627bb5f7
            file_links.append(href)

    downloaded_files = []
    for link in file_links:
        file_url = link
        if not re.match(r"^https?://", file_url):
            file_url = urljoin(url, file_url)
        file_name = os.path.basename(file_url.split("?")[0])
        out_path = os.path.join(output_dir, file_name)
        r = requests.get(file_url)
        with open(out_path, "wb") as f:
            f.write(r.content)
        downloaded_files.append(out_path)
<<<<<<< HEAD
    return html_path, downloaded_files


def print_file(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    print(content)
=======

    store_content(page_text, "page", output_dir)
    return html_path, downloaded_files, page_text


def print_file(file_path: str, output_dir: str = SCRAP_DIR):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    print(content)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    store_content(content, base_name, output_dir)
>>>>>>> 4f26e73ccf843b81ba0a9bbe292a6c3b627bb5f7


def main():
    parser = argparse.ArgumentParser(description="Simple web and file scraper")
    parser.add_argument("--url", help="URL of the web page to scrape")
    parser.add_argument("--file", help="Local file path to display")
<<<<<<< HEAD
    parser.add_argument(
        "--output", default="output", help="Directory to save scraped data"
    )
    args = parser.parse_args()

    if args.url:
        html_path, files = download_webpage(args.url, args.output)
=======
    parser.add_argument("--output", default=SCRAP_DIR, help="Directory to save scraped data")
    args = parser.parse_args()

    if args.url:
        html_path, files, _text = download_webpage(args.url, args.output)
>>>>>>> 4f26e73ccf843b81ba0a9bbe292a6c3b627bb5f7
        print(f"Saved HTML to {html_path}")
        if files:
            print("Downloaded files:")
            for path in files:
                print(f" - {path}")
    if args.file:
<<<<<<< HEAD
        print_file(args.file)
=======
        print_file(args.file, args.output)
>>>>>>> 4f26e73ccf843b81ba0a9bbe292a6c3b627bb5f7


if __name__ == "__main__":
    main()
