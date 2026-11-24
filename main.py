from collections.abc import Sequence

from mistralai import agents
from mistralai.client import Mistral
from mistralai.client import models as api_models

INSTRUCTIONS = """You are NEXUS, a work assistant for Tommy Wijaya (Tomm), a 22-year-old crypto hunter, airdrop hunter, and trader from Indonesia. Help with research, coding, data analysis, and writing. Be direct, concise, and evidence-based. Use web search to verify current facts before stating them. When you write code, make it complete and runnable. When you analyze data, show your working. Respond in Indonesian when the user writes in Indonesian, otherwise in English. Never invent facts, prices, or dates. If you are unsure, say so."""


def _text_of(content: "str | Sequence[object]") -> str:
    if isinstance(content, str):
        return content
    return "".join(
        chunk.text for chunk in content if isinstance(chunk, api_models.TextChunk)
    )


@agents.tool
async def web_search(query: str) -> str:
    """Search the web for current, verifiable information. Returns the answer text with its sources. Use this to verify facts, prices, and dates before stating them."""
    client = Mistral()
    response = await client.beta.conversations.start_async(
        model="mistral-medium-3-5",
        inputs=query,
        tools=[{"type": "web_search"}],
        store=False,
    )
    replies = [
        entry for entry in response.outputs if isinstance(entry, api_models.MessageOutputEntry)
    ]
    return _text_of(replies[-1].content)


agent = agents.Agent(
    model="mistral-medium-3-5",
    name="nexus",
    description="NEXUS work agent for Tommy Wijaya: research, coding, data analysis, and writing.",
    instructions=INSTRUCTIONS,
    tools=[web_search],
    environment=agents.MistralSandbox(),
)
