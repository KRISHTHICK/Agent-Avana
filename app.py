from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn, os, shutil, uuid, datetime

app = FastAPI()
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount a directory to serve static files like uploaded documents.
app.mount('/static', StaticFiles(directory=STATIC_DIR), name='static')

# The main route to serve your index.html file.
# This assumes that index.html is located in the same directory as this Python file.
@app.get('/', response_class=HTMLResponse)
async def homepage():
    file_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="index.html not found", status_code=404)

# NOTE: The following routes are commented out because gptindex.html and geindex.html
# were not provided and would cause a server error.
# @app.get("/gpt", response_class=HTMLResponse)
# async def serve_gpt():
#     file_path = os.path.join(BASE_DIR, "gptindex.html")
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             return HTMLResponse(content=f.read())
#     return HTMLResponse(content="GPT page not found", status_code=404)

# @app.get("/ge", response_class=HTMLResponse)
# async def serve_ge():
#     file_path = os.path.join(BASE_DIR, "geindex.html")
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             return HTMLResponse(content=f.read())
#     return HTMLResponse(content="GE page not found", status_code=404)

# This endpoint handles file uploads from the frontend.
# It saves the file to a 'static' directory and returns a mock JSON response.
@app.post('/api/upload')
async def upload(file: UploadFile = File(...)):
    # Save file temporarily with a unique ID to prevent filename collisions
    uid = str(uuid.uuid4())[:8]
    filename = f"{uid}_{file.filename}"
    save_path = os.path.join(STATIC_DIR, filename)
    
    with open(save_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)
        
    # Mock processing response
    unique_id = f"091VA880-{str(uuid.uuid4().int)[:6]}"
    response = {
        "status": "ok",
        "title": file.filename,
        "unique_id": unique_id,
        "uploaded_at": datetime.datetime.utcnow().isoformat()+"Z"
    }
    return JSONResponse(response)

# This endpoint handles chat requests from the frontend's chatbot UI.
# It provides a mock reply based on the user's question.
@app.post('/api/chat')
async def chat(payload: dict):
    q = payload.get('q','')
    # Mock reply - in production, this is where you would call an AI model
    reply = f"I understood your question: '{q}'. (This is a demo reply. Integrate Gemini for production.)"
    return JSONResponse({"reply": reply})

# This is the entry point for running the application.
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
