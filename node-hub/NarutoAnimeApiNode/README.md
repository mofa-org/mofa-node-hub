# naruto_api_node

Naruto API Dora Node: Fetch Villages, Teams, and Characters

## Features
- Fetches all villages from the Naruto anime API
- Retrieves team information from NarutoDB
- Gets a full list of Naruto characters

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
  - id: naruto_api_node
    build: pip install -e .
    path: naruto_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - naruto_api_outputs
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
  - id: user_node  # Source node
    build: pip install your-user-node
    path: your-user-node
    outputs:
      - user_input

  - id: naruto_api_node
    build: pip install -e .
    path: naruto_api_node
    inputs:
      user_input: user_node/user_input
    outputs:
      - naruto_api_outputs
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (used for chaining, actual content is ignored)
* Metadata:

  ```json
  {
    "required": false,
    "description": "Placeholder for workflow chaining/trigger."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                  |
| ----------- | ------ | ---------------------------- |
| user_input  | any    | Used to trigger the workflow |

### Output Topics

| Topic               | Type         | Description                               |
| ------------------- | ------------ | ----------------------------------------- |
| naruto_api_outputs  | dict         | All endpoint results and error messages   |

## License

Released under the MIT License.
