import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "meta-llama/llama-3.1-8b-instruct",
    )

    OPENROUTER_BASE_URL = (
        "https://openrouter.ai/api/v1"
    )


settings = Settings()