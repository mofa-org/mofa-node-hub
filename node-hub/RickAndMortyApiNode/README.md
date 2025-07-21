# rick_and_morty_node

A Dora-rs node that fetches the complete set of data from three Rick & Morty API endpoints (episodes, characters, locations) and returns all of it as a single structured output. The node is suitable for data ingestion, experimentation, and downstream composable pipelines.

## Features
- Fetches all episodes, characters, and locations from the Rick & Morty API
- Combines multiple API endpoints into one result dictionary
- Robust error handling with structured error messages

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
  - id: rickandmorty_api_node
    build: pip install -e .
    path: rick_and_morty_node
    outputs:
      - rickandmorty_full_data
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
  - id: rickandmorty_api_node
    build: pip install -e .
    path: rick_and_morty_node
    outputs:
      - rickandmorty_full_data

  - id: consumer
    build: pip install -e .
    path: your_consumer_node
    inputs:
      rickdata: rickandmorty_api_node/rickandmorty_full_data
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": 0,
    "dtype": "float32",
    "shape": [0, 2]
  }
  ```

## API Reference

### Input Topics

| Topic        | Type  | Description                                   |
| ------------| ------| ----------------------------------------------|
| user_input  | any   | Placeholder for dataflow compatibility.        |

### Output Topics

| Topic                  | Type  | Description                                                             |
| ---------------------- | ----- | ----------------------------------------------------------------------- |
| rickandmorty_full_data | dict  | Dictionary containing episode, character, and location API responses.    |

## License

Released under the MIT License.
