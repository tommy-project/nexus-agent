# NEXUS

Managed Agent for Tommy Wijaya (Tomm): research, coding, data analysis, and writing.

- Model: `mistral-medium-3-5`
- Built-in web search: `web_search` tool wrapping the hosted `web_search` tool (Conversations API)
- Code interpreter: `environment=agents.MistralSandbox()` (Python/shell in a Mistral-hosted container)
- No external connectors (no GitHub, Gmail, Drive, Notion)

## Run locally

```bash
uv run --env-file .env agents chat
```

## Deploy (Mistral-managed)

Push this repository to GitHub, then deploy it as a managed deployment in Mistral Studio
(`deploy_workflow_deployment` with this repo's URL and pushed commit). The agent registers
under the name `nexus`.
