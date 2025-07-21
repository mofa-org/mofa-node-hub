# got_quote_node

Get random Game of Thrones quotes as a Dora-rs node.

## Features
- Retrieves random quotes from the Game of Thrones Quotes API
- Robust error handling with clear error messages
- Easy integration into Dora pipelines

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
  - id: got_quote_node
    build: pip install -e .
    path: got_quote_node
    inputs:
      user_input: input/user_input  # Dummy input, triggers quote fetching
    outputs:
      - got_quote
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
  - id: point_source
    build: pip install your-node
    path: your-node
    outputs:
      - user_input
  - id: got_quote_node
    build: pip install -e .
    path: got_quote_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - got_quote
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (e.g. string, integer, or dummy/pulse)
* Metadata:

  ```json
  {
    "description": "Dummy input that triggers Game of Thrones quote fetch"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| user_input  | Any    | Dummy parameter to trigger API request  |

### Output Topics

| Topic      | Type   | Description                            |
| ---------- | ------ | -------------------------------------- |
| got_quote  | JSON   | Random Game of Thrones quote or error  |


## License

Released under the MIT License.
