from llm.ollama_client import OllamaClient
from tools.calculator import calculate
import re

class PhysicsAgent:
    def __init__(self):
        self.client = OllamaClient()
        
        # Load physics prompt
        with open('prompts/physics_prompt.txt', 'r') as f:
            self.physics_prompt = f.read()
    
    def calculate_if_needed(self, text):
        """Find and evaluate math expressions"""
        pattern = r'calculate:\s*([0-9+\-*/().^ ]+)'
        matches = re.findall(pattern, text, re.IGNORECASE)
        
        for expr in matches:
            result = calculate(expr.strip())
            text = text.replace(f"calculate: {expr}", str(result))
        
        return text
    
    def respond(self, user_input):
        prompt = self.physics_prompt.format(input=user_input)
        response = self.client.invoke(prompt)
        
        # Check if calculation is needed
        if "calculate:" in response.lower():
            response = self.calculate_if_needed(response)
        
        return response
