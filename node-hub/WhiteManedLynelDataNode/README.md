# white_maned_lynel_node

Fetches White-Maned Lynel data from the Breath of the Wild Compendium API and outputs a structured JSON result suitable for integration in a Dora-rs graph.

## Features
- Fetches detailed data for the "White-Maned Lynel" from a public botw-compendium API
- Robust error handling with descriptive output on request failures
- Simple Dora parameter-to-output agent structure for plug-and-play graph integration

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
  - id: white_maned_lynel_node
    build: pip install -e .
    path: white_maned_lynel_node
    inputs:
      user_input: input/user_input
    outputs:
      - white_maned_lynel_data
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
  - id: some_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input

  - id: white_maned_lynel_node
    build: pip install -e .
    path: white_maned_lynel_node
    inputs:
      user_input: some_input_node/user_input
    outputs:
      - white_maned_lynel_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable input; can be an empty dict `{}`
* Metadata:

  ```json
  {
    "description": "Any input to facilitate graph connectivity. No required fields."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type                   | Description                                                |
| ----------- | ---------------------- | ---------------------------------------------------------- |
| user_input  | Any serializable object| Dummy or real parameter to trigger the API data retrieval. |

### Output Topics

| Topic                | Type      | Description                                   |
| -------------------- | --------- | --------------------------------------------- |
| white_maned_lynel_data | JSON dict | BotW Compendium API result for the Lynel, or errors. |


## License

Released under the MIT License.
