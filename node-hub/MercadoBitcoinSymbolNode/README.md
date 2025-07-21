# mercado_bitcoin_symbols

Real-time Mercado Bitcoin symbol fetcher Dora-rs node

## Features
- Fetches the full list of trading symbols from Mercado Bitcoin's public API
- Exposes API data via Dora node output for downstream consumption
- Simple upstream integration via a placeholder parameter

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
  - id: mercado_bitcoin_symbols
    build: pip install -e .
    path: mercado_bitcoin_symbols
    inputs:
      user_input: input/user_input  # Placeholder for demonstration
    outputs:
      - symbols
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
    outputs:
      - user_input
  - id: mercado_bitcoin_symbols
    build: pip install -e .
    path: mercado_bitcoin_symbols
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - symbols
```

Your point source must output:

* Topic: `user_input`
* Data: Any valid JSON-serializable object (used as placeholder)
* Metadata:

  ```json
  {
    "description": "Placeholder input, ignored by the symbol fetcher"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| user_input | object  | Placeholder input; required for pipeline    |

### Output Topics

| Topic   | Type           | Description                                       |
| ------- | -------------- | ------------------------------------------------- |
| symbols | dict or object | JSON response from Mercado Bitcoin symbols API    |


## License

Released under the MIT License.
