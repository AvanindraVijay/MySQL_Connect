from agent import ask_ai

def main():
    print("🤖 Internship AI Chatbot (Type 'exit' to quit)")
    print("-" * 50)

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break

            if not user_input:
                print("⚠️ Please type something...")
                continue

            response = ask_ai(user_input)
            print("AI:", response)

        except Exception as e:
            print("❌ Error:", str(e))
            print("🔁 Try again or ask using format like: show details of PMIS2025001")

if __name__ == "__main__":
    main()