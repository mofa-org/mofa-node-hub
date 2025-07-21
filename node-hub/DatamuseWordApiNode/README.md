# datamuse_word_node

Simple Dora-rs node for querying the Datamuse word API. This node demonstrates how to chain external API requests and aggregate their responses for downstream pipeline usage.

## Features
- Queries multiple Datamuse API endpoints for semantic and phonetic word associations
- Aggregates results into a structured output for chaining and composition
- Minimal configuration—runs all sample endpoints by default

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
  - id: datamuse_node
    build: pip install -e .
    path: datamuse_word_node
    inputs:
      user_input: input/user_input
    outputs:
      - datamuse_outputs
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
  - id: my_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input
  - id: datamuse_node
    build: pip install -e .
    path: datamuse_word_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - datamuse_outputs
  - id: my_result_consumer
    build: pip install my-result-consumer
    path: my-result-consumer
    inputs:
      datamuse_outputs: datamuse_node/datamuse_outputs
```

Your point source must output:

* Topic: `user_input`
* Data: (any data; not used by this node, but needed for chaining)
* Metadata:

  ```json
  {
    "description": "User input placeholder; not evaluated."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | any    | Placeholder input for chaining/composability  |

### Output Topics

| Topic            | Type   | Description                                                       |
| ---------------- | ------ | ----------------------------------------------------------------- |
| datamuse_outputs | dict   | Aggregated API results keyed by description or error info          |

## License

Released under the MIT License.
