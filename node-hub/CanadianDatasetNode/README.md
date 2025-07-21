# canadian_dataset_node

Access Canadian Open Data Portal (package_show) from Dora pipeline.

## Features
- Fetches real-time dataset metadata from Canada’s Open Data API
- Handles API errors gracefully with structured error outputs
- Simple interface: request dataset info by dataset ID

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
  - id: canadian-dataset
    build: pip install -e canadian_dataset_node
    path: canadian_dataset_node
    inputs:  # Expecting a dummy user_input to trigger
      user_input: input/user_input
    outputs:
      - canadian_dataset_output
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
  - id: your_node
    build: pip install -e your_node
    path: your_node
    outputs:
      - user_input

  - id: canadian-dataset
    build: pip install -e canadian_dataset_node
    path: canadian_dataset_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - canadian_dataset_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (used as dummy trigger parameter)
* Metadata:

  ```json
  {
    "description": "Any value to trigger the agent call."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description              |
| ---------- | ------- | ------------------------ |
| user_input | any     | Dummy trigger parameter. |

### Output Topics

| Topic                   | Type   | Description                                                               |
| ----------------------- | ------ | ------------------------------------------------------------------------- |
| canadian_dataset_output | dict   | Metadata/result from Open Canada dataset API (with error info if any).    |


## License

Released under the MIT License.
