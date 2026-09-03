from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    user_query: str
    chat_id: Optional[str] = None
