# radical_character_api

Easy API integration node for fetching Chinese radical character data from the Hemiola CCDB API for Dora-rs graphs.

## Features
- Fetches Chinese radical character data from the Hemiola CCDB API
- Simple API query mechanism via `requests`
- Dora-rs node for easy pipeline integration

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
  - id: radical_character_api
    build: pip install -e .
    path: radical_character_api
    inputs:
      user_input: input/user_input
    outputs:
      - character_info
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

  - id: radical_character_api
    build: pip install -e .
    path: radical_character_api
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - character_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any compatible user input (unused by this node, but required for the pipeline)
* Metadata:

  ```json
  {
    "description": "String or object representing user input. Unused, but for pipeline compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type         | Description                                                               |
| ----------| ------------ | ------------------------------------------------------------------------- |
| user_input | any          | Received for compatibility; not directly used by this node                |

### Output Topics

| Topic           | Type                | Description                                                           |
| -------------- | ------------------- | --------------------------------------------------------------------- |
| character_info  | dict                | JSON response or error about the Chinese radical character from API   |


## License

Released under the MIT License.
