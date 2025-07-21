# location_coordinate_node

A Dora-rs node for retrieving location data from a remote API endpoint. This node acts as a bridge between the Dora/MOFA framework and external web APIs, returning geolocation information or error messages.

## Features
- Receives parameter input from Dora/Mofa pipelines
- Makes HTTP requests to a public geolocation API
- Publishes the raw API result or errors to downstream nodes

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
  - id: location_coordinate_node
    build: pip install -e .
    path: location_coordinate_node
    inputs:
      user_input: input/user_input
    outputs:
      - location_api_response
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
    build: pip install -e .  # Replace with your node's name
    path: your_input_node
    outputs:
      - user_input

  - id: location_coordinate_node
    build: pip install -e .
    path: location_coordinate_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - location_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: (Any value to trigger the request)
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Input trigger, content unused by this node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                          |
| ----------|--------|--------------------------------------|
| user_input | string | Input trigger, content not required. |

### Output Topics

| Topic                 | Type   | Description                                                 |
|-----------------------|--------|-------------------------------------------------------------|
| location_api_response | string | Result from https://mcinenews.net/LAT/ (raw API response or error message) |

## License

Released under the MIT License.
