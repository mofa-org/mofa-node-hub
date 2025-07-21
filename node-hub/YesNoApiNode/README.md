# yesno_api_node

A minimal Dora-rs compatible node that returns a random yes/no (with sometimes "maybe") answer using the public [https://yesno.wtf/api](https://yesno.wtf/api). Includes error handling and pipeline-friendly parameter usage.

## Features
- Fetches yes/no/maybe answers from an internet API
- Receives input parameter for pipeline compatibility
- Outputs responses or error status in a structured format

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
  - id: yesno
    build: pip install -e yesno_api_node
    path: yesno_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - yesno_result
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
  - id: your_input_source
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input

  - id: yesno
    build: pip install -e yesno_api_node
    path: yesno_api_node
    inputs:
      user_input: your_input_source/user_input
    outputs:
      - yesno_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (dummy parameter to trigger a response)
* Metadata:

  ```json
  {
    "dtype": "any",
    "usage": "dummy or pipeline parameter"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type | Description                             |
| ----------- | ---- | --------------------------------------- |
| user_input  | any  | Dummy parameter to trigger API response |

### Output Topics

| Topic         | Type   | Description                       |
| ------------- | ------ | --------------------------------- |
| yesno_result  | object | {"answer": "yes"\|"no"\|"maybe"} or {"error": "..."} |

## License

Released under the MIT License.
