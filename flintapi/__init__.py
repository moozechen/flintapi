"""FlintAPI — One API key for 25+ Chinese LLMs.

Usage:
    from flintapi import Flint
    
    flint = Flint(api_key="your-key")
    reply = flint.chat("Hello!")
    print(reply)

Install:
    pip install flintapi
"""

from .client import Flint, chat, stream_chat

__version__ = "0.1.0"
__all__ = ["Flint", "chat", "stream_chat"]
