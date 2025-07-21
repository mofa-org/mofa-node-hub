# ai_pollinations_node

Access Pollinations Free AI Text Generator from Dora-rs

## Features
- Seamless integration with Pollinations Free AI Text API
- Simple Dora-rs compatible parameter input (user_input)
- Robust error-handling with clear diagnostics

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
  - id: ai_text_generator
    build: pip install -e ai_pollinations_node
    path: ai_pollinations_node
    inputs:
      user_input: input/user_input
    outputs:
      - ai_text_output
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
  # Your parameter source node
  - id: param_source
    build: pip install <your_param_node>
    path: <your_param_node>
    outputs:
      - user_input

  # Pollinations text generator node
  - id: ai_text_generator
    build: pip install -e ai_pollinations_node
    path: ai_pollinations_node
    inputs:
      user_input: param_source/user_input
    outputs:
      - ai_text_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (required for dataflow consistency, but not used by Pollinations API)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Any string placeholder for user input (not processed by Pollinations endpoint)"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                |
| ----------- | ------ | ---------------------------------------------------------- |
| user_input  | str    | Any input string. Used for dataflow consistency only.      |

### Output Topics

| Topic          | Type   | Description                                        |
| -------------- | ------ | --------------------------------------------------- |
| ai_text_output | str or dict | AI-generated text as string, or error diagnostics |


## License

Released under the MIT License.
