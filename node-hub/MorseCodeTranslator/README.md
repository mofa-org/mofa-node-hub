# morse_code_translator

Morse code translation as a Dora-rs/Mofa agent node using FunTranslations API.

## Features
- Translates input text to Morse code using a public API
- Gracefully handles empty or missing text input (defaults to "hello world")
- Outputs both successful translations and any API errors

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: morse_translator
    build: pip install -e .
    path: morse_code_translator
    inputs:
      text: input/text
    outputs:
      - morse_code_translation
```

Run the demo:

```bash
dora build demo.yml
dora start demo.yml
```


## Integration with Other Nodes

To connect with your existing node:

```yaml
nodes:
  # Your text input source node
  - id: text_source
    build: pip install your-node
    path: your-node-path
    outputs:
      - text

  - id: morse_translator
    build: pip install -e .
    path: morse_code_translator
    inputs:
      text: text_source/text
    outputs:
      - morse_code_translation
```

Your point source must output:

* Topic: `text`
* Data: String (the text to be translated)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Text to convert to Morse code."
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                      |
|-------|--------|----------------------------------|
| text  | string | Text to be translated to Morse.   |

### Output Topics

| Topic                  | Type   | Description                                                    |
|------------------------|--------|----------------------------------------------------------------|
| morse_code_translation | object | Morse translation API response or error (JSON-serializable)    |


## License

Released under the MIT License.
