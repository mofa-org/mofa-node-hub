# pony_character_node

A Dora-rs node for fetching and streaming character data from the public Pony API (https://ponyapi.net). The node queries the remote service and outputs a complete listing of pony characters, ready to be consumed or integrated with other Dora graph nodes.

## Features
- Retrieves all character data from the Pony API in real time
- Robust error handling, gracefully reports HTTP and JSON decoding issues
- Seamless integration into Dora/Mofa agent graphs via documented topics

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
  - id: pony_character_fetcher
    build: pip install -e pony_character_node
    path: pony_character_node
    inputs:
      user_input: input/user_input   # Optional parameter for compatibility
    outputs:
      - pony_characters
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
  - id: your_custom_node
    build: pip install -e your_custom_node
    path: your_custom_node
    outputs:
      - user_input

  - id: pony_character_fetcher
    build: pip install -e pony_character_node
    path: pony_character_node
    inputs:
      user_input: your_custom_node/user_input
    outputs:
      - pony_characters
```

Your point source must output:

* Topic: `user_input`
* Data: Any (kept for compatibility; can be null or a stub value)
* Metadata:

  ```json
  {
    "description": "User input or placeholder (not used by node, but required for input topic structure)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| user_input | Any    | Placeholder input for compatibility. Unused. |

### Output Topics

| Topic           | Type           | Description                                                     |
| --------------- | -------------- | --------------------------------------------------------------- |
| pony_characters | dict or list   | Complete data fetched from the Pony API or error report object. |


## License

Released under the MIT License.
