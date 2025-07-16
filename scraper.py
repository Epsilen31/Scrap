import argparse
import os
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def download_webpage(url: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    html_path = os.path.join(output_dir, "page.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    file_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.search(r"\.(pdf|docx?|xlsx?|csv|jpg|png|gif|txt)$", href, re.IGNORECASE):
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
    return html_path, downloaded_files


def print_file(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    print(content)


def main():
    parser = argparse.ArgumentParser(description="Simple web and file scraper")
    parser.add_argument("--url", help="URL of the web page to scrape")
    parser.add_argument("--file", help="Local file path to display")
    parser.add_argument(
        "--output", default="output", help="Directory to save scraped data"
    )
    args = parser.parse_args()

    if args.url:
        html_path, files = download_webpage(args.url, args.output)
        print(f"Saved HTML to {html_path}")
        if files:
            print("Downloaded files:")
            for path in files:
                print(f" - {path}")
    if args.file:
        print_file(args.file)


if __name__ == "__main__":
    main()
