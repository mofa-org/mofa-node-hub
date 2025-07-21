# nominatim_geocoding

Lightweight Dora-rs node for OpenStreetMap's Nominatim Geocoding API, supporting city search, detailed OSM object info, and reverse geocoding with flexible parameterization.

## Features
- Search for city locations using Nominatim's HTTP API
- Obtain details of OSM objects by id and type
- Perform reverse geocoding from latitude/longitude coordinates

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
  - id: geocoder
    build: pip install -e .
    path: nominatim_geocoding
    inputs:
      user_input: any/input_topic
      operation: user/input/operation
      city: user/input/city
      osmtype: user/input/osmtype
      osmid: user/input/osmid
      format: user/input/format
      lat: user/input/lat
      lon: user/input/lon
      zoom: user/input/zoom
    outputs:
      - geocoding_result
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
  - id: your_node
    build: pip install your-node
    path: your_node
    outputs:
      - user_input
      - operation
      - city
      - osmtype
      - osmid
      - format
      - lat
      - lon
      - zoom

  - id: geocoder
    build: pip install -e .
    path: nominatim_geocoding
    inputs:
      user_input: your_node/user_input
      operation: your_node/operation
      city: your_node/city
      osmtype: your_node/osmtype
      osmid: your_node/osmid
      format: your_node/format
      lat: your_node/lat
      lon: your_node/lon
      zoom: your_node/zoom
    outputs:
      - geocoding_result
```

Your point source must output:

* Topic: `user_input` (and relevant parameters)
* Data: String or number parameters for geocoding
* Metadata:

  ```json
  {
    "parameters": [
      "user_input", "operation", "city", "osmtype", "osmid", "format", "lat", "lon", "zoom"
    ],
    "description": "All parameters are interpreted as strings unless otherwise specified"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                |
| ----------- | ------ | ------------------------------------------ |
| user_input  | Any    | Required: dummy input to trigger operation |
| operation   | str    | 'search_city', 'details', 'reverse'        |
| city        | str    | City name for search (search_city)         |
| osmtype     | str    | OSM type ('N', 'W', 'R') for details       |
| osmid       | int    | OSM id for details                         |
| format      | str    | Output format (json, jsonv2, ... )         |
| lat         | float  | Latitude for reverse geocoding             |
| lon         | float  | Longitude for reverse geocoding            |
| zoom        | int    | Zoom level for reverse geocoding           |

### Output Topics

| Topic            | Type   | Description                             |
| ----------------| ------ | --------------------------------------- |
| geocoding_result| dict   | Geocoding result or error info          |


## License

Released under the MIT License.
