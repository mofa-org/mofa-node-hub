# truth_or_dare_node

A Dora node that queries the truthordarebot.xyz APIs to provide Truth, Dare, Never Have I Ever, Would You Rather, or Paranoia prompts via Dora messaging. Easily add party game features to your Dora apps or agent pipelines!

## Features
- Query random party game prompts (Truth, Dare, WYR, Paranoia, NHIE)
- Flexible API selection via `user_input` parameter
- Simple REST integration wrapped in Dora/Mofa node interface

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
  - id: truth_or_dare_node
    build: pip install -e .
    path: truth_or_dare_node # or relative path if required
    inputs:
      user_input: input/user_input
    outputs:
      - game_api_response
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
  # Your node that picks a game mode and emits a 'user_input' (e.g., "truth", "dare", "paranoia")
  - id: game_input
    build: pip install your-custom-node   # Replace with your node's install line
    path: your-custom-node               # Replace with your node directory
    outputs:
      - user_input

  # The TruthOrDare node configuration
  - id: truth_or_dare_node
    build: pip install -e .
    path: truth_or_dare_node
    inputs:
      user_input: game_input/user_input
    outputs:
      - game_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: String of one of the following (case-insensitive):
  * "truth"
  * "dare"
  * "nhie"
  * "paranoia"
  * "wyr"
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Game API option (truth, dare, nhie, paranoia, wyr)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                               |
| ----------- | ------ | ---------------------------------------------------------|
| user_input  | string | Game type: one of 'truth', 'dare', 'nhie', 'paranoia', 'wyr' |

### Output Topics

| Topic             | Type   | Description                                                                |
| ----------------- | ------ | -------------------------------------------------------------------------- |
| game_api_response | object | API response containing prompt or error, structure varies by API endpoint  |

## License

Released under the MIT License.
