from langgraph.graph import StateGraph, START, END
from typing import List, Dict
from typing_extensions import TypedDict
from AppConfig.AppConfigHelper import get_config, get_prompt
import requests


api_key = get_config("API_KEY")
api_url = get_config("API_URL")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


class MemoryState(TypedDict):
    memory: List[str]
    msgs: str  # [{"user": "Hello"}, {"Agent": "Hi, how can i help"}}


def memory(state):
    short_memory = state.get("memory")
    short_memory = short_memory[-3:]
    return {"memory": short_memory}


# Graph setup
def memory_agent():
    builder = StateGraph(MemoryState)
    builder.add_node("node", memory)

    builder.add_edge(START, "node")
    builder.add_edge("node", END)
    graph = builder.compile()
    # display(Image(graph.get_graph().draw_mermaid_png()))
    return graph
