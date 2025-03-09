import asyncio
from llm_integration import get_llm_response

class ChatService:
    def __init__(self):
        self.conversation_history = {}

    async def process_message(self, user_id: str, message: str) -> str:
        context = self.conversation_history.get(user_id, [])
        context.append({"role": "user", "message": message})
        
        response = await get_llm_response(context)
        
        context.append({"role": "assistant", "message": response})
        self.conversation_history[user_id] = context
        return response
