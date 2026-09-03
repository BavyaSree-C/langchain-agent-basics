from fastapi import APIRouter
from models.chat_model import ChatRequest
from service.chat_service import process_chat
from utils.logger import get_logger

logger = get_logger(__name__)

chat_router = APIRouter()

@chat_router.post("/chat")
def chat(request: ChatRequest):
    try:
        if request.user_query and request.user_query.strip():
            return process_chat(request.user_query, request.chat_id)
        else:
            raise ValueError("User query should not be empty")

    except ValueError as e:
        logger.warning(f"Invalid query: {e}")
        return {"status": 400, "message": str(e)}

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {"status": 500, "message": "Oops, an unexpected error occurred"}
