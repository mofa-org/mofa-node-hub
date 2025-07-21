# digimon_card_api_node

A Dora-rs node for seamless integration with the Digimon Card Game API. It lets you search for specific Digimon cards or fetch the whole card catalog with customizable parameters―all consumable from any dora-rs pipeline.

## Features
- Search Digimon cards using any supported parameter (name, color, set, etc.)
- Retrieve the full Digimon card catalog, with sorting and filtering
- Simple Dora-compatible inputs/outputs for robust pipeline integration

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
  - id: card_api
    build: pip install -e digimon_card_api_node
    path: digimon_card_api_node
    inputs:
      mode: input/mode
      params: input/params
      user_input: input/user_input
    outputs:
      - api_response
      - api_error
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
    build: pip install your-node
    path: your_input_node
    outputs:
      - mode
      - params
      - user_input

  - id: card_api
    build: pip install -e digimon_card_api_node
    path: digimon_card_api_node
    inputs:
      mode: your_input_node/mode
      params: your_input_node/params
      user_input: your_input_node/user_input
    outputs:
      - api_response
      - api_error
```

Your point source must output:

* Topic: `params` (as JSON string, can be empty `{}`)
* Topic: `mode` (either `search` or `get_all`)
* Topic: `user_input` (any string, not used for API but required for node linkage)
* Data: See API Reference
* Metadata:

  ```json
  {
    "mode": "search",
    "params": "{\"n\":\"Aldamon\"}",
    "user_input": "trigger"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                          |
| ------------| ------ | --------------------------------------------------- |
| mode        | str    | 'search' or 'get_all' (API endpoint switch)         |
| params      | str    | JSON string with API parameters (optional)          |
| user_input  | str    | Placeholder input for node linkage (required)       |

### Output Topics

| Topic        | Type         | Description                                     |
| ------------ | ------------| ----------------------------------------------- |
| api_response | dict/list/str| API response: found cards, card info(s), or raw |
| api_error    | dict         | API error information (with failure message)     |


## License

Released under the MIT License.
