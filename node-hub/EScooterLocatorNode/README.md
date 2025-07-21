# EScooterLocatorNode

Locate all available E-Scooters within 500m of a specific point using the Swiss Shared Mobility API.

## Features
- Discover E-scooters via Swiss Shared Mobility API
- Geographic search (by latitude and longitude)
- Simple Dora-rs integration; input/output topics

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
  - id: locator_node
    build: pip install -e escooter_locator_node
    path: escooter_locator_node
    inputs:
      lat: input/lat
      lon: input/lon
    outputs:
      - escooter_results
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
  - id: your_coords_source
    build: pip install your-coords-node
    path: your_coords_source
    outputs:
      - lat
      - lon
  - id: locator_node
    build: pip install -e escooter_locator_node
    path: escooter_locator_node
    inputs:
      lat: your_coords_source/lat
      lon: your_coords_source/lon
    outputs:
      - escooter_results
```

Your point source must output:

* Topic: `lat`, `lon`
* Data: String (latitude or longitude)
* Metadata:

  ```json
  {
    "dtype": "str"
  }
  ```

## API Reference

### Input Topics

| Topic   | Type | Description |
| ------- | ---- | ----------- |
| lat     | str  | Latitude as string |
| lon     | str  | Longitude as string |

### Output Topics

| Topic            | Type        | Description                             |
| ---------------- | ----------- | --------------------------------------- |
| escooter_results | dict or str | Swiss sharedmobility.ch API response or error |

## License

Released under the MIT License.
