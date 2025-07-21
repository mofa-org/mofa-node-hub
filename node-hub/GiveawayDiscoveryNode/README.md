# giveaway_discovery

Fetch and aggregate free game giveaways from the GamerPower API.

## Features
- Aggregates free game giveaway data from the GamerPower network
- Returns a list of currently available giveaways with error handling
- Simple integration as a Dora-rs node, compatible with automated pipelines

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
  - id: giveaway_discovery
    build: pip install -e .
    path: giveaway_discovery
    inputs:
      user_input: dora/any/input  # Optional, placeholder for dataflow compatibility
    outputs:
      - giveaways
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
    build: pip install my_input_node
    path: my_input_node
    outputs:
      - user_input
  - id: giveaway_discovery
    build: pip install -e .
    path: giveaway_discovery
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - giveaways
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (optional/unused in this node, but required for compatibility)
* Metadata:

  ```json
  {
    "description": "Optional input for dataflow compatibility; not used."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type          | Description                                   |
| ---------- | ------------- | --------------------------------------------- |
| user_input | any/optional  | Placeholder input for dataflow compatibility. |

### Output Topics

| Topic     | Type             | Description                                                           |
| --------- | ---------------- | --------------------------------------------------------------------- |
| giveaways | list[dict] \| dict | List of giveaways as returned by GamerPower, or error info as dict.   |


## License

Released under the MIT License.
