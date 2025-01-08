# Usage Guide

## Running the Program
To start the program run this command
```bash
pyllm
```

## Tokenization
PyLLM tokenizes your input text based on a predefined vocabulary Unknown words are assigned a token of `-1`

## Inference
The model generates a mock response based on the input tokens

Customize the `pyllm/model.py` file to implement your own model logic
