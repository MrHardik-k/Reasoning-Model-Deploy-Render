from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from groq import Groq

router = APIRouter()
GROQ_API_KEY="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"

client = Groq(api_key=GROQ_API_KEY)

# Define the request model
class ChatRequest(BaseModel):
    message: str

@router.post("/predicts")
async def chat_with_groq(request: ChatRequest):
    try:
        # Send the message to Groq API
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": request.message}],
            model="llama-3.3-70b-versatile",  # Choose the appropriate model
        )
        # Extract and return the response content
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
