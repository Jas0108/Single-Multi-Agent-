from langchain_ollama import OllamaLLM

class OllamaClient:
    def __init__(self, model_name="mistral"):
        self.model_name = model_name
        self.base_url = "http://localhost:11434"
        # Use only LangChain wrapper
        self.llm = OllamaLLM(model=model_name, base_url=self.base_url)
    
    def get_llm(self):
        return self.llm
    
    def invoke(self, prompt):
        try:
            # Use LangChain wrapper with optimized settings
            return self.llm.invoke(prompt)
        except Exception as e:
            return f"Error: Unable to get response from Ollama. {str(e)}"
