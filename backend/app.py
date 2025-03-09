from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from chat import ChatService
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_service = ChatService()

@app.post("/chat")
async def chat_endpoint(user_id: str, message: str):
    """
    Receives a chat message, processes it, and returns the LLM response.
    """
    try:
        response = await chat_service.process_message(user_id, message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
