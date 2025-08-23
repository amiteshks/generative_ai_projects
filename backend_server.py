# This is my Backend code
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Chat API", version="1.0")

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse, tags=["chat"])
def chat(req: ChatRequest):
    # TODO: Replace with real LLM call
    return ChatResponse(reply=f"You said: {req.prompt}")
