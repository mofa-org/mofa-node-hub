# restroom_locator

GenderNeutralRestroomLocator: Dora-rs node for retrieving public gender-neutral restroom locations using the Refuge Restrooms API.

## Features
- Retrieves a curated list of public gender-neutral restrooms via REST API
- Handles API errors gracefully and reports them in output
- Simple integration as an informational data source node in pipelines

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
  - id: restroom_locator
    build: pip install -e .
    path: restroom_locator
    inputs:
      user_input: input/user_input
    outputs:
      - restroom_data
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
  - id: user_input_node
    build: pip install your-user-input-node
    path: your_user_input_node
    outputs:
      - user_input

  - id: restroom_locator
    build: pip install -e .
    path: restroom_locator
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - restroom_data
```

Your point source must output:

* Topic: `user_input`
* Data: None (can be empty or any string)
* Metadata:

  ```json
  {
    "description": "Trigger for retrieving restroom locations. Can be an empty event or string."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                     |
| ---------- | ------ | ----------------------------------------------- |
| user_input | any    | Input trigger (can be empty) to fetch restrooms |

### Output Topics

| Topic         | Type      | Description                                                    |
| ------------- | --------- | -------------------------------------------------------------- |
| restroom_data | list/dict | List of gender-neutral restroom locations, or error information |

## License

Released under the MIT License.
