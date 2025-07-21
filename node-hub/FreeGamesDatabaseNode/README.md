# FreeGamesDatabaseNode

Query free-to-play PC games from the Free-To-Play Games Database API and deliver the results to downstream Dora nodes. Wraps the public API in a Dora-compatible node for seamless dataflow integration.

## Features
- Retrieves a JSON list of current free-to-play PC games
- Simple Dora node interface with one input and one output
- Handles API request errors robustly, reporting issues in the output

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
  - id: free_games_db
    build: pip install -e .
    path: free_games_database  # directory or Python module location
    inputs:
      user_input: input/user_input
    outputs:
      - games_list
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
  - id: my_custom_source
    build: pip install my-input-node  # your node
    path: my-input-node-dir  # location
    outputs:
      - user_input

  - id: free_games_db
    build: pip install -e .
    path: free_games_database
    inputs:
      user_input: my_custom_source/user_input
    outputs:
      - games_list

  - id: my_consumer
    build: pip install my-consumer
    path: my-consumer-dir
    inputs:
      games_list: free_games_db/games_list
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable object (not used, can be None)
* Metadata:

  ```json
  {
    "description": "Any trigger for the games API query (not used by agent)",
    "required": false
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                    |
|-------------|--------|--------------------------------|
| user_input  | Any    | Triggers games list retrieval   |

### Output Topics

| Topic      | Type               | Description                                                |
|------------|--------------------|------------------------------------------------------------|
| games_list | List[dict] or dict | List of games as returned from the API, or error info dict |


## License

Released under the MIT License.
