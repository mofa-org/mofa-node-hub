# quote_retrieval_node

A Dora node for retrieving random inspirational quotes via the Quoterism public API. This node can be integrated into multi-modal pipelines for dynamic quote fetching, enabling both synchronous and as-needed quote retrieval for downstream processing or UI presentation.

## Features
- Fetches random quotes from the Quoterism API
- Robust error handling and output signaling API status
- Easy integration with other Dora nodes using standard input/output topics

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: quote_retriever
    build: pip install -e .  # or path to this node
    path: quote_retrieval_node
    inputs:
      user_input: input/user_input  # dummy, triggers quote retrieval
    outputs:
      - quote_output
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
  # Your trigger/input node
  - id: user_trigger
    build: pip install your-trigger-node
    path: user-trigger-node
    outputs:
      - user_input
  # Quote Retrieval Node
  - id: quote_retriever
    build: pip install -e .
    path: quote_retrieval_node
    inputs:
      user_input: user_trigger/user_input
    outputs:
      - quote_output
```

Your point source must output:

* Topic: `user_input`
* Data: Can be any dummy value (string or trigger event)
* Metadata:

  ```json
  {
    "description": "Any string/int, just to trigger quote retrieval."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type         | Description                          |
| ------------| ------------| --------------------------------------|
| user_input  | any         | Dummy param to trigger quote retrieval |

### Output Topics

| Topic         | Type   | Description                                         |
| ------------- | ------ | -------------------------------------------------- |
| quote_output  | dict   | Dict with API response or error (with status field) |


## License

Released under the MIT License.
