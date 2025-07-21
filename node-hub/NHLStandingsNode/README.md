# nhl_standings_node

Real-time NHL Standings Fetching Node for Dora-rs

## Features
- Fetches current NHL season standings from the official NHL public API
- Graceful error handling with JSON-serializable outputs
- Dora-compatible API: receive parameter and send output for robust integration

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
  - id: nhl_standings
    build: pip install -e ./nhl_standings_node
    path: nhl_standings_node
    inputs:
      user_input: input/user_input  # Facilitator input for dataflow
    outputs:
      - nhl_standings
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
  - id: user_trigger
    build: pip install -e ./user_trigger_node
    path: user_trigger_node
    outputs:
      - user_input

  - id: nhl_standings
    build: pip install -e ./nhl_standings_node
    path: nhl_standings_node
    inputs:
      user_input: user_trigger/user_input
    outputs:
      - nhl_standings
```

Your point source must output:

* Topic: `user_input`
* Data: Any (facilitator input, can be empty or a dummy value)
* Metadata:

  ```json
  {
    "description": "Trigger or context for fetching NHL standings"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                              |
| ----------- | ------- | ---------------------------------------- |
| user_input  | Any     | Facilitator input; triggers a new fetch  |

### Output Topics

| Topic          | Type          | Description                                         |
| -------------- | ------------- | --------------------------------------------------- |
| nhl_standings  | dict/string | NHL standings JSON from api-web.nhle.com, or error  |


## License

Released under the MIT License.
