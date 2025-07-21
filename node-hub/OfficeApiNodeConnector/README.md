# office_api_node

A Dora-rs node to fetch data from The Office API (https://theofficeapi.dev), allowing users to programmatically retrieve episodes or character information and integrate it into a Dora pipeline.

## Features
- Fetches The Office episode data via public API
- Fetches character information from The Office API
- Simple API endpoint selection via parameter

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
  - id: api_fetcher
    build: pip install -e office_api_node
    path: office_api_node
    inputs:
      api_type: input/api_type
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
  - id: my_input_node
    build: pip install your-node
    path: my_input_node
    outputs:
      - api_type

  - id: api_fetcher
    build: pip install -e office_api_node
    path: office_api_node
    inputs:
      api_type: my_input_node/api_type
    outputs:
      - api_response

  - id: my_output_node
    build: pip install your-output-node
    path: my_output_node
    inputs:
      api_response: api_fetcher/api_response
```

Your point source must output:

* Topic: `api_type`
* Data: String, either "episodes" or "characters"
* Metadata:

  ```json
  {
    "type": "string",
    "required": true,
    "allowed_values": ["episodes", "characters"]
  }
  ```

## API Reference

### Input Topics

| Topic     | Type   | Description                               |
|-----------|--------|-------------------------------------------|
| api_type  | string | API target to fetch ("episodes" or "characters") |

### Output Topics

| Topic        | Type   | Description       |
|--------------|--------|------------------|
| api_response | object | Response from the office API; Either JSON details about episodes, characters, or an error. |


## License

Released under the MIT License.
