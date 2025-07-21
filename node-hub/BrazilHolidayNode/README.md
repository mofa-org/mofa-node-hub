# brazil_holiday_node

A Dora-rs node for retrieving official Brazilian 2024 holidays using the BrasilAPI. Returns all holiday data as a structured list, ready for integration with other pipeline components.

## Features
- Fetches all official holidays in Brazil for 2024
- Robust error handling with user-friendly output
- Simple integration as a data source node in Dora-rs pipelines

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
  - id: brazil_holiday_node
    build: pip install -e .
    path: brazil_holiday_node
    inputs:
      user_input: input/user_input
    outputs:
      - holidays_2024
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
  - id: my_preprocessor
    build: pip install my-preprocessor
    path: my_preprocessor
    outputs:
      - user_input

  - id: brazil_holiday_node
    build: pip install -e .
    path: brazil_holiday_node
    inputs:
      user_input: my_preprocessor/user_input
    outputs:
      - holidays_2024

  - id: my_consumer
    build: pip install my-consumer
    path: my_consumer
    inputs:
      holidays_2024: brazil_holiday_node/holidays_2024
```

Your point source must output:

* Topic: `user_input`
* Data: Free-form user parameter (not required for this node, but allows chaining)
* Metadata:

  ```json
  {
    "description": "User-defined input parameter (optional, not required by BrazilHolidayNode)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type     | Description                                         |
| ---------- | -------- | --------------------------------------------------- |
| user_input | Any      | Optional parameter for extensibility (not required) |

### Output Topics

| Topic         | Type    | Description                                       |
| ------------- | ------- | ------------------------------------------------- |
| holidays_2024 | list/dict | List of Brazilian 2024 holidays, or error object |


## License

Released under the MIT License.
