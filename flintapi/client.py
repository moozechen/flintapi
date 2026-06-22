"""FlintAPI Client — lightweight OpenAI-compatible wrapper."""
import os
from typing import Optional, Iterator

try:
    from openai import OpenAI
except ImportError:
    raise ImportError(
        "openai package required. Install with: pip install openai"
    )

BASE_URL = "https://flintapi.ai/v1"
DEFAULT_MODEL = "flint-smart"


class Flint:
    """FlintAPI client — thin wrapper around OpenAI SDK.

    Example:
        flint = Flint(api_key="tk-...")
        reply = flint.chat("Explain AI in one sentence")
        print(reply)

        # Streaming
        for chunk in flint.chat_stream("Tell me a story"):
            print(chunk, end="")
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = BASE_URL,
        default_model: str = DEFAULT_MODEL,
    ):
        self.api_key = api_key or os.environ.get("FLINTAPI_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "API key required. Set FLINTAPI_API_KEY env var "
                "or pass api_key=tk-... to Flint().\n"
                "Get your key at https://flintapi.ai/dashboard"
            )
        self.default_model = default_model
        self._client = OpenAI(
            base_url=base_url,
            api_key=self.api_key,
        )

    def chat(
        self,
        prompt: str,
        model: Optional[str] = None,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> str:
        """Send a chat message and return the response text.

        Args:
            prompt: User message
            model: Model ID (default: flint-smart)
            system: Optional system prompt
            temperature: 0-2, higher = more creative
            max_tokens: Max response length

        Returns:
            Response text string
        """
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self._client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content or ""

    def chat_stream(
        self,
        prompt: str,
        model: Optional[str] = None,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> Iterator[str]:
        """Stream a chat response token by token.

        Yields:
            Text chunks as they arrive
        """
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        stream = self._client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content


# Convenience functions
def chat(prompt: str, api_key: Optional[str] = None, **kwargs) -> str:
    """One-shot chat. Uses FLINTAPI_API_KEY env var if api_key not provided."""
    return Flint(api_key=api_key).chat(prompt, **kwargs)


def stream_chat(prompt: str, api_key: Optional[str] = None, **kwargs) -> Iterator[str]:
    """One-shot streaming chat."""
    return Flint(api_key=api_key).chat_stream(prompt, **kwargs)
