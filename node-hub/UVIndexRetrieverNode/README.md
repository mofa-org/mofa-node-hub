# uv_index_node

Dora node for real-time retrieval of the UV Index using geospatial coordinates. This node queries the currentuvindex.com public API and outputs the latest UV index report for given latitude/longitude pairs.

## Features
- Fetches real-time UV Index data from external API
- Validates input geocoordinates and delivers error handling
- Simple integration with other Dora nodes via flexible input/output

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
  - id: uvindex
    build: pip install -e uv_index_node
    path: uv_index_node
    inputs:
      latitude: input/latitude
      longitude: input/longitude
    outputs:
      - uv_result
    env:
      # Optional: provide defaults
      LATITUDE: "40.6943"
      LONGITUDE: "-73.9249"
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
  - id: location-input
    build: pip install your-input
    path: your-input-node
    outputs:
      - latitude
      - longitude

  - id: uvindex
    build: pip install -e uv_index_node
    path: uv_index_node
    inputs:
      latitude: location-input/latitude
      longitude: location-input/longitude
    outputs:
      - uv_result
```

Your point source must output:

* Topic: `latitude`, `longitude`
* Data: string (convertible to float)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Latitude and longitude as string values. Example: '40.6943', '-73.9249'"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                      |
|-------------|--------|----------------------------------|
| latitude    | string | Latitude coordinate as string    |
| longitude   | string | Longitude coordinate as string   |

### Output Topics

| Topic      | Type   | Description                                       |
|------------|--------|---------------------------------------------------|
| uv_result  | dict   | JSON object containing the UV index API response  |

## License

Released under the MIT License.
