from pyllm.tokenizer import Tokenizer
from pyllm.model import Model

def main():
    """Main entry point for the PyLLM application."""
    print("\nWelcome to PyLLM: Python Lightweight Language Model!\n")

    # Get user input
    text = input("Enter your text: ").strip()
    if not text:
        print("Error: No input provided. Please try again.")
        return

    try:
        # Initialize tokenizer and model
        tokenizer = Tokenizer("data/vocab.txt")
        model = Model()

        # Tokenize the input text
        tokens = tokenizer.tokenize(text)
        print(f"\nTokens: {tokens}\n")

        # Perform inference
        response = model.infer(tokens)
        print(f"Model Response: {response}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
