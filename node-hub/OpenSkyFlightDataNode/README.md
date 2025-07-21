# opensky_flight_node

OpenSkyFlightDataNode: Retrieve Real-Time Air Traffic Data from OpenSky Network

## Features
- Query multiple OpenSky API endpoints for real-time or historical flight data (Switzerland airspace, Frankfurt arrivals, worldwide states)
- Robust error handling and logging for API request failures
- Provides a standardized output (JSON/text) for downstream Dora pipeline integration

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
  - id: opensky
    build: pip install -e ./opensky_flight_node
    path: opensky_flight_node
    inputs:
      user_input: input/user_input  # Optional, kept for compatibility
      api_choice: input/api_choice
    outputs:
      - flight_data
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
  - id: your_source_node
    build: pip install -e ./your_source_node
    path: your_source_node
    outputs:
      - api_choice

  - id: opensky
    build: pip install -e ./opensky_flight_node
    path: opensky_flight_node
    inputs:
      api_choice: your_source_node/api_choice
      user_input: input/user_input  # Optional
    outputs:
      - flight_data

  - id: downstream_consumer
    build: pip install -e ./downstream_consumer
    path: downstream_consumer
    inputs:
      flight_data: opensky/flight_data
```

Your point source must output:

* Topic: `api_choice`
* Data: One of `switzerland_airplanes`, `frankfurt_arrivals`, or `all_states` (as a string)
* Metadata:

  ```json
  {
    "type": "string",
    "allowed_values": ["switzerland_airplanes", "frankfurt_arrivals", "all_states"]
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| user_input  | any    | Pass-through, compatibility (not used)   |
| api_choice  | string | One of 'switzerland_airplanes', 'frankfurt_arrivals', or 'all_states' |

### Output Topics

| Topic        | Type   | Description                                |
| ------------ | ------ | ------------------------------------------ |
| flight_data  | dict   | Result: {error: bool, data/message/status_code}
|


## License

Released under the MIT License.
