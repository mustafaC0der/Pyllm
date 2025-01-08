
# PyLLM Usage Guide

## Running the Model

To run the model, use the following command:

```bash
pyllm
```

This will start the language model and allow you to interact with it through the command line.

## Example Usage

```python
from pyllm import Model

# Initialize the model
model = Model()

# Use the model for text generation
text = model.generate("Write a short story about a robot")
print(text)
```

This will generate a short story using the PyLLM model.

## Customizing the Model

You can adjust various parameters for the model to fine-tune its behavior:

- `temperature`: Controls the randomness of the output (higher values lead to more creative output).
- `max_tokens`: Limits the number of tokens in the generated text.

Example:

```python
output = model.generate("Write a poem about space", temperature=0.7, max_tokens=100)
```

## Command-Line Interface

You can interact with the model directly through the CLI:

```bash
pyllm generate "Write a poem about nature" --temperature 0.5 --max-tokens 150
```

Refer to `pyllm --help` for more command-line options.
