# insult_generator_node

A Dora-rs node that provides humorous or silly insults on-demand by calling the evilinsult.com API. Supports language and response format configuration and can be used in stateless, composable pipelines. 

## Features
- On-demand insult generation via evilinsult.com API
- Optional language and response type override via parameters
- Error reporting as a dedicated output

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
  - id: insult_generator
    build: pip install -e insult_generator_node
    path: insult_generator_node
    inputs:
      user_input: input/user_input
      lang: input/lang  # Optional, may omit for default
      type: input/type  # Optional, may omit for default
    outputs:
      - insult
      - insult_error
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
  - id: input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input
      - lang      # optional
      - type      # optional

  - id: insult_generator
    build: pip install -e insult_generator_node
    path: insult_generator_node
    inputs:
      user_input: input_node/user_input
      lang: input_node/lang  # optional
      type: input_node/type  # optional
    outputs:
      - insult
      - insult_error
```

Your point source must output:

* Topic: `user_input`
* Data: String (any value, can be a trigger)
* Metadata:

  ```json
  {
    "description": "Any input to trigger insult generation, value is ignored"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | str    | Any value to trigger insult generation       |
| lang        | str    | (Optional) Language code, e.g. `en`, `es`    |
| type        | str    | (Optional) Response format, `json` or `text` |

### Output Topics

| Topic        | Type   | Description                                |
| ------------ | ------ | ------------------------------------------ |
| insult       | any    | Insult from evilinsult.com (str or object) |
| insult_error | str    | Error details if generation fails          |

## License

Released under the MIT License.
