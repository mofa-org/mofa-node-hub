# publibike_station_node

Query Publibike Station Data via Dora Node

## Features
- Flexible HTTP interface to Publibike public station API
- Input parameter parsing with JSON validation
- Outputs station data or informative error messages

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
  - id: publibike_station
    build: pip install -e publibike_station_node
    path: publibike_station_node
    inputs:
      user_input: input/user_input
    outputs:
      - publibike_output
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
  - id: custom_input
    build: pip install your-custom-input-lib
    path: your-custom-input-module
    outputs:
      - user_input

  - id: publibike_station
    build: pip install -e publibike_station_node
    path: publibike_station_node
    inputs:
      user_input: custom_input/user_input
    outputs:
      - publibike_output
```

Your point source must output:

* Topic: `user_input`
* Data: JSON string with keys such as `action` and (optionally) `station_id`
* Metadata:
  ```json
  {
    "dtype": "str",
    "description": "JSON string specifying the requested action and parameters"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type  | Description                                 |
| ----------- | ----- | ------------------------------------------- |
| user_input  | str   | JSON string: `{ "action": ..., ... }`      |

### Output Topics

| Topic             | Type         | Description                               |
| ----------------- | ------------ | ----------------------------------------- |
| publibike_output  | dict/JSON    | Publibike API data or error message       |


## License

Released under the MIT License.
