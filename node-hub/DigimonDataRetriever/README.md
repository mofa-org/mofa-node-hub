# digimon_data_retriever

Retrieve Digimon API Data as a Dora-rs Node

## Features
- Fetches metadata and details of specific and all Digimon using a public API
- Single-output design for easy pipeline integration
- Handles endpoint errors gracefully and aggregates all results

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
  - id: digimon_api
    build: pip install -e .
    path: digimon_data_retriever
    inputs:
      user_input: input/user_input
    outputs:
      - digimon_data
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
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input
  - id: digimon_api
    build: pip install -e .
    path: digimon_data_retriever
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - digimon_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable string or JSON object (unused in this node, placeholder for integration)
* Metadata:

  ```json
  {
    "type": "string",
    "desc": "Placeholder input for future compatibility. Not used by the agent."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| user_input  | String | Placeholder for integration purposes    |

### Output Topics

| Topic         | Type     | Description                                |
| ------------- | -------- | ------------------------------------------ |
| digimon_data  | Object   | Results from Digimon API calls (JSON/dict) |


## License

Released under the MIT License.
