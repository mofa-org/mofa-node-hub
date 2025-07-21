# dictionary_api_node

Agent node for querying definitions from FreedictionaryAPI and returning the results as Dora-compatible output. Designed for streamlined integration in Dora-rs dataflow pipelines.

## Features
- Queries FreedictionaryAPI for English word definitions
- Graceful HTTP error and JSON error reporting
- Compatible with Dora-rs parameter and output conventions

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
  - id: dictionary_api_node
    build: pip install -e .
    path: dictionary_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - dictionary_api_result
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
    path: your-input-node
    outputs:
      - user_input

  - id: dictionary_api_node
    build: pip install -e .
    path: dictionary_api_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - dictionary_api_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (for compatibility; value is not used)
* Metadata:

  ```json
  {
    "type": "string",
    "purpose": "Compatibility placeholder for triggering the API call"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                          |
| ----------- | ------ | ------------------------------------ |
| user_input  | string | Placeholder for triggering execution |

### Output Topics

| Topic                 | Type   | Description                               |
| --------------------- | ------ | ----------------------------------------- |
| dictionary_api_result | object | Result from FreedictionaryAPI (raw JSON), or error info |

## License

Released under the MIT License.
