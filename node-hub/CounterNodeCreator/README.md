# counter_node

Simple Dora node for counting API demo with programmable create/get interface

## Features
- Integrates with letscountapi.com for demonstration counter operations
- Exposes `create` and `get` operations via Dora parameters
- Returns status and content from the counter API in structured output

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
  - id: counter_node
    build: pip install -e .
    path: counter_node
    inputs:
      user_input: input/user_input
      operation: input/operation
      payload: input/payload
    outputs:
      - counter_api_result
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
  - id: my_point_source
    build: pip install my-custom-node
    path: my-custom-node
    outputs:
      - operation
      - payload

  - id: counter_node
    build: pip install -e .
    path: counter_node
    inputs:
      operation: my_point_source/operation
      payload: my_point_source/payload
    outputs:
      - counter_api_result
```

Your point source must output:

* Topic: `operation` and `payload`
* Data: `operation` is a string ("create" or "get"), `payload` is a JSON object (as string)
* Metadata:

  ```json
  {
    "operation": "string, either 'create' or 'get'",
    "payload": "JSON object (as string, optional for 'get')"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                   |
| ------------|--------|-----------------------------------------------|
| user_input  | string | User input (for compatibility, usually unused) |
| operation   | string | API operation: "create" or "get"              |
| payload     | string | JSON string payload (for "create" operation)   |

### Output Topics

| Topic               | Type   | Description                                         |
|---------------------|--------|-----------------------------------------------------|
| counter_api_result  | dict   | Contains 'status_code', 'content', or 'error'       |


## License

Released under the MIT License.
