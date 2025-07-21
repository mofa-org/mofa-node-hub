# dnd_api_node

Bridge Dora node to fetch Dungeons & Dragons 5e data from selected API endpoints.

## Features
- Fetches data from the official D&D 5e API
- Supports selecting among multiple endpoints (Race: dwarf, Spells list, Ability: charisma)
- Returns responses in a serializable dict format for downstream nodes

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
  - id: dnd_api
    build: pip install -e dnd_api_node
    path: dnd_api_node
    inputs:
      endpoint_choice: input/endpoint_choice
    outputs:
      - dnd_api_response
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
  - id: input_param
    build: pip install your-parameter-node
    path: your-parameter-node
    outputs:
      - endpoint_choice
  - id: dnd_api
    build: pip install -e dnd_api_node
    path: dnd_api_node
    inputs:
      endpoint_choice: input_param/endpoint_choice
    outputs:
      - dnd_api_response
```

Your point source must output:

* Topic: `endpoint_choice`
* Data: String; one of `'dwarf'`, `'spells'`, or `'ability_scores_cha'`
* Metadata:

  ```json
  {
    "allowed": ["dwarf", "spells", "ability_scores_cha"],
    "type": "string",
    "description": "D&D 5e API endpoint to query."
  }
  ```

## API Reference

### Input Topics

| Topic             | Type   | Description                                      |
| ----------------- | ------ | ------------------------------------------------ |
| endpoint_choice   | str    | Choice of API endpoint: 'dwarf', 'spells', or 'ability_scores_cha' |

### Output Topics

| Topic              | Type   | Description                                                  |
| ------------------ | ------ | ------------------------------------------------------------ |
| dnd_api_response   | dict   | Raw API response from the DnD 5e API, or error dict if failed |


## License

Released under the MIT License.
