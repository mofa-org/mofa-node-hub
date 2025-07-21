# avatar_api_node

Access episodic, character, and show information from SampleAPIs Avatar: The Last Airbender REST API endpoints via a Dora-rs node interface.

## Features
- Fetches Avatar: The Last Airbender episodes, character, or info data via REST API
- Parameter-based input for dynamic selection of API endpoint
- Structured pass-through of JSON response to Dora output topics

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
  - id: avatar_api
    build: pip install -e avatar_api_node
    path: avatar_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - episodes_data
      - characters_data
      - info_data
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
  - id: your_input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input

  - id: avatar_api
    build: pip install -e avatar_api_node
    path: avatar_api_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - episodes_data
      - characters_data
      - info_data
      - error
```

Your point source must output:

* Topic: `user_input`
* Data: String (e.g., `episodes`, `characters`, or `info`)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Which endpoint to query. Accepts 'episodes', 'characters', or 'info'. Defaults to 'info'."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                        |
| ---------- | ------ | ------------------------------------------------------------------ |
| user_input | string | Endpoint to query; accepts 'episodes', 'characters', or 'info'.    |

### Output Topics

| Topic            | Type   | Description                                                   |
| ---------------- | ------ | ------------------------------------------------------------- |
| episodes_data    | json   | JSON result from episodes endpoint                            |
| characters_data  | json   | JSON result from characters endpoint                          |
| info_data        | json   | JSON result from info endpoint                                |
| error            | string | Any error encountered during REST call or processing          |

## License

Released under the MIT License.
