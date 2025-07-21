# ron_swanson_quote_node

Get a random Ron Swanson quote from an online API as a Dora-rs node.

## Features
- Fetches a random Ron Swanson quote from the public [ron-swanson-quotes API](https://ron-swanson-quotes.herokuapp.com/v2/quotes)
- Outputs the quote wrapped as JSON in the topic `ron_swanson_quote`
- Handles API errors gracefully and outputs error information

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
  - id: ron_swanson_quote_node
    build: pip install -e .
    path: ron_swanson_quote_node
    inputs:
      user_input: input/user_input
    outputs:
      - ron_swanson_quote
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
  - id: your_input_node
    build: pip install -e your_input_node
    path: your_input_node
    outputs:
      - user_input
  - id: ron_swanson_quote_node
    build: pip install -e .
    path: ron_swanson_quote_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - ron_swanson_quote
```

Your point source must output:

* Topic: `user_input`
* Data: Any dummy input (string, not used but needed to trigger fetch)
* Metadata:

  ```json
  {"type": "string"}
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description        |
| ----------- | ------ | ------------------|
| user_input  | string | Dummy input (any value to trigger fetching the quote) |

### Output Topics

| Topic              | Type   | Description                |
| ------------------ | ------ | --------------------------|
| ron_swanson_quote  | JSON   | Random Ron Swanson quote or error message |


## License

Released under the MIT License.
