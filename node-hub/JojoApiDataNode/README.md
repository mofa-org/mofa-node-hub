# jojo_api_node

JojoApiDataNode: Dora-rs node for fetching JoJo's Bizarre Adventure characters and stands from the Stand-by-me public API.

## Features
- Fetches characters data from the /characters API endpoint
- Fetches stands data from the /stands API endpoint
- Unified Dora interface for other nodes to consume character & stand data

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
  - id: jojo_api_node
    build: pip install -e .
    path: jojo_api_node
    inputs:
      user_input: input/user_input  # any string to trigger API requests
    outputs:
      - characters
      - stands
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

  - id: jojo_api_node
    build: pip install -e .
    path: jojo_api_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - characters
      - stands

  - id: downstream_processor
    build: pip install your-downstream-processor
    path: downstream-processor
    inputs:
      characters: jojo_api_node/characters
      stands: jojo_api_node/stands
```

Your point source must output:

* Topic: `user_input`
* Data: Any string trigger
* Metadata:

  ```json
  {
    "description": "Any string to trigger the API request, e.g. 'get'",
    "type": "str"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                      |
| ------------| ------ | -------------------------------- |
| user_input  | str    | Any string to trigger API fetch.  |

### Output Topics

| Topic      | Type                      | Description                         |
| ---------- | ------------------------- | ----------------------------------- |
| characters | dict or list (JSON)       | List or dict with character data    |
| stands     | dict or list (JSON)       | List or dict with stand data        |


## License

Released under the MIT License.
