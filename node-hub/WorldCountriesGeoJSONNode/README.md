# world_countries_node

Fetch World Countries GeoJSON Data from ArcGIS

## Features
- Download GeoJSON for all countries or a specific country
- Easy integration with Dora-rs and other MofaAgent pipelines
- Robust error reporting for failed lookups or network issues

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
  - id: world_countries
    build: pip install -e world_countries_node
    path: world_countries_node
    inputs:
      country: input/country  # Optional, supply a country name string to filter results
      user_input: input/user_input  # Optionally connect for QM compatibility
    outputs:
      - geojson_result
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
  - id: custom_input
    build: pip install your-custom-node
    path: your-custom-node
    outputs:
      - country  # Should output country name as a string

  - id: world_countries
    build: pip install -e world_countries_node
    path: world_countries_node
    inputs:
      country: custom_input/country
      user_input: input/user_input
    outputs:
      - geojson_result
```

Your point source must output:

* Topic: `country`
* Data: Country name as a string (e.g., "France") or empty string/null for all
* Metadata:

  ```json
  {
    "dtype": "string"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                       |
| ---------- | ------- | --------------------------------- |
| country    | string  | Optional country name to filter   |
| user_input | string  | Optional field for QM interop     |

### Output Topics

| Topic          | Type  | Description                     |
| -------------- | ----- | ------------------------------- |
| geojson_result | dict  | Resulting GeoJSON FeatureCollection or error message |


## License

Released under the MIT License.
