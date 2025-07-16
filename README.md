# Web_Scrapin

This project includes a small Python script for scraping a webpage and downloading files linked on that page. It can also display the contents of a local file. Scraped data is saved in the `scrapped` folder as PDF, JSON and CSV files.

## Requirements

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Usage

### Scrape a webpage (CLI)

```bash
python scraper.py --url https://example.com --output data
```

This command saves the HTML of the page to `data/page.html` and downloads any linked files (PDF, images, spreadsheets, JSON, etc.) into the same directory. The text content of the page is also stored in the `scrapped` folder as `page.pdf`, `page.json` and `page.csv`.

### Display a local file (CLI)

```bash
python scraper.py --file path/to/file.txt
```

This prints the file contents to the terminal and stores them in the `scrapped` folder.

### Run the API

You can also start a small FastAPI server which exposes endpoints for uploading a URL or a file. Swagger UI documentation is available at `/docs` once the server is running.

```bash
uvicorn api:app --reload
```
