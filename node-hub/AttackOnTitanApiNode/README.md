# attack_on_titan_node

Attack on Titan Public API Dora Node

## Features
- Retrieves data from the public Attack on Titan API (characters, episodes, organizations, locations, titans, and base routes)
- Outputs aggregated API data in a single message for downstream Dora nodes
- Designed for seamless integration in Dora/Mofa dataflow pipelines

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
  - id: attack_on_titan_api
    build: pip install -e attack_on_titan_node
    path: attack_on_titan_node
    inputs:
      user_input: input/user_input  # Placeholder input for connectivity
    outputs:
      - aot_api_data
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
  - id: your_point_source
    build: pip install your-point-source
    path: your-point-source
    outputs: [user_input]

  - id: attack_on_titan_api
    build: pip install -e attack_on_titan_node
    path: attack_on_titan_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - aot_api_data
```

Your point source must output:

* Topic: `user_input`
* Data: Placeholder input (can be any data, not used)
* Metadata:

  ```json
  {
    "type": "placeholder",
    "optional": true
  }
  ```

## API Reference

### Input Topics

| Topic       | Type        | Description                                           |
| ----------- | ---------- | ----------------------------------------------------- |
| user_input  | any        | Placeholder, not used. Required for dataflow wiring.  |

### Output Topics

| Topic         | Type    | Description                                  |
| ------------- | ------- | --------------------------------------------- |
| aot_api_data  | dict    | Aggregated data from the Attack on Titan API. |

## License

Released under the MIT License.
