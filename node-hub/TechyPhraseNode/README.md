# techy_phrase_node

A Dora node that fetches a random techy phrase using the Techy API. Useful for demos, testing message propagation, or injecting random phrases into a Dora pipeline.

## Features
- Fetches real-time random techy phrases from the Techy API
- Simple integration as a Dora-compatible node (MofaAgent)
- Graceful error handling with structured error output

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
  - id: techy_phrase_node
    build: pip install -e .
    path: techy_phrase_node
    inputs:
      user_input: input/user_input
    outputs:
      - techy_phrase
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
  - id: your_node
    build: pip install -e your_node
    path: your_node
    outputs:
      - user_input
  - id: techy_phrase_node
    build: pip install -e .
    path: techy_phrase_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - techy_phrase
```

Your point source must output:

* Topic: `user_input`
* Data: string or any value (not used, but must be set for compatibility)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Any trigger value, not used by techy_phrase_node"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                           |
| ----------- | ------ | ------------------------------------- |
| user_input  | string | Optional trigger input (any value OK) |

### Output Topics

| Topic        | Type           | Description                                |
| ------------ | --------------| -------------------------------------------|
| techy_phrase | dict or string | Random techy phrase, or error if occurred  |

## License

Released under the MIT License.
