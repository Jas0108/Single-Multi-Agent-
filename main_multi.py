from graph.multi_agent_graph import MultiAgentGraph

def main():
    graph = MultiAgentGraph()
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        if not user_input:
            continue
        
        response = graph.run(user_input)
        print(f"\nTutor: {response}")

if __name__ == "__main__":
    main()
