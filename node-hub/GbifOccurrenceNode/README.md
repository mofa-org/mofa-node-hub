# gbif_occurrence_node

Fetch GBIF Occurrence Data for 19th Century (1800-1899)

## Features
- Requests GBIF (Global Biodiversity Information Facility) occurrence records for specified years.
- Robust error handling and serialization of outputs for downstream Dora nodes.
- Compatible with MOFA agent framework via `MofaAgent`/`run_agent` interface.

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
  - id: gbif_occurrence
    build: pip install -e .
    path: gbif_occurrence_node
    inputs:
      user_input: input/user_input
    outputs:
      - gbif_occurrence_output
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
  - id: user_input
    build: pip install -e your-input-node
    path: your-input-node
    outputs:
      - user_input
  - id: gbif_occurrence
    build: pip install -e .
    path: gbif_occurrence_node
    inputs:
      user_input: user_input/user_input
    outputs:
      - gbif_occurrence_output
```

Your point source must output:

* Topic: `user_input`
* Data: String (dummy value, e.g., "start")
* Metadata:

  ```json
  {"type": "string", "required": true, "description": "Dummy parameter to trigger GBIF fetch."}
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ----------| ------ | ----------------------------------------- |
| user_input | string | Dummy input parameter to trigger request. |

### Output Topics

| Topic                  | Type  | Description                                 |
| ---------------------- | ----- | ------------------------------------------- |
| gbif_occurrence_output | dict  | Result dictionary or error message payload. |


## License

Released under the MIT License.
