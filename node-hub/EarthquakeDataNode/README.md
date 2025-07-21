# earthquake_data_node

Node for querying real-time or historical earthquake data from the USGS Earthquake API. Returns earthquake event data in GeoJSON format based on user-specified parameters (date range and minimum magnitude).

## Features
- Query USGS earthquake data by date range and magnitude
- Configurable parameters: starttime, endtime, minmagnitude
- Outputs complete GeoJSON event data as JSON string

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: earthquake_data_node
    build: pip install -e .
    path: earthquake_data_node
    inputs:
      parameters: input/parameters
    outputs:
      - earthquake_data
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
  - id: param_source
    build: pip install your-parameter-node
    path: your-parameter-node
    outputs:
      - parameters
  - id: earthquake_data_node
    build: pip install -e .
    path: earthquake_data_node
    inputs:
      parameters: param_source/parameters
    outputs:
      - earthquake_data
```

Your point source must output:

* Topic: `parameters`
* Data: A dictionary with keys: `starttime`, `endtime`, `minmagnitude`, all as strings, e.g.
* Metadata:

  ```json
  {
    "keys": ["starttime", "endtime", "minmagnitude"],
    "types": ["string", "string", "string"]
  }
  ```

## API Reference

### Input Topics

| Topic       | Type           | Description                               |
| ----------- | -------------- | ----------------------------------------- |
| parameters  | dict (str)     | Query parameters: starttime, endtime, minmagnitude |

### Output Topics

| Topic           | Type           | Description                                  |
| -------------- | -------------- | -------------------------------------------- |
| earthquake_data | JSON string    | Earthquake event data in GeoJSON (as string) |

## License

Released under the MIT License.
