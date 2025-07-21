# space_launch_node

Dora-rs node for dynamic retrieval of space launch information, agencies, or astronauts from The Space Devs API.

## Features
- Fetch real-time launcher data from The Space Devs API
- Retrieve curated agency or astronaut lists on demand
- Simple endpoint selection with robust error reporting

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
  - id: space_launch_node
    build: pip install -e .
    path: space_launch_node
    inputs:
      user_input: input/user_input
      endpoint_type: input/endpoint_type # Should be 'launch_data', 'agencies', or 'astronauts'
    outputs:
      - spacelaunch_output
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
  - id: my_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - endpoint_type
      - user_input

  - id: space_launch_node
    build: pip install -e .
    path: space_launch_node
    inputs:
      user_input: my_input_node/user_input
      endpoint_type: my_input_node/endpoint_type
    outputs:
      - spacelaunch_output
```

Your point source must output:

* Topic: `endpoint_type`
* Data: string (either 'launch_data', 'agencies', or 'astronauts')
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Which API endpoint to fetch. Must be one of: launch_data, agencies, astronauts."
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                                          |
|-----------------|--------|----------------------------------------------------------------------|
| user_input      | any    | Optional trigger or contextual message for orchestrating inputs        |
| endpoint_type   | string | API endpoint to fetch; one of: 'launch_data', 'agencies', 'astronauts'|

### Output Topics

| Topic              | Type         | Description                                       |
|--------------------|-------------|---------------------------------------------------|
| spacelaunch_output | JSON object | The API response or error information as a dict   |


## License

Released under the MIT License.
