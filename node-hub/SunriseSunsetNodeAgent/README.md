# sunrise_sunset_node

Fetch sunrise and sunset info from the official Sunrise-Sunset API via a Dora/Mofa node.

## Features
- Takes latitude and longitude (and optionally timezone) as input parameters
- Calls the official REST API for sunrise/sunset calculation
- Outputs result as JSON or descriptive error object

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
  - id: sunrise_sunset_node
    build: pip install -e .
    path: sunrise_sunset_node
    inputs:
      lat: input/lat
      lng: input/lng
      tzid: input/tzid  # optional
    outputs:
      - sunrise_sunset_info
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
    outputs:
      - lat
      - lng
      - tzid

  - id: sunrise_sunset_node
    build: pip install -e .
    path: sunrise_sunset_node
    inputs:
      lat: your_input_node/lat
      lng: your_input_node/lng
      tzid: your_input_node/tzid  # optional
    outputs:
      - sunrise_sunset_info
```

Your point source must output:

* Topic: `lat`, `lng`, and (optional) `tzid`
* Data: string representation of latitude, longitude, and optionally tzid
* Metadata:

  ```json
  {
    "lat": "string",
    "lng": "string",
    "tzid": "string (optional)"
  }
  ```

## API Reference

### Input Topics

| Topic | Type | Description |
|-------|------|-------------|
| lat   | str  | Latitude in string form |
| lng   | str  | Longitude in string form |
| tzid  | str  | Timezone identifier (optional) |

### Output Topics

| Topic                | Type      | Description                 |
|----------------------|-----------|-----------------------------|
| sunrise_sunset_info  | dict      | JSON dict with sunrise/sunset info or error message |


## License

Released under the MIT License.
