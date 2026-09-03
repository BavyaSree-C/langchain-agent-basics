from anthropic import Anthropic

from config.settings import settings


def create_anthropic_client() -> Anthropic:

    if not settings.ANTHROPIC_API_KEY:
        raise ValueError(
            "ANTHROPIC_API_KEY is not configured"
        )

    if not settings.ANTHROPIC_WORKSPACE_ID:
        raise ValueError(
            "ANTHROPIC_WORKSPACE_ID is not configured"
        )

    return Anthropic(
        api_key=settings.ANTHROPIC_API_KEY,
        default_headers={
            "anthropic-workspace-id": settings.ANTHROPIC_WORKSPACE_ID
        }
    )


claude_client = create_anthropic_client()