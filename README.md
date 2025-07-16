# Web_Scrapin

This project includes a small Python script for scraping a webpage and downloading files linked on that page. It can also display the contents of a local file.

## Requirements

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Usage

### Scrape a webpage

```bash
python scraper.py --url https://example.com --output data
```

This command saves the HTML of the page to `data/page.html` and downloads any linked files (PDF, images, spreadsheets, etc.) into the same directory.

### Display a local file

```bash
python scraper.py --file path/to/file.txt
```

This simply prints the file contents to the terminal.
