import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from backend.services.pdf_service import extract_text_from_pdf
from backend.services.rag_service import save_document

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_pdf(
        file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)

    chunks = save_document(text)

    return {
        "message": "PDF uploaded",
        "chunks": chunks
    }