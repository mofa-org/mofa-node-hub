# pokeapi_data_node

A Dora node that retrieves data from the public PokeAPI, combining species, ability, and detailed info queries for fixed Pokémon endpoints. It exposes this composite data as a single output for integration into larger Dora pipelines.

## Features
- Fetches Pokémon species information from PokeAPI
- Retrieves Pokémon ability details from PokeAPI
- Aggregates diverse PokeAPI results in a single output

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
  - id: pokeapi
    build: pip install -e .
    path: pokeapi_data_node
    inputs:
      user_input: input/user_input
    outputs:
      - pokeapi_data
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
  # Your point source node
  - id: my_input_node
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_input
  - id: pokeapi
    build: pip install -e .
    path: pokeapi_data_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - pokeapi_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (can be empty or None)
* Metadata:

  ```json
  {"type": "trigger", "description": "Trigger the PokeAPI node to fetch."}
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                 |
| ---------- | ------ | -------------------------- |
| user_input | Any    | Triggers a PokeAPI fetch   |

### Output Topics

| Topic         | Type   | Description                             |
| ------------- | ------ | --------------------------------------- |
| pokeapi_data  | dict   | Combined PokeAPI results (species, info, ability) |

## License

Released under the MIT License.
