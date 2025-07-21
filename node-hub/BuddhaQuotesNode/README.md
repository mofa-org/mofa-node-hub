# buddha_quotes_node

Fetch random Buddha quotes and expose them via Dora node API.

## Features
- Obtain random Buddha quotes using Buddha API
- Provides simple node interface for integration in Dora pipelines
- Includes robust error handling with clear messages

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
  - id: buddha_quote_node
    build: pip install -e .
    path: buddha_quotes_node
    inputs:
      user_input: input/user_input  # Optional, used for node triggering
    outputs:
      - buddha_quote
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
  - id: another_node
    build: pip install -e your_node
    path: your_node
    outputs:
      - user_input
  - id: buddha_quote_node
    build: pip install -e .
    path: buddha_quotes_node
    inputs:
      user_input: another_node/user_input
    outputs:
      - buddha_quote
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (typically a string, placeholder to trigger the node)
* Metadata:

  ```json
  {
    "trigger": "any"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| user_input  | Any    | Placeholder input to trigger quote fetching. |

### Output Topics

| Topic         | Type     | Description                        |
| ------------- | -------- | ---------------------------------- |
| buddha_quote  | dict/str | Random Buddha quote or error info. |


## License

Released under the MIT License.
