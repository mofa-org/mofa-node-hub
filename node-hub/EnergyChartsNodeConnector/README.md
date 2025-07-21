# energy_charts_node

EnergyChartsNodeConnector: Dora-rs node for retrieving energy market and public power data from energy-charts.info and providing structured outputs.

## Features
- Fetches day-ahead spot market price for DE-LU (Germany/Luxembourg)
- Retrieves public power statistics for Switzerland
- Outputs data in an easily consumable, serializable structure

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
  - id: energy_charts_node
    build: pip install -e .
    path: energy_charts_node
    inputs:
      user_input: input/user_input  # Placeholder for future parameterization
    outputs:
      - energy_charts_data
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
  - id: upstream_node
    build: pip install your-upstream-node
    path: your-upstream-node
    outputs:
      - user_input
  - id: energy_charts_node
    build: pip install -e .
    path: energy_charts_node
    inputs:
      user_input: upstream_node/user_input
    outputs:
      - energy_charts_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (parameter to propagate through pipeline, currently placeholder)
* Metadata:

  ```json
  {
      "description": "Parameter for future extensibility."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                       |
| ----------| ------ | --------------------------------- |
| user_input | Any    | Placeholder for user input/trigger |

### Output Topics

| Topic               | Type   | Description                                           |
| ------------------- | ------ | ----------------------------------------------------- |
| energy_charts_data  | dict   | JSON object with keys 'day_ahead_price_DE_LU' and 'public_power_CH', or error details |

## License

Released under the MIT License.
