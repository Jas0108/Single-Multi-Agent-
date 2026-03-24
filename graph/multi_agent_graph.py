from langgraph.graph import StateGraph, END, START
from state.state import TutorState
from agents.supervisor import SupervisorAgent
from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent
from agents.chemistry_agent import ChemistryAgent

class MultiAgentGraph:
    def __init__(self):
        self.supervisor = SupervisorAgent()
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
        self.chemistry_agent = ChemistryAgent()
        
        self.graph = self._build_graph()
    
    def _build_graph(self):
        workflow = StateGraph(TutorState)
        
        # Add nodes
        workflow.add_node("supervisor", self._supervisor_node)
        workflow.add_node("math_agent", self._math_node)
        workflow.add_node("physics_agent", self._physics_node)
        workflow.add_node("chemistry_agent", self._chemistry_node)
        
        # Add edges
        workflow.add_edge(START, "supervisor")
        
        workflow.add_conditional_edges(
            "supervisor",
            self._route_to_agent,
            {
                "math": "math_agent",
                "physics": "physics_agent",
                "chemistry": "chemistry_agent"
            }
        )
        
        workflow.add_edge("math_agent", END)
        workflow.add_edge("physics_agent", END)
        workflow.add_edge("chemistry_agent", END)
        
        return workflow.compile()
    
    def _supervisor_node(self, state: TutorState):
        selected_agent = self.supervisor.classify(state["user_input"])
        state["selected_agent"] = selected_agent
        return state
    
    def _math_node(self, state: TutorState):
        print(f"Executing Math Agent")
        response = self.math_agent.respond(state["user_input"])
        state["response"] = response
        return state
    
    def _physics_node(self, state: TutorState):
        print(f"Executing Physics Agent")
        response = self.physics_agent.respond(state["user_input"])
        state["response"] = response
        return state
    
    def _chemistry_node(self, state: TutorState):
        print(f"Executing Chemistry Agent")
        response = self.chemistry_agent.respond(state["user_input"])
        state["response"] = response
        return state
    
    def _route_to_agent(self, state: TutorState):
        return state["selected_agent"]
    
    def run(self, user_input):
        initial_state = TutorState(
            user_input=user_input,
            selected_agent=None,
            response="",
            messages=[],
            conversation_history=[]
        )
        
        result = self.graph.invoke(initial_state)
        return result["response"]
