# transport_rest_node

Connect to the transport.rest API and forward queries to selected endpoints within a Dora-rs pipeline. This node enables data-driven access to stations, departures, or station search from the German and European mobility open platform.

## Features
- Query station metadata and filter by DBLounge availability
- Autocomplete stations using query strings
- Fetch real-time departures for a station in a specified direction

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
  - id: transport
    build: pip install -e transport_rest_node
    path: transport_rest_node
    inputs:
      endpoint_key: input/endpoint_key
      user_input: input/user_input
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
  - id: other_source
    build: pip install your-other-node
    path: your-other-node
    outputs:
      - endpoint_key
      - user_input

  - id: transport
    build: pip install -e transport_rest_node
    path: transport_rest_node
    inputs:
      endpoint_key: other_source/endpoint_key
      user_input: other_source/user_input
    outputs:
      - api_response
```

Your point source must output:

* Topic: `endpoint_key`
* Data: String, one of ["stations_with_dblounge", "autocomplete_stations", "departures_from_halle"]
* Metadata:

  ```json
  {
    "description": "API endpoint key to query: stations_with_dblounge, autocomplete_stations, or departures_from_halle"
  }
  ```

## API Reference

### Input Topics

| Topic          | Type   | Description                                                        |
| --------------| ------ | ------------------------------------------------------------------ |
| endpoint_key   | str    | API endpoint key (see allowed values above)                        |
| user_input     | str    | Optional payload chained (not used for API request in current node) |

### Output Topics

| Topic        | Type         | Description                  |
| ------------| ------------ | ---------------------------- |
| api_response| dict/list/str | Transport.rest API response. |

## License

Released under the MIT License.
