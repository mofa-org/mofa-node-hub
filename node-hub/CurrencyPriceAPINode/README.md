# currency_price_api_node

A Dora-rs node that provides real-time exchange rates by querying the public https://dolarapi.com API. This node receives requests from other nodes and broadcasts dollar and currency exchange rates as JSON outputs.

## Features
- Real-time retrieval of dollar and other currency prices via public API
- Seamless integration with the Dora agent framework
- Simple input/output API for currency queries

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
  - id: currency_api
    build: pip install -e currency_price_api_node
    path: currency_price_api_node
    inputs:
      user_input: upstream_node/user_input
    outputs:
      - currency_prices
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
    build: pip install my-node
    path: my-point-source
    outputs:
      - user_input

  - id: currency_api
    build: pip install -e currency_price_api_node
    path: currency_price_api_node
    inputs:
      user_input: my_point_source/user_input
    outputs:
      - currency_prices
```

Your point source must output:

* Topic: `user_input`
* Data: (can be any serializable parameter for triggering the query)
* Metadata:

  ```json
  {
    "description": "Parameter forwarded to trigger currency fetching. May be unused."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                                   |
| ---------- | --------- | --------------------------------------------- |
| user_input | any       | Trigger for currency price update (arbitrary) |

### Output Topics

| Topic            | Type   | Description                              |
| ---------------- | ------ | ---------------------------------------- |
| currency_prices  | JSON   | Exchange rates or error message (JSON)   |


## License

Released under the MIT License.
