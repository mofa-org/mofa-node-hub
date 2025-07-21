# china_holiday_info

Fetch up-to-date China holiday information from a public API and expose it as a Dora node output.

## Features
- Retrieves latest China holiday data via REST API
- Robust HTTP client logic with retries and error handling
- Integrates as a Dora node with configurable inputs and outputs

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
  - id: china_holiday_node
    build: pip install -e .
    path: china_holiday_info
    inputs:
      user_input: input/user_input # (optional, compatibility parameter)
    outputs:
      - china_holiday_data
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
  - id: my_custom_node
    build: pip install my-custom-node
    path: my_custom_node
    inputs:
      holiday_data: china_holiday_node/china_holiday_data
    outputs:
      - processed_result

  - id: china_holiday_node
    build: pip install -e .
    path: china_holiday_info
    inputs:
      user_input: input/user_input   # Optional parameter for compatibility
    outputs:
      - china_holiday_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (ignored, for compatibility)
* Metadata:

  ```json
  {
    "type": "any",
    "description": "Compatibility input; not used by node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ----------| ------ | ----------------------------------------- |
| user_input | any    | (Optional) Compatibility parameter; ignored |

### Output Topics

| Topic              | Type  | Description                          |
| ------------------ | ----- | ------------------------------------ |
| china_holiday_data | JSON  | China holiday API response (or error) |


## License

Released under the MIT License.
