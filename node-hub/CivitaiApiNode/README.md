# civitai_api_node

Dora-rs node for querying Civitai model/image endpoints with SFW/NSFW filtering. Provides a simple interface to Civitai's public API from your MOFA/Dora workflow.

## Features
- Query Civitai for models or images
- SFW/NSFW filtering of results
- Configurable API parameters (entity type, limit, nsfw)

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
  - id: civitai_api_node
    build: pip install -e .
    path: civitai_api_node
    inputs:
      user_input: input/user_input
      entity_type: input/entity_type
      limit: input/limit
      nsfw: input/nsfw
    outputs:
      - civitai_api_response
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
      - entity_type
      - limit
      - nsfw
      - user_input
  - id: civitai_api_node
    build: pip install -e .
    path: civitai_api_node
    inputs:
      user_input: your_input_node/user_input
      entity_type: your_input_node/entity_type
      limit: your_input_node/limit
      nsfw: your_input_node/nsfw
    outputs:
      - civitai_api_response
```

Your point source must output:

* Topic: `user_input`, `entity_type`, `limit`, `nsfw`
* Data: Strings for each parameter
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Input parameters for the Civitai API node. Must include at least entity_type ('models' or 'images'). Optional: limit (int as string), nsfw ('none', 'soft', 'mature', 'x')."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                |
| ------------|--------|-----------------------------------------------------------|
| user_input   | str    | Placeholder input for MOFA/Dora compliance                |
| entity_type  | str    | Required. 'models' or 'images'                            |
| limit        | str    | Optional. Limits number of results (default: '10')        |
| nsfw         | str    | Optional. NSFW filter: 'none', 'soft', 'mature', 'x'      |

### Output Topics

| Topic                | Type  | Description                                                     |
|----------------------|-------|-----------------------------------------------------------------|
| civitai_api_response | dict  | Full API response from Civitai or error message as dict         |


## License

Released under the MIT License.
