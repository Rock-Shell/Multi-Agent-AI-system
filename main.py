from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import time
from Agents.Agent import agent

app = FastAPI()
graph = agent()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str
    metadata: Dict[str, str]


@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    start_time = time.time()

    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    # logic for response
    inputdata = {"msg": request.query}
    messages = graph.invoke(inputdata)
    answer = messages.get("msg", "some error occurred")
    print(messages.keys(), len(messages["memory"]))

    metadata = {
        "model": "gpt-4o",
        "timestamp": str(int(time.time())),
        "response_time": f"{(time.time() - start_time):.3f}s"
    }

    return {"response": answer, "metadata": metadata}
