import os
import time

from dotenv import load_dotenv
from typing import List, Optional
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, Request, UploadFile, Form


app = FastAPI()

# Load environment variables from .env
load_dotenv()

# Get the Tesseract path from env variable
apikey = os.getenv("API_KEY")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware to add processing time to response headers.
    This decorator registers a middleware function for HTTP requests in FastAPI.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.post("/api_example")
async def extract_info_from_file(
    file: UploadFile = File(...),  # required file upload
    page_number: int = Form(1),  # default to the first page
    keys_list: Optional[List[str]] = Form(
        None
    ),  # optional list of keys to extract, if not provided, defaults will be used
):
    filename = file.filename.lower()
    contents = await file.read()
    a = True
    b = True
    # Determine input file type
    if a:
        try:
            pass
        except Exception as e:
            return JSONResponse(
                status_code=400, content={"error": f"TIF processing failed: {str(e)}"}
            )

    elif b:
        try:
            pass
        except Exception as e:
            return JSONResponse(
                status_code=400, content={"error": f"PDF processing failed: {str(e)}"}
            )

    else:
        return JSONResponse(
            status_code=400,
            content={"error": "Unsupported file format. Only TIF and PDF allowed."},
        )

    return JSONResponse(content={"message": "File processed successfully."})
