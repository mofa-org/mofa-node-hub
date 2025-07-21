# softwium_api_node

A Dora-rs node for fetching aggregated data from the Softwium public APIs (currencies, books, pokemons, peoples) with error handling, exposed as a single data stream for further integration in any Dora pipeline.

## Features
- Fetches latest data from all Softwium API endpoints in parallel
- Bundles results and error details in a unified output
- Compatible with programmatic dataflow (supports `user_input` parameter for chaining)

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: softwium_api_node
    build: pip install -e .
    path: softwium_api_node
    inputs:
      user_input: input/user_input  # Allows optional flow chaining
    outputs:
      - softwium_data
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
  - id: softwium_api_node
    build: pip install -e .
    path: softwium_api_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - softwium_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (optional, not used by this node)
* Metadata:

  ```json
  {
    "description": "Optional user input to trigger API fetch. Content is ignored by node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description             |
| ----------|--------|------------------------|
| user_input | any    | Optional trigger input. |

### Output Topics

| Topic         | Type   | Description                                                                       |
|-------------- |--------|-----------------------------------------------------------------------------------|
| softwium_data | dict   | Dictionary containing keys `data` (results per API) and `errors` (per-endpoint).   |

## License

Released under the MIT License.
