# elevation_api_node

A Dora node integrating with the European Elevation API for geospatial elevation queries. Supports both single-point and multi-point elevation lookups via structured Dora messages.

## Features
- Query elevation for a single latitude/longitude coordinate
- Batch elevation query for multiple coordinates at once
- Handles errors gracefully and returns message-structured results

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
  - id: elevation
    build: pip install -e elevation_api_node
    path: elevation_api_node
    inputs:
      input_mode: input/input_mode
      latitude: input/latitude
      longitude: input/longitude
      pts: input/pts
    outputs:
      - elevation_result
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
  - id: my_gps_source
    build: pip install my-gps-node
    path: my-gps-node
    outputs:
      - latitude
      - longitude
      - pts
      - input_mode
  - id: elevation
    build: pip install -e elevation_api_node
    path: elevation_api_node
    inputs:
      input_mode: my_gps_source/input_mode
      latitude: my_gps_source/latitude
      longitude: my_gps_source/longitude
      pts: my_gps_source/pts
    outputs:
      - elevation_result
```

Your point source must output:

* Topic: `pts` (for multiple mode) or `latitude`/`longitude` (for single mode)
* Data: String representation of a Python list for `pts` or string/float for `latitude`/`longitude`
* Metadata:

  ```json
  {
    "input_mode": "single" | "multiple", 
    "latitude": "<float, required if single>", 
    "longitude": "<float, required if single>", 
    "pts": "<str, required if multiple>"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                                       |
|------------ |--------- |--------------------------------------------------|
| input_mode  | string   | Query type: 'single' for one point or 'multiple'  |
| latitude    | float    | Latitude coordinate (when input_mode is 'single') |
| longitude   | float    | Longitude coordinate (when input_mode is 'single')|
| pts         | string   | List of [lat,lon] pairs, as string, for 'multiple'|

### Output Topics

| Topic            | Type        | Description                                 |
|----------------- |------------|---------------------------------------------|
| elevation_result | dict/str    | Result from API, or error message if failed |

## License

Released under the MIT License.
