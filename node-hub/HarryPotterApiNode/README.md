# harry_potter_node

Access the open Harry Potter API via a MOFA/Dora node

## Features
- Fetches the full spell list from the HP API
- Obtains all characters, staff members, and Ravenclaw students via REST endpoints
- Simple Dora-rs node, easy integration with parameter input/output

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
  - id: harry_potter_api
    build: pip install -e .
    path: harry_potter_node
    inputs:
      user_input: input/user_input
    outputs:
      - all_spells
      - ravenclaw_characters
      - staff_characters
      - all_characters
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
  - id: harry_potter_api
    build: pip install -e .
    path: harry_potter_node
    inputs:
      user_input: any/previous_output
    outputs:
      - all_spells
      - ravenclaw_characters
      - staff_characters
      - all_characters
```

Your point source must output:

* Topic: `user_input`
* Data: any serializable type, e.g. string (input is not strictly required but needed for Dora compatibility)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Dummy trigger parameter for agent sync"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                          |
| ----------| ------ | ------------------------------------ |
| user_input | string | Dummy input for agent sync/compliance |

### Output Topics

| Topic                 | Type      | Description                      |
| --------------------- | --------- | -------------------------------- |
| all_spells            | list/dict | All spells from HP API           |
| ravenclaw_characters  | list/dict | Ravenclaw students from HP API   |
| staff_characters      | list/dict | Staff characters from HP API     |
| all_characters        | list/dict | All characters from HP API       |

## License

Released under the MIT License.
