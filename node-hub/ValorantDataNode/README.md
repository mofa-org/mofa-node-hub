# valorant_data_node

Fetches Valorant agents and buddies information from the Valorant public API and provides unified access in a Dora node environment.

## Features
- Retrieves latest Valorant "buddies" metadata
- Fetches full Valorant agent roster and details
- Aggregated data via a single output topic

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
  - id: valorant_data
    build: pip install -e valorant_data_node
    path: valorant_data_node
    outputs:
      - valorant_data
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
  - id: valorant_data
    build: pip install -e valorant_data_node
    path: valorant_data_node
    outputs:
      - valorant_data
  - id: consumer
    build: pip install your-consumer-node
    path: your-consumer-node
    inputs:
      valorant_info: valorant_data/valorant_data
```

Your point source must output:

* Topic: `valorant_data`
* Data: JSON with two keys: `buddies` and `agents` (`dict`)
* Metadata:

  ```json
  {
    "type": "object",
    "properties": {
      "buddies": {"type": "object"},
      "agents": {"type": "object"}
    }
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                           |
| ------------| ------ | ------------------------------------- |
| user_input  | any    | (Optional/ignored) Input parameter    |

### Output Topics

| Topic          | Type    | Description                                     |
| -------------- | ------- | ----------------------------------------------- |
| valorant_data  | object  | JSON dict with keys: `buddies` and `agents`     |


## License

Released under the MIT License.
