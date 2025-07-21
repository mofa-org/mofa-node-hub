# pokemon3d_node

A Dora node that retrieves the full set of Pokémon 3D models from a public API endpoint in real-time. It offers seamless integration for workflows requiring detailed Pokémon 3D asset data.

## Features
- Fetches all available Pokémon 3D models via a public REST API
- Robust error handling for network requests
- Exposes the data as a Dora node output for downstream processing

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
  - id: pokemon3d
    build: pip install -e pokemon3d_node
    path: pokemon3d_node
    inputs: {}
    outputs:
      - pokemon_3d_models
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
  - id: pokemon3d
    build: pip install -e pokemon3d_node
    path: pokemon3d_node
    outputs:
      - pokemon_3d_models
  - id: consumer_node
    build: pip install -e path/to/your_consumer
    path: path/to/your_consumer
    inputs:
      pokemon_3d_models: pokemon3d/pokemon_3d_models
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": 1,
    "dtype": "float32",
    "shape": [1, 2]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                                 |
| ---------- | --------- | ------------------------------------------- |
| user_input | any/None  | Optional unused parameter for compatibility |

### Output Topics

| Topic              | Type   | Description                                                                |
| ------------------ | ------ | -------------------------------------------------------------------------- |
| pokemon_3d_models  | dict   | JSON content with all available Pokémon 3D models, or error message on fail |


## License

Released under the MIT License.
