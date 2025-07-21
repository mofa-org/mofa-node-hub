# nextbike_data_node

A Dora node to retrieve real-time bike-sharing data from the Nextbike public API. Allows filtered queries by city, geolocation, and bike-sharing domain.

## Features
- Query Nextbike's global bike-sharing network data in real time
- Filter results by city ID, latitude/longitude, or operator domain
- Simple output as parsed JSON for integration with other nodes

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
  - id: nextbike
    build: pip install -e .
    path: nextbike_data_node
    inputs:
      parameters: input/parameters  # Optional: can inject params from other node
    outputs:
      - api_response
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
  - id: params_source
    build: pip install your-param-node
    path: your-param-node
    outputs:
      - parameters

  - id: nextbike
    build: pip install -e .
    path: nextbike_data_node
    inputs:
      parameters: params_source/parameters
    outputs:
      - api_response
```

Your point source must output:

* Topic: `parameters`
* Data: Dictionary with string values (all parameters are optional):
* Metadata:

  ```json
  {
    "city": "1",           // Optional, city ID as string
    "lat": "51.34049",    // Optional, latitude as string
    "lng": "12.36890",    // Optional, longitude as string
    "domains": "kg"       // Optional, domain/brand as string
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                                       |
| ----------- | -------- | -------------------------------------------------|
| parameters  | dict     | Query parameters for the Nextbike API call        |

### Output Topics

| Topic        | Type  | Description                                  |
| ------------ | ------ | --------------------------------------------- |
| api_response | dict   | Parsed Nextbike API JSON result or error dict |


## License

Released under the MIT License.
