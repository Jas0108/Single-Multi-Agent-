from llm.ollama_client import OllamaClient
from tools.calculator import calculate
import re

class MathAgent:
    def __init__(self):
        self.client = OllamaClient()
        
        # Load math prompt
        with open('prompts/math_prompt.txt', 'r') as f:
            self.math_prompt = f.read()
    
    def calculate_if_needed(self, text):
        """Find and evaluate math expressions"""
        pattern = r'calculate:\s*([0-9+\-*/().^ ]+)'
        matches = re.findall(pattern, text, re.IGNORECASE)
        
        for expr in matches:
            result = calculate(expr.strip())
            text = text.replace(f"calculate: {expr}", str(result))
        
        return text
    
    def respond(self, query: str) -> str:
        """Generate math-focused response"""
        prompt = self.math_prompt.format(input=query)
        response = self.client.invoke(prompt)
        
        # Handle calculations
        if "calculate:" in response.lower():
            response = self.calculate_if_needed(response)
        
        return response
