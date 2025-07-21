# is_even_number_checker

A Dora-rs node that queries whether a given number is even using the public isevenapi.xyz REST API. Receives the input as a string, validates it as an integer, and returns the API result, including error details if input or requests fail.

## Features
- Stateless string-to-integer user input validation
- Calls the isevenapi.xyz REST endpoint with configurable number
- Robust error handling for input and API/network issues

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
  - id: is_even_checker
    build: pip install -e is_even_number_checker
    path: is_even_number_checker
    inputs:
      user_input: input/user_input
    outputs:
      - is_even_api_response
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
  - id: user_text_node
    build: pip install your-user-input-node
    path: your-user-input-node
    outputs:
      - user_input

  - id: is_even_checker
    build: pip install -e is_even_number_checker
    path: is_even_number_checker
    inputs:
      user_input: user_text_node/user_input
    outputs:
      - is_even_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: String representing the integer query
* Metadata:

  ```json
  {
    "type": "string",
    "description": "A number in string format"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description               |
| ----------- | ------ | ------------------------- |
| user_input  | string | Number as string to check |

### Output Topics

| Topic                 | Type         | Description                                           |
| --------------------- | ------------ | ----------------------------------------------------- |
| is_even_api_response  | dict (JSON)  | JSON with API result, including error keys if any     |


## License

Released under the MIT License.
