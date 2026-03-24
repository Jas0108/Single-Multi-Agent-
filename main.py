from agents.single_agent import SingleAgent

def main():
    tutor = SingleAgent()
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            break
        
        if not user_input:
            continue
        
        response = tutor.chat(user_input)
        print(f"\nTutor: {response}")

if __name__ == "__main__":
    main()
