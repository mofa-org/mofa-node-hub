# elevation_coordinate_node

Query Elevation Data for Coordinates Using SRTM via OpenTopodata API.

## Features
- Retrieve elevation for arbitrary coordinates using the OpenTopodata SRTM dataset
- Configurable interpolation method (e.g., cubic, nearest)
- Graceful error reporting via output ports

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
    build: pip install -e elevation_coordinate_node
    path: elevation_coordinate_node
    inputs:
      locations: input/locations
      interpolation: input/interpolation
    outputs:
      - elevation_result
      - error
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
  - id: your_source
    build: pip install your-node
    path: your-node
    outputs:
      - locations
      - interpolation
  - id: elevation
    build: pip install -e elevation_coordinate_node
    path: elevation_coordinate_node
    inputs:
      locations: your_source/locations
      interpolation: your_source/interpolation
    outputs:
      - elevation_result
      - error
```

Your point source must output:

* Topic: `locations`
* Data: String of lat,lon pairs (e.g., "39.7391536,-104.9847034|40.748817,-73.985428")
* Metadata:

  ```json
  {
    "datatype": "str",
    "description": "Coordinates as 'lat,lon|lat2,lon2' string; required."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                  |
| ------------| -------| ------------------------------------------------------------ |
| locations   | str    | Bar-separated latitude,longitude pairs (e.g. "lat,lon|lat2,lon2"). Required. |
| interpolation | str  | (Optional) Interpolation method: 'cubic', 'nearest', etc. Defaults to 'cubic'. |

### Output Topics

| Topic            | Type   | Description                               |
|------------------|--------|-------------------------------------------|
| elevation_result | dict   | Returned elevation data (parsed JSON)      |
| error            | str    | Error details if any error occurred        |


## License

Released under the MIT License.
