# eve_universe_node

EVE Online Universe Node for Mofa Agents

## Features
- Retrieves EVE Online universe structures from ESI API
- Fetches current market prices for all items
- Lists available regions in the game world

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
  - id: eve_universe
    build: pip install -e eve_universe_node
    path: eve_universe_node
    inputs:
      user_input: input/user_input  # placeholder for parameter compliance
    outputs:
      - structures
      - market_prices
      - regions
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
  - id: something_else
    build: pip install my-custom-node
    path: my_custom_dir
    outputs:
      - user_input

  - id: eve_universe
    build: pip install -e eve_universe_node
    path: eve_universe_node
    inputs:
      user_input: something_else/user_input
    outputs:
      - structures
      - market_prices
      - regions
```

Your point source must output:

* Topic: `user_input`
* Data: any (can be placeholder, will be ignored)
* Metadata:

  ```json
  {
    "description": "Placeholder parameter, ignored by eve_universe_node",
    "required": false
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                         |
| ------------| ------ | --------------------------------------------------- |
| user_input  | any    | Placeholder parameter; not used by node logic.      |

### Output Topics

| Topic          | Type                | Description                                           |
| -------------- | ------------------- | ----------------------------------------------------- |
| structures     | list/dict (JSON)    | List of structure IDs/info from EVE Online universe   |
| market_prices  | list (JSON)         | Current market prices of all items                    |
| regions        | list/dict (JSON)    | List of available regions with their metadata         |


## License

Released under the MIT License.
