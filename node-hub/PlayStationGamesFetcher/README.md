# playstation_games_fetcher

Fetches the newest PlayStation games available in Switzerland from the official PlayStation Store API. Designed as a Dora-rs node with MofaAgent integration for chaining and flexible parameter input.

## Features
- Fetches latest PlayStation games (up to 20, sorted by release date) for the Switzerland PlayStation Store
- Outputs data as JSON for easy integration with downstream nodes
- Gracefully handles API errors with JSON output

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
  - id: ps_game_fetcher
    build: pip install -e playstation_games_fetcher
    path: playstation_games_fetcher
    inputs:
      user_input: input/user_input   # (Optional) provide a parameter if chaining is needed
    outputs:
      - ps_games_data
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
  - id: upstream_node
    build: pip install your-node
    path: your-node
    outputs:
      - user_input           # Topic to pass downstream (optional)

  - id: ps_game_fetcher
    build: pip install -e playstation_games_fetcher
    path: playstation_games_fetcher
    inputs:
      user_input: upstream_node/user_input   # Chained parameter if necessary
    outputs:
      - ps_games_data
```

Your point source must output:

* Topic: `user_input`
* Data: User input or any serializable dictionary/string if chaining is required
* Metadata:

  ```json
  {
    "type": "string or object",
    "description": "Optional user input passed for chaining; not used in this node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                          |
| ---------- | ------ | ------------------------------------ |
| user_input | object | Optional parameter, passed downstream |

### Output Topics

| Topic           | Type  | Description                                      |
| --------------- | ----- | ------------------------------------------------ |
| ps_games_data   | dict  | JSON response from PlayStation Store API (or error) |


## License

Released under the MIT License.
