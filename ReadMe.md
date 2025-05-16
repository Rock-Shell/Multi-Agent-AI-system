**Multi Agent AI System**

This project covers an Agentic approach to perform question answering, content summarization task. Used 
langgraph to create graph like structure, where each individual agent is a node, connected via edges. The
workflow can be understook easily from Agent_structure.png

![alt text](https://github.com/Rock-Shell/Multi-Agent-AI-system/blob/main/Agent_structure.png)

Agents - Common location for all sub-agents
    - plannerAgent - routes to responder/analyst agent
    
    - responderAgent - responds to simple queries
    
    - analystAgent - perform summarization task
    
    - memoryAgent - Keeps short term memory. Last 3 messages are recorded
    
    - Agent - Connects all sub-agents

AppConfig - 

    - config.yaml - model config
    
    - promptConfig.yaml - prompts used in agents and sub-agents

utilModules - 
    - Modules used commonly by sub-agents

main.py - Agent inference bound inside FastAPI /ask endpoint

chatbot_ui.py - Simple streamlit code to interact with the API
