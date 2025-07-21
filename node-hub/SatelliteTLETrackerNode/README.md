# satellite_tle_node

Satellite TLE Fetch Node for Dora-rs

## Features
- Fetches up-to-date Two-Line Element (TLE) data for satellites
- Sends TLE data as structured JSON via Dora messaging
- Graceful error handling with informative error messages

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
  - id: satellite_tle_node
    build: pip install -e .
    path: satellite_tle_node
    inputs:
      user_input: some_topic/user_input
    outputs:
      - tle_data
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
    build: pip install -e .  # or your node's builder
    path: your_input_node
    outputs:
      - user_input

  - id: satellite_tle_node
    build: pip install -e .
    path: satellite_tle_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - tle_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (string/object/int)
* Metadata:

  ```json
  {
    "description": "User or node-supplied parameter to trigger TLE fetch"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type          | Description                                  |
| -------------| ------------- | ---------------------------------------------|
| user_input   | Any           | Parameter to trigger TLE retrieval (optional) |

### Output Topics

| Topic     | Type   | Description                                |
|-----------|--------|--------------------------------------------|
| tle_data  | dict   | JSON dictionary of TLE data or error info   |


## License

Released under the MIT License.
