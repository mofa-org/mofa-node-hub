# random_rejection_node

A Dora node for generating random rejection reasons by querying an external API endpoint (naas.isalman.dev/no). Useful for adding humorous or randomized decision-making responses in Dora workflows.

## Features
- Fetches a random rejection reason from an external service
- Simple drop-in node for demos or fun applications
- Robust error handling with detailed messages

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
  - id: random_rejection_node
    build: pip install -e .
    path: random_rejection_node
    inputs:
      user_input: input/user_input  # dummy input for compatibility
    outputs:
      - random_rejection_reason
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
    path: my_input_node
    outputs:
      - user_input

  - id: random_rejection_node
    build: pip install -e .
    path: random_rejection_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - random_rejection_reason
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy value, e.g., string or dict)
* Metadata:

  ```json
  {
    "type": "string or dict (ignored)",
    "description": "Dummy parameter to trigger the node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                              |
| ----------- | ------- | -------------------------------------------------------- |
| user_input  | Any     | Dummy parameter required to trigger the node execution   |

### Output Topics

| Topic                  | Type         | Description                                                |
| ---------------------- | ------------ | ---------------------------------------------------------- |
| random_rejection_reason| String/Dict  | Random rejection reason or structured error message         |


## License

Released under the MIT License.
