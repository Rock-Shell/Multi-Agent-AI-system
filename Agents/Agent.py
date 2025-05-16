from typing import List, Dict, Literal
from typing_extensions import TypedDict
from PIL import Image
import io
from langgraph.graph import StateGraph, START, END

from AppConfig.AppConfigHelper import get_config, get_prompt
from Agents.plannerAgent import planner_agent, planner
from Agents.responderAgent import responder_agent
from Agents.analystAgent import analyst_agent
from Agents.memoryAgent import memory_agent
import requests


class AnalystState(TypedDict):
    memory: List[str]
    planner_decision: Literal["analyze", "respond"]
    msg: str


# Graph setup
def agent():
    builder = StateGraph(AnalystState)
    builder.add_node("planner_agent", planner)
    builder.add_node("responder_agent", responder_agent())
    builder.add_node("analyst_agent", analyst_agent())
    builder.add_node("memory_agent", memory_agent())

    builder.set_entry_point("planner_agent")
    builder.add_conditional_edges("planner_agent", lambda state: state["planner_decision"], {"responder_agent": "responder_agent", "analyst_agent": "analyst_agent"})
    builder.add_edge("responder_agent", "memory_agent")
    builder.add_edge("analyst_agent", "memory_agent")
    builder.add_edge("memory_agent", END)
    graph = builder.compile()
    # Image.open(io.BytesIO(graph.get_graph().draw_mermaid_png(max_retries=2, retry_delay=2.0))).save("Agent_structure.png")
    return graph
