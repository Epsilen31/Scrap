# Web and File Scraper

This project includes a small Python script for scraping a webpage and downloading files linked on that page. It can also display the contents of a local file. Scraped data is saved in the `scrapped` folder as PDF, JSON and CSV files.

The included API accepts uploads through the Swagger UI and stores the uploaded
file and its extracted text in the same three formats.

## Requirements

Install dependencies with pip:

```bash
python -m pip install -r requirements.txt
```

If `uvicorn` is not found after installation, you can run it via the Python
module command:

```bash
python -m uvicorn api:app --reload
```

## Usage

### Scrape a webpage (CLI)

```bash
python scraper.py --url https://example.com
```

This command saves the HTML of the page to the `scrapped` directory and downloads any linked files (PDF, images, spreadsheets, JSON, etc.) into the same folder. The page text is saved as `page.pdf`, `page.json` and `page.csv`.

### Display a local file (CLI)

```bash
python scraper.py --file path/to/file.txt
```

This prints the file contents to the terminal and stores them in the `scrapped` folder. Use `--output DIR` to specify a different directory if needed.

### Run the API

You can also start a small FastAPI server which exposes endpoints for scraping a URL or uploading a file. Swagger UI documentation is available at `/docs` once the server is running. Uploaded files are saved under `scrapped/`.

```bash
python -m uvicorn api:app --reload
```
