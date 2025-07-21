# population_data_node

Access US Population Data in Real-Time via Dora Node

## Features
- Pulls latest US population data from the DataUSA API
- Structured error reporting for API and JSON issues
- Simple integration with other Dora nodes

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
  - id: population_data_node
    build: pip install -e .
    path: population_data_node
    inputs:
      user_input: input/user_input
    outputs:
      - population_data
      - population_api_error
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
  - id: my_source_node
    outputs:
      - user_input
  - id: population_data_node
    build: pip install -e .
    path: population_data_node
    inputs:
      user_input: my_source_node/user_input
    outputs:
      - population_data
      - population_api_error
```

Your point source must output:

* Topic: `user_input`
* Data: Free-form string or None
* Metadata:

  ```json
  {
    "description": "Free-form parameter to trigger the population API query."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                      |
| ----------|--------|--------------------------------------------------|
| user_input | string | Free-form parameter to trigger API fetch (unused) |

### Output Topics

| Topic                 | Type   | Description                                |
|-----------------------|--------|--------------------------------------------|
| population_data       | object | Raw API response JSON from DataUSA API     |
| population_api_error  | object | Error message object if API call fails     |


## License

Released under the MIT License.
