# newton_derivative_node

A Dora-rs node for symbolic differentiation using the Newton API. Computes the derivative of $x^2$ via API call and makes result available to downstream nodes.

## Features
- Computes symbolic derivative via HTTP API
- Receives user input parameter for pipeline compatibility
- Robust error handling and output serialization

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
  - id: newton-derivative
    build: pip install -e .
    path: newton_derivative_node
    inputs:
      user_input: input/user_input
    outputs:
      - derivative_output
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
  - id: user-input
    build: pip install your-input-node
    path: your_input_node_path
    outputs:
      - user_input

  - id: newton-derivative
    build: pip install -e .
    path: newton_derivative_node
    inputs:
      user_input: user-input/user_input
    outputs:
      - derivative_output
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary (can be an empty, placeholder, or triggering datum)
* Metadata:

  ```json
  {
    "description": "User input parameter, used as trigger; content ignored."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                |
| ---------- | ------ | ------------------------------------------ |
| user_input | Any    | User parameter, used to trigger derivation |

### Output Topics

| Topic             | Type   | Description                                  |
| ----------------- | ------ | --------------------------------------------- |
| derivative_output | Object | Derivative result or error from Newton API    |


## License

Released under the MIT License.
