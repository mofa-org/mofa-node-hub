# multi_account_fraud_node

A Dora-compatible Python node for querying external fraud detection APIs via HTTP GET requests. This node provides a convenient way for other nodes to trigger fraud detection checks with optional user-defined parameters, returning JSON or plain text results.

## Features
- Simple integration with external (REST HTTP GET) fraud detection or analysis APIs
- Accepts dynamic input parameters for flexible query construction
- Outputs JSON or raw text response to downstream Dora nodes

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
  - id: fraud_checker
    build: pip install -e .
    path: multi_account_fraud_node
    inputs:
      user_input: input/user_input
    outputs:
      - fraud_detection_result
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
  - id: custom_input
    build: pip install -e custom_node
    path: custom_node
    outputs:
      - user_input

  - id: fraud_checker
    build: pip install -e .
    path: multi_account_fraud_node
    inputs:
      user_input: custom_input/user_input
    outputs:
      - fraud_detection_result
```

Your point source must output:

* Topic: `user_input`
* Data: String (may be empty, or a query string, e.g. `user_id=123`)
* Metadata:

  ```json
  {
    "description": "(optional) HTTP query string appended to baseline endpoint URL"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                        |
| ------------|--------|----------------------------------------------------|
| user_input  | str    | Optional query string to append as HTTP GET params. |

### Output Topics

| Topic                   | Type                        | Description                                   |
|-------------------------|-----------------------------|-----------------------------------------------|
| fraud_detection_result  | dict / str / list / error   | JSON or text response from the remote API.    |


## License

Released under the MIT License.
