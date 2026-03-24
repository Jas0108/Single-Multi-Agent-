from llm.ollama_client import OllamaClient
from tools.calculator import calculate
from memory.memory import ConversationMemory
import re

class SingleAgent:
    def __init__(self):
        self.client = OllamaClient()
        self.memory = ConversationMemory()
        
        # Load tutor prompt
        with open('prompts/tutor_prompt.txt', 'r') as f:
            self.tutor_prompt = f.read()
    
    def calculate_if_needed(self, text):
        """Find and evaluate math expressions"""
        pattern = r'calculate:\s*([0-9+\-*/().^ ]+)'
        matches = re.findall(pattern, text, re.IGNORECASE)
        
        for expr in matches:
            result = calculate(expr.strip())
            text = text.replace(f"calculate: {expr}", str(result))
        
        return text
    
    def chat(self, user_input):
        # Add user message to memory
        self.memory.add_message("Student", user_input)
        
        # Create prompt with history
        prompt = self.tutor_prompt.format(
            history=self.memory.get_conversation_history(),
            input=user_input
        )
        
        # Get response
        response = self.client.invoke(prompt)
        
        # Check if calculation is needed
        if "calculate:" in response.lower():
            response = self.calculate_if_needed(response)
        
        # Add response to memory
        self.memory.add_message("Tutor", response)
        
        return response
