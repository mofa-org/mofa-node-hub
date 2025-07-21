# league_dragon_node

Fetches the full public League of Legends champion dataset from Riot’s Data Dragon API for use in Dora/Mofa pipelines as a data node.

## Features
- Retrieves champion metadata live from Riot’s Data Dragon API
- Exposes output as a Dora/Mofa node, callable programmatically
- Graceful error handling with error info in output

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
  - id: league_dragon
    build: pip install -e .
    path: league_dragon_node
    outputs:
      - league_champion_data
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
  - id: data_source
    build: pip install -e .
    path: league_dragon_node
    outputs:
      - league_champion_data
  - id: consumer
    build: pip install your-consumer-node
    path: your-consumer-node
    inputs:
      league_champion_data: data_source/league_champion_data
```

Your point source must output:

* Topic: `league_champion_data`
* Data: Champion metadata (JSON as dict) or error message
* Metadata:

  ```json
  {
    "type": "dict",
    "description": "Champion metadata or error info as returned from Riot API."
  }
  ```

## API Reference

### Input Topics

| Topic     | Type    | Description                       |
| --------- | ------- | --------------------------------- |
| user_input| any     | Placeholder for triggering requests|

### Output Topics

| Topic               | Type     | Description                               |
| ------------------- | -------- | ----------------------------------------- |
| league_champion_data| dict     | Riot champion metadata or error info dict |


## License

Released under the MIT License.
