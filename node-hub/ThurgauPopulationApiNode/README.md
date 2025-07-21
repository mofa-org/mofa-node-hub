# thurgau_population_api

A Dora-rs node for accessing and distributing population dataset records from the Canton Thurgau (Switzerland) public records API. Provides structured, serializable outputs that can be integrated downstream in your pipeline.

## Features
- Fetches up-to-date population data from Thurgau open government API
- Robust error handling with explicit error topic output
- Easy integration with Dora-flow and MofaAgent-based nodes

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
  - id: thurgau_population_api
    build: pip install -e .
    path: thurgau_population_api
    inputs:
      user_input: input/user_input
    outputs:
      - thurgau_population_data
      - error
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
  - id: point_source
    build: pip install your-node
    path: your-node
    outputs:
      - user_input

  - id: thurgau_population_api
    build: pip install -e .
    path: thurgau_population_api
    inputs:
      user_input: point_source/user_input
    outputs:
      - thurgau_population_data
      - error
```

Your point source must output:

* Topic: `user_input`
* Data: (Any, or empty object)
* Metadata:

  ```json
  {
    "type": "trigger",
    "description": "Triggers population data fetch"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                           |
| ----------- | ------ | ------------------------------------- |
| user_input  | Any    | Triggers the agent to fetch data      |

### Output Topics

| Topic                     | Type   | Description                                                    |
| ------------------------- | ------ | -------------------------------------------------------------- |
| thurgau_population_data   | dict/list | Population JSON result from API (or string if decoding error) |
| error                    | dict   | Error message with details if fetch or processing fails        |

## License

Released under the MIT License.
