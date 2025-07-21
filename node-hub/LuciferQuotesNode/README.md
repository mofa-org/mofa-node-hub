# lucifer_quotes_node

A Dora-rs node that outputs random quotes from Lucifer using the https://lucifer-quotes.vercel.app API. Designed for integration into workflows where nodes may trigger motivational or fun quotes via message calls.

## Features
- Fetches random quotes from the Lucifer Quote API
- Outputs serializable quote data and handles errors gracefully
- Can be triggered on-demand by other nodes or messages

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
  - id: lucifer-quote
    build: pip install -e .
    path: lucifer_quotes_node
    inputs:
      user_input: input/user_input
    outputs:
      - lucifer_quote
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
  - id: your-custom-node
    build: pip install -e .
    path: your_custom_node
    outputs:
      - user_input
  - id: lucifer-quote
    build: pip install -e .
    path: lucifer_quotes_node
    inputs:
      user_input: your-custom-node/user_input
    outputs:
      - lucifer_quote
```

Your point source must output:

* Topic: `user_input`
* Data: Any (typically a trigger value or message)
* Metadata:

  ```json
  {
    "description": "Trigger for requesting a Lucifer quote (can be any value)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                       |
| ----------- | ------ | ----------------------------------------------------------------- |
| user_input  | Any    | Message/trigger to request a Lucifer quote                        |

### Output Topics

| Topic         | Type                | Description                                                 |
| ------------- | ------------------- | ----------------------------------------------------------- |
| lucifer_quote | dict or list (JSON) | Lucifer quote (fields: quote, author, series, or error info) |


## License

Released under the MIT License.
