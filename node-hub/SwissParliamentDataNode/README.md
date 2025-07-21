# swiss_parliament_node

Fetch Swiss Parliament Data Node

## Features
- Automatic retrieval of Swiss Parliament session information
- Fetches data about federal councillors (members)
- Retrieves voting records for councillors

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
  - id: swissparliament
    build: pip install -e swiss_parliament_node
    path: swiss_parliament_node
    inputs: {}
    outputs:
      - sessions_data
      - councillors_data
      - votes_data
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
  - id: swissparliament
    build: pip install -e swiss_parliament_node
    path: swiss_parliament_node
    outputs:
      - sessions_data
      - councillors_data
      - votes_data
  - id: your_node
    build: pip install -e your_node
    path: your_node
    inputs:
      sessions: swissparliament/sessions_data
      councillors: swissparliament/councillors_data
      votes: swissparliament/votes_data
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

| Topic       | Type  | Description                               |
| ----------- | ----- | ----------------------------------------- |
| user_input  | any   | Reserved parameter for future extensions. |

### Output Topics

| Topic             | Type | Description                            |
| ----------------- | ---- | -------------------------------------- |
| sessions_data     | any  | Parliament sessions data (JSON)        |
| councillors_data  | any  | List of councillors (JSON)             |
| votes_data        | any  | Votes by councillor (JSON)             |


## License

Released under the MIT License.
