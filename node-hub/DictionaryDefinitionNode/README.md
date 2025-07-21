# dictionary_node

A Dora-rs node that fetches word definitions from the free DictionaryAPI.dev service. This example node demonstrates how to integrate external REST APIs into a Dora/Mofa pipeline, providing stateless responses with robust error handling.

## Features
- Retrieves definitions for the English word 'fart' from DictionaryAPI.dev
- Handles API errors and connectivity issues gracefully
- Design supports easy future extension for arbitrary word lookups

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
  - id: dictionary
    build: pip install -e .
    path: ./dictionary_node
    inputs:
      user_input: input/user_input
    outputs:
      - definition_data
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
  - id: your_input_node
    build: pip install -e .
    path: ./your_input_node
    outputs:
      - user_input

  - id: dictionary
    build: pip install -e .
    path: ./dictionary_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - definition_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or dict payload (currently unused)
* Metadata:

  ```json
  {
    "description": "Placeholder for arbitrary user input (currently unused - future extensibility)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                 |
| ----------- | ------- | ------------------------------------------- |
| user_input  | string  | Placeholder for user input (not yet used)   |

### Output Topics

| Topic           | Type   | Description                                            |
| --------------- | ------ | ------------------------------------------------------|
| definition_data | dict   | DictionaryAPI response JSON or error container         |

## License

Released under the MIT License.
