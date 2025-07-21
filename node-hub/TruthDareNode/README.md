# truth_dare_node

Fetch random Truth and Dare prompts as a Dora node.

## Features
- Fetches a random "Truth" prompt from a public API
- Fetches a random "Dare" prompt from a public API
- Exposes a simple interface for integration in modular Dora/Mofa workflows

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
  - id: truth_dare
    build: pip install -e .
    path: truth_dare_node
    inputs:
      user_input: input/user_input
    outputs:
      - truth_dare_result
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
  - id: input_source
    build: pip install your-input-node  # Replace with your input node
    path: your-input-node
    outputs:
      - user_input

  - id: truth_dare
    build: pip install -e .
    path: truth_dare_node
    inputs:
      user_input: input_source/user_input
    outputs:
      - truth_dare_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any user input payload; not strictly required, used for triggering
* Metadata:

  ```json
  {
    "description": "Arbitrary user input for triggering the Truth/Dare node. Can be any data."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| user_input  | any    | Optional input to trigger the node run. |

### Output Topics

| Topic              | Type   | Description                           |
| ------------------ | ------ | ------------------------------------- |
| truth_dare_result  | dict   | Dictionary with `truth` and `dare` keys. |

## License

Released under the MIT License.
