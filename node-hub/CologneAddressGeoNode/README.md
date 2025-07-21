# CologneAddressGeoNode

A Dora-rs node for fetching and serving Cologne city address geodata from the official Cologne open data endpoint (https://offenedaten-koeln.de/dataset/adressen-köln). The node can be integrated into data pipelines for geographic information, spatial analysis, and address-based services, automatically relaying address metadata as JSON.

## Features
- Fetches real-time Cologne address geodata from the city geoportal
- Exposes API for other nodes to trigger requests via parameters
- Robust error handling with error messages returned on failure

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
  - id: cologne_address_geo
    build: pip install -e .
    path: cologne_address_geo
    inputs:
      user_input: input/user_input
    outputs:
      - address_geojson
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
  - id: your_input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input

  - id: cologne_address_geo
    build: pip install -e .
    path: cologne_address_geo
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - address_geojson
```

Your point source must output:

* Topic: `user_input`
* Data: String or object depending on pipeline trigger needs
* Metadata:

  ```json
  {
    "description": "Parameter to trigger address geo data request. May be empty string if request should always proceed."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                         |
| ----------- | ------ | ----------------------------------- |
| user_input  | Any    | Triggers fetch of address geo data  |

### Output Topics

| Topic            | Type   | Description                                |
| ---------------- | ------ | ------------------------------------------ |
| address_geojson  | Dict   | JSON/dict Cologne address data or error    |


## License

Released under the MIT License.
