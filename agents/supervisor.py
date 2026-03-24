from llm.ollama_client import OllamaClient

class SupervisorAgent:
    def __init__(self):
        self.client = OllamaClient()
        
        # Load supervisor prompt
        with open('prompts/supervisor_prompt.txt', 'r') as f:
            self.supervisor_prompt = f.read()
    
    def classify(self, user_input):
        prompt = self.supervisor_prompt.format(input=user_input)
        raw_response = self.client.invoke(prompt)
        
        # Clean and normalize response
        cleaned_response = raw_response.strip().lower()
        
        # Strict classification - only exact matches
        if cleaned_response == "math":
            selected_agent = "math"
        elif cleaned_response == "physics":
            selected_agent = "physics"
        elif cleaned_response == "chemistry":
            selected_agent = "chemistry"
        else:
            # Fallback for invalid responses
            selected_agent = "math"
        
        print(f"Node selected: {selected_agent}")
        print(f"Routing to {selected_agent} agent")
        
        return selected_agent
