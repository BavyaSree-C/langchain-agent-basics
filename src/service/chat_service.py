from utils.llm_model import invoke_claude
from typing import Optional
from utils.logger import get_logger
import uuid
from service.agent import Agent
from prompts.agent_prompt import AGENT_PROMPT
logger = get_logger(__name__)

agent = Agent(AGENT_PROMPT)

def process_chat(user_query: str,chat_id: Optional[str] = None):

    if chat_id is None:
        chat_id = str(uuid.uuid4())

    agent_response = agent(user_query)
    logger.info(f"user query: {user_query},\n chat id : {chat_id}, \n response: {agent_response}")

    return {
        "status": 200,
        "message": "Success",
        "user_query": user_query,
        "chat_id": chat_id,
        "respose": agent_response
        }
