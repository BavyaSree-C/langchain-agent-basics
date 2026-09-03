from client.openrouter_client import openrouter_client
from config.settings import settings


def invoke_claude(prompt) -> str:
    # Accept either a plain string or a pre-built message list
    if isinstance(prompt, str):
        messages = [{"role": "user", "content": prompt}]
    else:
        messages = prompt

    response = openrouter_client.post(
        f"{settings.OPENROUTER_BASE_URL}/chat/completions",
        json={
            "model": settings.OPENROUTER_MODEL,
            "messages": messages,
        },
    )

    data = response.json()

    if not response.ok:
        raise RuntimeError(
            f"OpenRouter API error "
            f"({response.status_code}): "
            f"{data}"
        )

    if "choices" not in data:
        raise RuntimeError(
            f"Unexpected OpenRouter response: {data}"
        )

    return data["choices"][0]["message"]["content"]