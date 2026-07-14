"""
kanazawa_tourism.py

Example MCP server built on the StackChan-Dify MCP Bridge.
Forwards StackChan's voice queries to a Dify agent grounded in
the Kanazawa Tourism Association's official tourism knowledge base.

Used in the Hackster.io project:
"Samurai StackChan: Tourism Guide for Kanazawa" (M5Stack Global
Innovation Contest 2026).
"""

from fastmcp import FastMCP
import sys
import os
import logging
import httpx
from dotenv import load_dotenv

# stdout is reserved for the MCP stdio protocol, so logs must go to stderr only
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(asctime)s [%(name)s] %(message)s")
logger = logging.getLogger('KanazawaTourism')

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

DIFY_API_BASE = os.environ.get("DIFY_API_BASE", "https://api.dify.ai/v1")
DIFY_API_KEY = os.environ.get("DIFY_API_KEY")

# Create an MCP server
mcp = FastMCP("KanazawaTourism")

@mcp.tool()
def get_kanazawa_tourism_info(question: str) -> dict:
    """Dedicated tool for answering questions about Kanazawa tourism, Maeda
    Toshiie, and Kanazawa's history and culture. For questions about
    Kanazawa Castle, Kenrokuen Garden, Maeda Toshiie, Higashi Chaya
    District, etc., always call this tool and use its answer as-is rather
    than answering from web search or your own knowledge. Do not use this
    tool for questions unrelated to Kanazawa."""
    if not DIFY_API_KEY:
        logger.error("DIFY_API_KEY is not set")
        return {"success": False, "answer": "The tourism guide system is not configured yet."}

    try:
        response = httpx.post(
            f"{DIFY_API_BASE}/chat-messages",
            headers={"Authorization": f"Bearer {DIFY_API_KEY}"},
            json={
                "inputs": {},
                "query": question,
                "response_mode": "blocking",
                "conversation_id": "",
                "user": "stackchan-kanazawa",
            },
            timeout=15.0,
        )
        response.raise_for_status()
        answer = response.json()["answer"]
        logger.info(f"question: {question} -> answer: {answer}")
        return {"success": True, "answer": answer}
    except Exception as e:
        logger.error(f"Dify request failed: {e}")
        return {
            "success": False,
            "answer": "Sorry, I couldn't retrieve tourism information right now. Please try asking again.",
        }

# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
