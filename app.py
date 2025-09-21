from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn, os, shutil, uuid, datetime

app = FastAPI()
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static if needed
app.mount('/static', StaticFiles(directory=STATIC_DIR), name='static')

@app.get("/gpt", response_class=HTMLResponse)
async def serve_gpt():
    file_path = os.path.join(BASE_DIR, "gptindex.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="GPT page not found", status_code=404)

@app.get("/ge", response_class=HTMLResponse)
async def serve_ge():
    file_path = os.path.join(BASE_DIR, "geindex.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="GE page not found", status_code=404)


# @app.get('/gpt', response_class=HTMLResponse)
# async def gpt_page():
#     with open(os.path.join(BASE_DIR, 'gptindex.html'), 'r', encoding='utf-8') as f:
#         return HTMLResponse(content=f.read())

# @app.get('/ge', response_class=HTMLResponse)
# async def ge_page():
#     with open(os.path.join(BASE_DIR, 'Geindex.html'), 'r', encoding='utf-8') as f:
#         return HTMLResponse(content=f.read())

@app.get('/', response_class=HTMLResponse)
async def homepage():
    with open(os.path.join(BASE_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        return HTMLResponse(content=f.read())

@app.post('/api/upload')
async def upload(file: UploadFile = File(...)):
    # Save file temporarily
    uid = str(uuid.uuid4())[:8]
    filename = f"{uid}_{file.filename}"
    save_path = os.path.join(STATIC_DIR, filename)
    with open(save_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    # Mock processing: in real app call Document AI, classifiers, translations, etc.
    unique_id = f"091VA880-{str(uuid.uuid4().int)[:6]}"
    response = {
        "status": "ok",
        "title": file.filename,
        "unique_id": unique_id,
        "uploaded_at": datetime.datetime.utcnow().isoformat()+"Z"
    }
    return JSONResponse(response)

@app.post('/api/chat')
async def chat(payload: dict):
    q = payload.get('q','')
    # Mock reply - in prod call Gemini or Vertex AI
    reply = f"I understood your question: '{q}'. (This is a demo reply. Integrate Gemini for production.)"
    return JSONResponse({"reply": reply})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
