# SwissTransportNode

Agent interface for the Swiss public transport OpenData API (transport.opendata.ch).

## Features
- Query Swiss public transport stationboard (departures/arrivals) by station
- Search station locations and details by query
- Retrieve intercity connections between two stations

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
  - id: swiss_transport
    build: pip install -e swiss_transport_node
    path: swiss_transport_node
    inputs:
      user_input: input/user_input
      input_type: input/input_type
      params: input/params
    outputs:
      - stationboard
      - locations
      - connections
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
  - id: your_point_source
    build: pip install your-point-source
    path: your-point-source
    outputs:
      - user_input
      - input_type
      - params

  - id: swiss_transport
    build: pip install -e swiss_transport_node
    path: swiss_transport_node
    inputs:
      user_input: your_point_source/user_input
      input_type: your_point_source/input_type
      params: your_point_source/params
    outputs:
      - stationboard
      - locations
      - connections
      - error
```

Your point source must output:

* Topic: `params` (as JSON string/dict as required)
* Data: Example: `{"station": "Bern", "limit": 5}`
* Metadata:

  ```json
  {
    "type": "object",
    "schema": {
      "station": "string",
      "limit": "int",
      "query": "string",
      "from": "string",
      "to": "string"
    },
    "description": "Parameters for API queries; stationboard uses 'station' and 'limit', locations uses 'query', connections uses 'from' and 'to'"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                          |
| ------------|--------|----------------------------------------------------------------------|
| user_input   | any    | Dummy trigger input to enable chaining/invocation of the node         |
| input_type   | str    | API method: 'stationboard', 'locations', or 'connections'            |
| params       | str    | JSON string or dict of request parameters (see above for details)     |

### Output Topics

| Topic        | Type   | Description                                         |
| ------------|--------|-----------------------------------------------------|
| stationboard | dict   | JSON result for stationboard query                  |
| locations    | dict   | JSON result for station/location search             |
| connections  | dict   | JSON result for route/connections search            |
| error        | dict   | Error messages or unsupported input_type response   |


## License

Released under the MIT License.
