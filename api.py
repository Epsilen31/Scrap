from fastapi import FastAPI, UploadFile, File
import os
import aiofiles
from scraper import download_webpage, store_content, SCRAP_DIR

app = FastAPI(title="Web and File Scraper")

@app.post("/scrape/url")
async def scrape_url(url: str):
    html_path, files, text = download_webpage(url, SCRAP_DIR)
    return {"html": html_path, "files": files}

@app.post("/scrape/file")
async def scrape_file(file: UploadFile = File(...)):
    os.makedirs(SCRAP_DIR, exist_ok=True)
    filename = os.path.basename(file.filename)
    dest_path = os.path.join(SCRAP_DIR, filename)
    async with aiofiles.open(dest_path, "wb") as f:
        while chunk := await file.read(1024):
            await f.write(chunk)
    async with aiofiles.open(dest_path, "r", encoding="utf-8", errors="ignore") as f_in:
        content = await f_in.read()
    base_name = os.path.splitext(filename)[0]
    store_content(content, base_name, SCRAP_DIR)
    return {"file_path": dest_path}
