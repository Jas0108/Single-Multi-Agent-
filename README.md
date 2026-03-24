# AI STEM Tutor

A clean, minimal AI-powered tutor using Ollama with both single-agent and multi-agent architectures.

## Setup

### 1. Activate virtual environment
```bash
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Pull model
```bash
ollama pull mistral
```

### 4. Run single agent
```bash
python main.py
```

### 5. Run multi-agent
```bash
python main_multi.py
```

## Project Structure

```
ai-tutor/
├── main.py                     # Single agent CLI
├── main_multi.py               # Multi-agent CLI
├── requirements.txt            # Dependencies
├── README.md                   # This file
│
├── llm/
│   └── ollama_client.py        # Ollama LLM connection
│
├── agents/
│   ├── single_agent.py         # Single tutor agent
│   ├── supervisor.py           # Question classifier
│   ├── math_agent.py           # Math specialist
│   ├── physics_agent.py        # Physics specialist
│   └── chemistry_agent.py      # Chemistry specialist
│
├── tools/
│   └── calculator.py           # Safe math calculator
│
├── memory/
│   └── memory.py               # Conversation memory
│
├── graph/
│   └── multi_agent_graph.py    # LangGraph workflow
│
├── state/
│   └── state.py                # State management
│
└── prompts/
    ├── tutor_prompt.txt        # General tutor prompt
    ├── supervisor_prompt.txt   # Supervisor classifier
    ├── math_prompt.txt         # Math specialist prompt
    ├── physics_prompt.txt      # Physics specialist prompt
    └── chemistry_prompt.txt    # Chemistry specialist prompt
```

## Features

### Phase 1: Single Agent
- General STEM tutoring
- Calculator tool integration
- Conversation memory
- Step-by-step explanations

### Phase 2: Multi-Agent System
- Supervisor agent for question classification
- Specialized agents for Math, Physics, Chemistry
- LangGraph workflow orchestration
- Subject-specific expertise

## Multi-Agent Workflow

The multi-agent system uses LangGraph to create an intelligent routing system:

```
┌─────────┐    ┌─────────────┐    ┌──────────────────────┐
│  START  │───▶│  SUPERVISOR │───▶│   ROUTING DECISION   │
└─────────┘    └─────────────┘    └──────────────────────┘
                                     │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
            ┌───────▼──────┐  ┌──────▼──────┐  ┌───────▼───────┐
            │  MATH AGENT  │  │PHYSICS AG. │  │CHEMISTRY AG. │
            └───────┬──────┘  └──────┬──────┘  └───────┬───────┘
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      │
                               ┌──────▼──────┐
                               │    END      │
                               └─────────────┘
```

###  Workflow Steps:

1. **START** → User input enters the system
2. **SUPERVISOR** → Analyzes and classifies the query:
   - "What is 2+2?" → classifies as "math"
   - "Explain gravity" → classifies as "physics"  
   - "Balance H₂ + O₂" → classifies as "chemistry"
3. **ROUTING DECISION** → Directs to appropriate specialist agent
4. **SPECIALIZED AGENT** → Provides subject-specific response
5. **END** → Returns final answer to user

### Agent Responsibilities:

- **Supervisor**: Query classification only (no answering)
- **Math Agent**: Algebra, calculus, statistics, step-by-step solutions
- **Physics Agent**: Mechanics, thermodynamics, formulas, numerical problems
- **Chemistry Agent**: Reactions, equations, concepts, stoichiometry

## Usage

1. Start the application with either `main.py` or `main_multi.py`
2. Type your STEM questions
3. Get detailed, step-by-step responses
4. Type 'exit' to quit

## Example Questions

**Math:**
- "Solve 2x + 5 = 15"
- "What is the derivative of x²?"

**Physics:**
- "Explain Newton's second law"
- "Calculate the force needed to accelerate a 10kg object at 5m/s²"

**Chemistry:**
- "Balance the equation: H₂ + O₂ → H₂O"
- "What is photosynthesis?"

## Tech Stack

- Python
- LangChain
- LangGraph
- Ollama (mistral model)
- AST for safe math evaluation
