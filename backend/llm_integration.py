import asyncio

async def get_llm_response(context: list) -> str:
    """
    Simulates an asynchronous call to an LLM API.
    Replace this with an actual API call (e.g., OpenAI, Anthropic) and apply prompt engineering as needed.
    """
    await asyncio.sleep(1)
    last_message = context[-1]['message']
    return f"LLM response to: {last_message}"
