# sbb_intercity_node

Swiss Federal Railways (SBB) Intercity Traffic Dora Node

## Features
- Live fetch of SBB Intercity departure data
- Query for cancellations or train delays
- Simple integration with Dora workflows

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
  - id: sbb_intercity
    build: pip install -e .
    path: sbb_intercity_node
    inputs:
      data_type: input/data_type  # Optional, default: "departures"
    outputs:
      - sbb_output
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
  - id: sbb_intercity
    build: pip install -e .
    path: sbb_intercity_node
    inputs:
      data_type: other_node/data_type
    outputs:
      - sbb_output
```

Your point source must output:

* Topic: `data_type`
* Data: string, one of ["departures", "cancellations", "delays"]
* Metadata:

  ```json
  {
    "dtype": "string",
    "enum": ["departures", "cancellations", "delays"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                              |
| ---------- | ------ | ---------------------------------------- |
| data_type  | str    | (Optional) One of: departures, cancellations, delays. Defaults to departures. |

### Output Topics

| Topic       | Type        | Description                      |
| ----------- | ---------- | -------------------------------- |
| sbb_output  | dict       | SBB API response (live data, errors, or status) |


## License

Released under the MIT License.
