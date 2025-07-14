from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join("docs", filename)
    print(f"Attempting to download file: {file_path}")
    if not os.path.isfile(file_path):
        return {"error": "File not found"}
    return FileResponse(path=file_path, filename=filename, media_type='application/octet-stream')


# uv run uvicorn http_server:app --reload --port 8001