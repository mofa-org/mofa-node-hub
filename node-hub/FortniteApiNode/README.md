# fortnite_api_node

A Dora node that fetches and serves real-time Fortnite data (cosmetics, map, and playlists) from the public Fortnite-API. Designed for seamless integration into larger Dora or MOFA pipelines, this node allows other services or agents to access and utilize Fortnite API data with ease.

## Features
- Fetches up-to-date Fortnite cosmetics, map, and playlists from Fortnite-API
- Simple input interface for easy port composition
- Structured output includes both successful data and error reporting

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
  - id: fortnite_api_node
    build: pip install -e fortnite_api_node
    path: fortnite_api_node
    inputs:
      user_input: input/user_input   # Optional, left blank to trigger fetch
    outputs:
      - fortnite_api_data
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
  - id: your_node
    build: pip install your-node
    path: your-node
    outputs:
      - user_input

  - id: fortnite_api_node
    build: pip install -e fortnite_api_node
    path: fortnite_api_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - fortnite_api_data
```

Your point source must output:

* Topic: `user_input`
* Data: (any, typically a string or None to trigger fetch)
* Metadata:

  ```json
  {
    "description": "Any input; usually None or trigger string",
    "type": "string or None"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                  |
| ---------- | ------ | ---------------------------- |
| user_input | any    | Triggers fetch; may be None. |

### Output Topics

| Topic             | Type   | Description                                                         |
| ----------------- | ------ | ------------------------------------------------------------------- |
| fortnite_api_data | object | Fortnite API fetch result. Contains `results` (dict) and `errors`.   |

## License

Released under the MIT License.
