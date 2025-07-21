# emoji_api_node

A Dora-rs node that provides programmatic access to the EmojiHub API, enabling retrieval of all emojis, all travel-and-places emojis, or a random emoji. Selection is controlled by parameters, making it easy to integrate emoji data into your pipeline.

## Features
- Fetch all emoji data from EmojiHub
- Retrieve only travel-and-places category emojis
- Select and return a random emoji

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
  - id: emoji
    build: pip install -e .
    path: emoji_api_node
    inputs:
      parameters: input/parameters  # Accepts action and optional timeout
    outputs:
      - emoji_result
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
  - id: custom_param_source
    build: pip install your-parameter-node
    path: your-parameter-node
    outputs:
      - parameters
  - id: emoji
    build: pip install -e .
    path: emoji_api_node
    inputs:
      parameters: custom_param_source/parameters
    outputs:
      - emoji_result
```

Your point source must output:

* Topic: `parameters`
* Data: JSON object with action and/or timeout
* Metadata:

  ```json
  {
    "action": "all" | "travel_and_places" | "random", // string, optional (default: random)
    "timeout": 5 // integer in seconds, optional
  }
  ```

## API Reference

### Input Topics

| Topic      | Type                   | Description                                             |
| ---------- | ---------------------- | ------------------------------------------------------- |
| parameters | JSON/dict              | { "action": ..., "timeout": ... }. Controls API call.  |

### Output Topics

| Topic        | Type      | Description                            |
| ------------ | --------- | -------------------------------------- |
| emoji_result | JSON/dict | The emoji API response or error report. |


## License

Released under the MIT License.
