from fastapi import FastAPI, UploadFile, File
import shutil
import os
from scraper import download_webpage, store_content, SCRAP_DIR

app = FastAPI(title="Web and File Scraper")

@app.post("/scrape/url")
async def scrape_url(url: str):
    html_path, files, text = download_webpage(url, SCRAP_DIR)
    return {"html": html_path, "files": files}

@app.post("/scrape/file")
async def scrape_file(file: UploadFile = File(...)):
    os.makedirs(SCRAP_DIR, exist_ok=True)
    dest_path = os.path.join(SCRAP_DIR, file.filename)
    with open(dest_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    with open(dest_path, "r", encoding="utf-8", errors="ignore") as f_in:
        content = f_in.read()
    base_name = os.path.splitext(file.filename)[0]
    store_content(content, base_name, SCRAP_DIR)
    return {"file_path": dest_path}
