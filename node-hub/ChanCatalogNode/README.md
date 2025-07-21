# chan_catalog_node

A Dora-rs node for fetching real-time catalog data from multiple 4chan boards. This node enables pipeline integration of trending topics and board structures from 4chan, designed for flexible use with other Dora nodes such as statistical processors or text analysis agents.

## Features
- Fetches full catalogs from /po/ (Origami) and /3/ (3D) 4chan boards in real-time
- Emits complete board list metadata via the `boards` output
- Gracefully handles API failures with structured error messages

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
  - id: chan_catalog
    build: pip install -e chan_catalog_node
    path: chan_catalog_node
    inputs:
      user_input: input/user_trigger   # Can be from timer, file, etc.
    outputs:
      - origami_catalog
      - three_d_catalog
      - boards
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
  - id: custom_trigger
    build: pip install your-trigger-node
    path: your_trigger_node
    outputs:
      - user_trigger

  - id: chan_catalog
    build: pip install -e chan_catalog_node
    path: chan_catalog_node
    inputs:
      user_input: custom_trigger/user_trigger
    outputs:
      - origami_catalog
      - three_d_catalog
      - boards
```

Your point source must output:

* Topic: `user_trigger`
* Data: Any value (string, dict, etc. – ignored by this node, present for pipeline compatibility)
* Metadata:
  ```json
  {
    "description": "Any, ignored. Present to support chaining in the dataflow."
  }
  ```

## API Reference

### Input Topics

| Topic         | Type    | Description                                  |
| -------------|---------|----------------------------------------------|
| user_input   | Any     | Received event to trigger the catalog query.  |

### Output Topics

| Topic            | Type     | Description                                          |
|------------------|----------|------------------------------------------------------|
| origami_catalog  | object   | JSON catalog from the /po/ (Origami) board           |
| three_d_catalog  | object   | JSON catalog from the /3/ (3D) board                 |
| boards           | object   | JSON list/metadata of all 4chan boards               |


## License

Released under the MIT License.
