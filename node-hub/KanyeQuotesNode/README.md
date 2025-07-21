# kanye_quotes_node

Retrieve Kanye West quotes via the [kanye.rest](https://kanye.rest/) API and output them through the MOFA agent node interface. This node can be integrated into workflows needing dynamic, inspirational, or humorous Kanye quotes, with robust error handling for API failures.

## Features
- Fetches random Kanye West quotes from the public API
- Handles network and API errors gracefully
- Compatible MOFA agent for easy downstream integration

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
  - id: kanye_quotes_node
    build: pip install -e .
    path: kanye_quotes_node
    inputs:
      user_input: input/user_input
    outputs:
      - kanye_quote
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
    build: pip install your-node
    path: user_input_node
    outputs:
      - user_input
  - id: kanye_quotes_node
    build: pip install -e .
    path: kanye_quotes_node
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - kanye_quote
```

Your point source must output:

* Topic: `user_input`
* Data: String, user request or prompt (not required by this node, but may be used for orchestration)
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "User request or prompt (not required by this node)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                           |
| ----------- | ------ | ------------------------------------- |
| user_input  | string | (Optional) User triggering or control |

### Output Topics

| Topic        | Type   | Description                              |
| ------------ | ------ | ---------------------------------------- |
| kanye_quote  | string | The latest Kanye West quote or error msg |


## License

Released under the MIT License.
