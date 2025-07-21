# colorado_business_data

Fetch all Colorado business records from the state's open data API and output as a JSON-serializable list. Designed for Dora-rs/MoFA dataflow pipelines and handles input/output messaging in compliance with agent node specs.

## Features
- Fetch statewide business records from Colorado's data API in real-time
- Sends results in JSON-serializable format for downstream consumption
- Robust error handling: all API and network issues are caught, and a structured error is returned

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
  - id: colorado-business-data
    build: pip install -e colorado_business_data
    path: colorado_business_data
    inputs:
      user_input: input/user_input
    outputs:
      - business_data
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
  - id: your-input-node
    build: pip install your-node
    path: your-node-path
    outputs:
      - user_input
  - id: colorado-business-data
    build: pip install -e colorado_business_data
    path: colorado_business_data
    inputs:
      user_input: your-input-node/user_input
    outputs:
      - business_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (ignored, can be dummy)
* Metadata:

  ```json
  {
    "description": "Any string value (content ignored, present for activation/compatibility)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                   |
|------------|--------|-----------------------------------------------|
| user_input | string | Trigger message for fetching (contents ignored; present for compatibility) |

### Output Topics

| Topic         | Type  | Description                                                           |
|---------------|-------|-----------------------------------------------------------------------|
| business_data | list  | List of business records from Colorado API or error JSON on failure |


## License

Released under the MIT License.
