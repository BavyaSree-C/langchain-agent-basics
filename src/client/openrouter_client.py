import requests

from config.settings import settings


def create_openrouter_client() -> requests.Session:

    if not settings.OPENROUTER_API_KEY:
        raise ValueError(
            "OPENROUTER_API_KEY is not configured"
        )

    client = requests.Session()

    client.headers.update({
        "Authorization": (
            f"Bearer {settings.OPENROUTER_API_KEY}"
        ),
        "Content-Type": "application/json",
    })

    return client


openrouter_client = create_openrouter_client()
