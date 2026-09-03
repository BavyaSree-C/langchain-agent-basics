import uvicorn
from fastapi import FastAPI
from src.router.chat import chat_router
from src.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI()
app.include_router(chat_router)

# def happy(a):
#     print(a)

if __name__ == "__main__":
    logger.info("Starting server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

    # ak = {
    #       'happy': happy   # dictionary with string key → function value
    #   }

    # s = 'happy'
    # ak[s]('i am looss')