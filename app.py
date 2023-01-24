from fastapi.responses import HTMLResponse
from fastapi import (
    FastAPI, WebSocket, WebSocketDisconnect,
    Request
)
from typing import List

app = FastAPI()
allData = []

html = "Err"
with open("./index.html","r") as f:
	html = f.read()

@app.get("/")
async def root():
    return HTMLResponse(content = html, status_code = 200)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
				allData.append(data)
        await websocket.send_text(f"Message text was: {data}")

@app.get("/code.js")
async def js():
    return {"message": "Hello World"}
