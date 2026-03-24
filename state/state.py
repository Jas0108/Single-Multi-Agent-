from typing import TypedDict, Annotated, List, Dict, Optional
from langgraph.graph.message import add_messages

class TutorState(TypedDict):
    user_input: str
    selected_agent: Optional[str]
    response: str
    messages: Annotated[List, add_messages]
    conversation_history: List[Dict[str, str]]
