# Dify Knowledge Base Setup — Kanazawa Tourism Example

This example uses [Dify](https://dify.ai) as the backend agent, with Kanazawa City's official tourism website as its knowledge source.

## 1. Create a Dify App

- App type: Agent / Chatflow (specify which you used)
- Model: (specify LLM used)

## 2. Configure the Knowledge Base

- Source: Kanazawa official tourism site (add URL)
- Ingestion method: (e.g. web scraping / manual PDF export / sitemap crawl — describe your actual method)
- Chunk size / overlap: (fill in your settings)
- Update frequency: (e.g. static snapshot at time of submission, or periodic refresh)

## 3. Expose as MCP Server

- Endpoint: (describe how the Dify app is exposed as an MCP-compatible endpoint)
- Authentication: reference `../../.env.example`, never commit real keys

## 4. Connect from `kanazawa_tourism.py`

Briefly describe how this example's MCP server script queries the Dify agent and returns responses to StackChan via `mcp_pipe.py`.
