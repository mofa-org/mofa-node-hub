# dragonball_node

A Dora-rs node for aggregating Dragon Ball universe data, specifically planets and character information, from the `dragonball-api`. This node fetches and outputs structured universe data suitable for downstream ML pipelines or interactive applications.

## Features
- Fetches comprehensive planet information from the Dragon Ball API
- Fetches a list of all Dragon Ball characters
- Error handling and status reporting for API requests

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
  - id: dragonball_universe
    build: pip install -e .
    path: dragonball_node
    inputs:
      user_input: input/user_input
    outputs:
      - planets_output
      - characters_output
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
  - id: my_input_node
    # Define your input node that sends 'user_input' or triggers
    ...
    outputs:
      - user_input
  - id: dragonball_universe
    build: pip install -e .
    path: dragonball_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - planets_output
      - characters_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any user input to trigger the API calls (can be dummy)
* Metadata:

  ```json
  {
    "description": "Any value to trigger universe data fetch. Typically a string or None."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                |
| ---------- | ------ | ------------------------------------------ |
| user_input | any    | User input signal to trigger data fetching |

### Output Topics

| Topic            | Type   | Description                                                    |
| ---------------- | ------ | -------------------------------------------------------------- |
| planets_output   | dict   | List of planets JSON object from Dragon Ball API                |
| characters_output| dict   | List of characters JSON object from Dragon Ball API             |


## License

Released under the MIT License.
