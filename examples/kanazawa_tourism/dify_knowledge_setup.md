# Dify Knowledge Base Setup — Kanazawa Tourism Example

This example uses [Dify](https://dify.ai) as the backend agent, with the
Kanazawa Tourism Association's official website
([kanazawa-kankoukyoukai.or.jp](https://www.kanazawa-kankoukyoukai.or.jp))
as its knowledge source.

## 1. Create a Dify App

- App type: Chatflow
- Model: Amazon Nova (via Bedrock)
- Flow: `START` → `Knowledge Retrieval` → `LLM` → `Answer`

## 2. Configure the Knowledge Base

- Source: Kanazawa Tourism Association official site
  (kanazawa-kankoukyoukai.or.jp)
- Ingestion method: Dify's built-in "Add URL" feature — pages were
  registered directly by URL, no manual scraping or export step
- Pages included: top-level sections such as `/spot/`, `/gourmet/`,
  `/event/`, `/access/`, `/article/`, `/modelCourse/` (including
  individual model course detail pages), `/favorite/`, `/support/`
- Chunking mode: Parent-child, high quality / hybrid retrieval
- Update frequency: static snapshot taken at ingestion time (not
  auto-refreshing); re-run ingestion manually to update

## 3. Connecting to Dify

`kanazawa_tourism.py` is implemented as a proper MCP server using
`fastmcp` (`FastMCP`, `@mcp.tool()`, `transport="stdio"`). It exposes a
single tool, `get_kanazawa_tourism_info`, which forwards the user's
question directly to this Dify Chatflow's standard Chat API
(`POST /chat-messages`) and returns the `answer` field from the response.
Errors (missing API key, request failure) are caught and returned as a
graceful fallback message rather than raising, so a Dify outage doesn't
crash the MCP server.

The Chatflow's LLM prompt instructs it to answer in the same language as
the user's question, so the same endpoint serves both Japanese- and
English-speaking visitors without any language switching logic on the
`kanazawa_tourism.py` side.

## 4. Authentication

Generate an API key from the Dify app's **API Access** page and set it in
`.env` (see `../../.env.example`). Never commit real API keys.
