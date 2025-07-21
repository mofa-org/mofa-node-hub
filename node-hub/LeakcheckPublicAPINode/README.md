# leakcheck_api_node

Check emails, usernames, or phone numbers against the LeakCheck public API via a Dora-rs node agent.

## Features
- Query the LeakCheck public API for data breach exposure
- Flexible input parameter: check user input or values from upstream nodes
- Clear error/status reporting via output topics

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
  - id: leakcheck
    build: pip install -e leakcheck_api_node
    path: leakcheck_api_node
    inputs:
      user_input: input/user_input
      check: input/check
    outputs:
      - leakcheck_api_response
      - leakcheck_api_error
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
  - id: your_source
    build: pip install your-node
    path: your-source-node
    outputs:
      - user_input
      - check
  - id: leakcheck
    build: pip install -e leakcheck_api_node
    path: leakcheck_api_node
    inputs:
      user_input: your_source/user_input
      check: your_source/check
    outputs:
      - leakcheck_api_response
      - leakcheck_api_error
```

Your point source must output:

* Topic: `user_input` or `check`
* Data: String value (the email, username, or phone number to check)
* Metadata:

  ```json
  {
    "dtype": "string"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                          |
| ----------| ------ | ------------------------------------ |
| user_input| string | Email, username, or phone number     |
| check     | string | Value to check (email/login/phone); will fallback to `user_input` if not provided |

### Output Topics

| Topic                  | Type                | Description                     |
| ---------------------- | ------------------- | ------------------------------- |
| leakcheck_api_response | dict or list/string | API response from LeakCheck     |
| leakcheck_api_error    | dict                | Error or status message         |


## License

Released under the MIT License.
