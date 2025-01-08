import unittest
from pyllm.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    """Unit tests for the Tokenizer class."""

    def setUp(self):
        """Set up test fixtures."""
        # Initialize tokenizer with a vocab file (make sure the path is correct)
        self.tokenizer = Tokenizer("data/vocab.txt")

    def test_tokenize(self):
        """Test tokenizing a sentence with known words."""
        # Example input text
        text = "hello how are you"
        tokens = self.tokenizer.tokenize(text)

        # Expected token IDs for the words in the text
        expected_tokens = [0, 1, 2, 3]
        self.assertEqual(tokens, expected_tokens)

    def test_unknown_tokens(self):
        """Test tokenizing a sentence with unknown words."""
        # Example input text with unknown words
        text = "unknown words"
        tokens = self.tokenizer.tokenize(text)

        # Expected token IDs for unknown words should be -1 (as per the logic in Tokenizer)
        expected_tokens = [-1, -1]
        self.assertEqual(tokens, expected_tokens)

    def test_empty_text(self):
        """Test tokenizing an empty string."""
        text = ""
        tokens = self.tokenizer.tokenize(text)

        # Expected result for empty string should be an empty list
        self.assertEqual(tokens, [])

if __name__ == "__main__":
    unittest.main()
