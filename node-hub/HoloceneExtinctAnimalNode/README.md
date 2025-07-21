# holocene_extinct_node

Fetch a list of animals that went extinct in the Holocene epoch, provided as a ready-to-integrate Dora node. This module wraps the Extinct API with automatic data output and error handling for your data or workflow pipelines.

## Features
- Fetches up-to-date Holocene epoch extinct animal data from a public API
- Graceful error handling with error outputs for downstream resilience
- Dora-rs compatible: receive parameter, send output as required for pipeline integration

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
  - id: extinct_animals
    build: pip install -e .
    path: holocene_extinct_node
    inputs:
      user_input: input/user_input
    outputs:
      - holocene_extinct_animals
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
    build: pip install my-source-node
    path: my-source-node
    outputs:
      - user_input

  - id: extinct_animals
    build: pip install -e .
    path: holocene_extinct_node
    inputs:
      user_input: my_source_node/user_input
    outputs:
      - holocene_extinct_animals
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (dummy/None is OK)
* Metadata:

  ```json
  {
    "description": "Dummy parameter to trigger API request",
    "type": "any"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                            |
| ----------- | ------ | -------------------------------------- |
| user_input  | Any    | Dummy parameter to trigger the API call |

### Output Topics

| Topic                      | Type              | Description                                           |
| -------------------------- | ----------------- | ----------------------------------------------------- |
| holocene_extinct_animals   | Dict[str, Any]    | List of extinct animals or error dictionary if failed |


## License

Released under the MIT License.
