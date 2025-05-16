from langgraph.graph import StateGraph, START, END
from typing import List, Dict
from typing_extensions import TypedDict
from AppConfig.AppConfigHelper import get_config, get_prompt
import requests
from UtilModules.gpt4o_client import client
import copy


api_key = get_config("API_KEY")
api_url = get_config("API_URL")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


class AnalystState(TypedDict):
    memory: List[str]
    msg: str


def summarizer(state):
    msg = state.get("msg")
    memory = state.get("memory", [])
    if not memory:
        memory = []
    prompt = copy.deepcopy(get_prompt("analyst_sum_prompt"))
    prompt[1]["content"] = prompt[1]["content"].format(user_msg=msg, memory=memory)

    # call gpt4o model
    response = client.chat.completions.create(
            model='gpt-4o',
            messages=prompt).choices[0].message.content
    memory.extend([{"User": msg}, {"Agent": response}])
    return {"msg": response, "memory": memory}


# Graph setup
def analyst_agent():
    builder = StateGraph(AnalystState)
    builder.add_node("node", summarizer)

    builder.add_edge(START, "node")
    builder.add_edge("node", END)
    graph = builder.compile()
    # display(Image(graph.get_graph().draw_mermaid_png()))
    return graph
