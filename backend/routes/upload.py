from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter
from io import BytesIO

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # 1. READ FILE
        content = await file.read()

        if not content:
            raise HTTPException(status_code=400, detail="Empty file")

        # 2. FIX: convert bytes → file-like object
        file_stream = BytesIO(content)

        # 3. DEBUG
        print("filename:", file.filename)
        print("size:", len(content))


        return {
            "status": "ok",
            "filename": file.filename,
            "size": len(content)
        }

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))