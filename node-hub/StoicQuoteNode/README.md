# stoic_quote_node

Retrieve Stoicism Quotes for Your Dora-rs Pipelines

## Features
- Fetches stoic quotes (quote and author) from a public web API
- Simple Dora-rs node interface with input/output parameter compatibility
- Handles API errors gracefully with informative error outputs

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
  - id: stoic_quote_node
    build: pip install -e .
    path: stoic_quote_node
    inputs:
      user_input: input/user_input  # Input required for Dora compatibility, can be empty
    outputs:
      - stoic_quote
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
    path: my-input-node
    outputs:
      - user_input

  - id: stoic_quote_node
    build: pip install -e .
    path: stoic_quote_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - stoic_quote

  - id: my_output
    build: pip install my-output-node
    path: my-output-node
    inputs:
      stoic_quote: stoic_quote_node/stoic_quote
```

Your point source must output:

* Topic: `user_input`
* Data: Any (e.g., string or null)
* Metadata:

  ```json
  {
    "type": "string",
    "desc": "Placeholder input for Dora compatibility. Accepts any user-provided value or an empty string. Not used by the node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                 |
| ----------|--------|---------------------------------------------|
| user_input | string | Placeholder; not consumed by the node logic |

### Output Topics

| Topic        | Type                 | Description                                           |
| ------------|----------------------|-------------------------------------------------------|
| stoic_quote | {"quote": str, "author": str, "error?": str} | Received quote and author, or error if fetch fails |


## License

Released under the MIT License.
