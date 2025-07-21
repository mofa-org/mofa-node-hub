# AdresseApiNode

A Dora-rs node for accessing the French National Address API (api-adresse.data.gouv.fr). Provides both forward (search by name/address) and reverse (lookup address by latitude/longitude) geocoding methods for spatial data integration in multimodal pipelines.

## Features
- Forward geocoding via address/name search (`search` method)
- Reverse geocoding to retrieve address from latitude/longitude (`reverse` method)
- Structured error handling and detailed API response forwarding

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
  - id: adresse_api_node
    build: pip install -e .
    path: adresse_api_node.py
    inputs:
      method: input/method      # 'reverse' or 'search'
      lon: input/lon            # longitude (for reverse)
      lat: input/lat            # latitude (for reverse)
      q: input/q                # query string (for search)
    outputs:
      - adresse_api_response
      - adresse_api_error
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
  - id: point_source
    build: pip install your-node
    path: your-point-source.py
    outputs:
      - lon
      - lat
  - id: adresse_api_node
    build: pip install -e .
    path: adresse_api_node.py
    inputs:
      lon: point_source/lon
      lat: point_source/lat
      method: input/method
    outputs:
      - adresse_api_response

```

Your point source must output:

* Topic: `method` (either `reverse` or `search` as string)
* Topic: `lon` and `lat` (strings or floats, for `reverse`) **or** `q` (for `search`, as string)
* Data: single values
* Metadata:

  ```json
  {
    "type": "parameter",
    "datatype": "string|float",
    "description": "Input parameter for AdresseApiNode"
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                  |
|----------|--------|------------------------------|
| method   | string | 'reverse' or 'search' method |
| lon      | float  | Longitude for reverse lookup  |
| lat      | float  | Latitude for reverse lookup   |
| q        | string | Search query (for search)     |

### Output Topics

| Topic                 | Type     | Description                                     |
|-----------------------|----------|-------------------------------------------------|
| adresse_api_response  | object   | The API response (address info/results)          |
| adresse_api_error     | object   | Any error encountered during processing          |

## License

Released under the MIT License.
