# sports_data_node

Node for accessing and querying sports statistics and metadata from TheSportsDB public API.

## Features
- Unified access to multiple sports information endpoints (events, teams, leagues, players)
- Dynamic input parameterization for flexible querying (supports country, league, player names, etc.)
- Error forwarding and human-readable error reporting for invalid queries

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
  - id: sports_data
    build: pip install -e ./sports_data_node
    path: sports_data_node.py
    inputs:
      operation: input/operation
      user_input: input/user_input
      params_json: input/params_json
    outputs:
      - event_data
      - league_list
      - player_data
      - teams_info
      - countries
      - error
    env:
      THESPORTSDB_API_KEY: "your_thesportsdb_api_key_here"
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
  - id: custom_query
    build: pip install -e ./custom_query_node
    path: custom_query_node.py
    outputs:
      - operation
      - user_input
      - params_json
  - id: sports_data
    build: pip install -e ./sports_data_node
    path: sports_data_node.py
    inputs:
      operation: custom_query/operation
      user_input: custom_query/user_input
      params_json: custom_query/params_json
    outputs:
      - event_data
      - league_list
      - player_data
      - teams_info
      - countries
      - error
```

Your point source must output:

* Topic: `operation`, `user_input`, `params_json`
* Data: operation (string, e.g. "search_event"), user_input (string for chaining), params_json (string, JSON-serialized dictionary)
* Metadata:

  ```json
  {
    "operation": "search_event",
    "user_input": "Find Barcelona FC matches",
    "params_json": "{\"e\": \"Barcelona FC\", \"s\": \"Soccer\"}"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                          |
| ------------| ------ | ------------------------------------ |
| operation   | str    | API operation (see below for options) |
| user_input  | str    | Raw user query for chaining/pipelining |
| params_json | str    | JSON string with operation parameters |

### Output Topics

| Topic        | Type   | Description                             |
| ------------| ------ | ----------------------------------------|
| event_data  | dict   | Events or match info (varies by op)     |
| league_list | dict   | List of all leagues                     |
| player_data | dict   | Info/data for searched player(s)         |
| teams_info  | dict   | Info/data for searched team(s)           |
| countries   | dict   | List of all countries                    |
| error       | dict   | Error details if operation/params failed |

## License

Released under the MIT License.
