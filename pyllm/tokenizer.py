class Tokenizer:
    """A simple tokenizer that converts text into tokens based on a vocabulary file."""

    def __init__(self, vocab_path):
        """
        Initialize the tokenizer and load the vocabulary from a specified file.
        
        Args:
            vocab_path (str): Path to the vocabulary file.
        """
        self.vocab = {}
        self.load_vocab(vocab_path)

    def load_vocab(self, vocab_path):
        """Load vocabulary from a file and store it in a dictionary."""
        try:
            with open(vocab_path, "r") as file:
                for index, word in enumerate(file):
                    self.vocab[word.strip()] = index
            print(f"Vocabulary loaded from {vocab_path}")
        except FileNotFoundError:
            print(f"Error: Vocabulary file '{vocab_path}' not found.")
        except Exception as e:
            print(f"Error loading vocabulary: {e}")

    def tokenize(self, text):
        """
        Tokenize a given text by splitting it into words and mapping each word to its token ID.
        
        Args:
            text (str): The input text to tokenize.
        
        Returns:
            list: A list of token IDs corresponding to the words in the text.
        """
        tokens = []
        for word in text.split():
            token_id = self.vocab.get(word, -1)  # Use -1 for unknown words
            tokens.append(token_id)
        
        # Optionally, print the tokenized output for debugging
        print(f"Tokenized text: {tokens}")
        return tokens
