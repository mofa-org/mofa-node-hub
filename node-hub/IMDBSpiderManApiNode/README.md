# imdb_spiderman_api

Query Spider-Man info from IMDB API as a Dora-rs node

## Features
- Queries a public IMDB API for Spider-Man movie information
- Fast, stateless operation (no persistent state)
- Standard Dora-rs API compatibility for easy integration

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
  - id: imdb_spiderman_api
    build: pip install -e .
    path: imdb_spiderman_api
    inputs:
      user_input: input/user_input
    outputs:
      - imdb_spiderman_api_response
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
  - id: input_node
    build: pip install your-node
    path: your-input-node
    outputs:
      - user_input

  - id: imdb_spiderman_api
    build: pip install -e .
    path: imdb_spiderman_api
    inputs:
      user_input: input_node/user_input
    outputs:
      - imdb_spiderman_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any (input is ignored but must be sent for compatibility)
* Metadata:

  ```json
  {
    "description": "unused; this input is ignored but required for wiring."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                   |
| ----------- | ------- | --------------------------------------------- |
| user_input  | Any     | Required placeholder; ignored by node logic   |

### Output Topics

| Topic                        | Type                        | Description                            |
| ---------------------------- | --------------------------- | -------------------------------------- |
| imdb_spiderman_api_response  | JSON (dict or string)        | IMDB query result or error message     |


## License

Released under the MIT License.
