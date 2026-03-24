import ast
import operator
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class CalculatorInput(BaseModel):
    expression: str = Field(description="Mathematical expression to evaluate, e.g., '2 + 3 * 4'")

class Calculator:
    def __init__(self):
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
        }
    
    def evaluate(self, expression):
        try:
            node = ast.parse(expression, mode='eval')
            return self._eval(node.body)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _eval(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            op_type = type(node.op)
            if op_type in self.operators:
                return self.operators[op_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):
            operand = self._eval(node.operand)
            op_type = type(node.op)
            if op_type in self.operators:
                return self.operators[op_type](operand)
            else:
                raise ValueError(f"Unsupported unary operator: {op_type}")
        else:
            raise ValueError(f"Unsupported expression: {type(node)}")

class CalculatorTool(BaseTool):
    """A calculator tool that safely evaluates mathematical expressions using LangChain tool framework."""
    
    name: str = "Calculator"
    description: str = "Useful for mathematical calculations. Input should be a mathematical expression like '2 + 3 * 4' or '(15 * 0.1) * 200'"
    args_schema: Type[BaseModel] = CalculatorInput
    
    def _run(self, expression: str) -> str:
        """Execute the calculation using the safe calculator."""
        try:
            calc = Calculator()
            result = calc.evaluate(expression.strip())
            return str(result)
        except Exception as e:
            return f"Calculation error: {str(e)}"
    
    async def _arun(self, expression: str) -> str:
        """Async version of the calculator."""
        return self._run(expression)

def calculate(expression):
    calc = Calculator()
    return calc.evaluate(expression)

# Factory function to create the LangChain tool
def create_calculator_tool():
    """Create a LangChain calculator tool."""
    return CalculatorTool()
