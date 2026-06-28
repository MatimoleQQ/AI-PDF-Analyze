from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.services.rag_service import save_document, ask_question
from backend.services.pdf_service import extract_text_from_pdf

from backend.routes import upload, ask

app = FastAPI()

# -----------------------------
# CORS (REACT FRONTEND FIX)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, tags=["Upload"])
app.include_router(ask.router, tags=["Ask"])

@app.get("/")
def root():
    return {"status": "ok", "message": "AI Document Assistant running"}


