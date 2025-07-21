# ice_and_fire_node

Fetches Game of Thrones API Data as a Dora-rs Node

## Features
- Retrieves character details from the An API of Ice and Fire
- Retrieves house details for a specified character
- Automatic retry and error handling on API requests

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
  - id: ice_and_fire_node
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input
    outputs:
      - character_details
      - house_details
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
    build: pip install your_input_node
    path: your_input_node
    outputs:
      - user_input
  - id: ice_and_fire_node
    build: pip install -e .
    path: .
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - character_details
      - house_details
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (used for chaining; not processed)
* Metadata:

  ```json
  {
    "description": "Dummy input for triggering node execution"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                         |
| ----------|--------|-------------------------------------|
| user_input | Any    | Dummy input to trigger processing   |

### Output Topics

| Topic             | Type    | Description                                    |
| -----------------|---------|------------------------------------------------|
| character_details | Dict    | JSON with details of character 581 (Jon Snow)  |
| house_details     | Dict    | JSON with details of House Stark (id 378)      |


## License

Released under the MIT License.
