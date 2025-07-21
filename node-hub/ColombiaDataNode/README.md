# colombia_node

A Dora-rs/Mofa agent node that aggregates live data on Colombia's presidents and top tourist attractions via the [API Colombia](https://api-colombia.com/). It makes external API calls, packages the results, and outputs structured data for integration in distributed dataflows.

## Features
- Fetches current and historical Colombian president data from public API
- Retrieves a live list of Colombian tourist attractions
- Robust error handling to ensure pipeline stability

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
  - id: colombia_node
    build: pip install -e .
    path: colombia_node
    inputs:
      user_input: input/user_input
    outputs:
      - colombia_data
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
  - id: my_input
    build: pip install my-input-node
    path: my_input
    outputs:
      - user_input
  - id: colombia_node
    build: pip install -e .
    path: colombia_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - colombia_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (typically string or JSON-serializable)
* Metadata:

  ```json
  {
    "type": "string or object",
    "required": false,
    "description": "Can be any pipeline input to trigger Colombia node run."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                              |
| ----------- | ------ | ---------------------------------------- |
| user_input  | Any    | Generic trigger or input for data fetch. |

### Output Topics

| Topic         | Type   | Description                                                    |
| ------------- | ------ | -------------------------------------------------------------- |
| colombia_data | dict   | Dictionary with president and tourist attraction data or errors |


## License

Released under the MIT License.
