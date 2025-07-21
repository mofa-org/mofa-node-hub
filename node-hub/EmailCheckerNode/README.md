# EmailCheckerNode

A Dora-rs node for checking whether an email address is a temporary or disposable address via the UserCheck API. Makes it easy for other nodes to verify the legitimacy of email addresses in data pipelines or interactive workflows.

## Features
- Checks if an email is a temporary (disposable) address via API
- Accepts email and timeout as configurable input parameters
- Structured output with email status and error handling

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
  - id: email_checker
    build: pip install -e .
    path: email_checker_node
    inputs:
      user_input: input/user_input
    outputs:
      - email_check_result
    env:
      USERCHECK_API_ENDPOINT: "https://api.usercheck.com/email/"    # optional, can set your own endpoint
      EMAILCHECKER_DEFAULT_EMAIL: "hello@freepublicapis.com"         # optional, email to check if none supplied
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
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input

  - id: email_checker
    build: pip install -e .
    path: email_checker_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - email_check_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any type (not used; serves as a tick/trigger for compatibility)
* Metadata:

  ```json
  {
    "type": "trigger"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                               |
| ----------- | ------- | ----------------------------------------- |
| user_input  | any     | Required dummy input to trigger execution |
| email       | string  | Optional parameter, email to check        |
| timeout     | int     | Optional parameter, request timeout (sec) |

### Output Topics

| Topic               | Type   | Description                                             |
| ------------------- | ------ | ------------------------------------------------------- |
| email_check_result  | dict   | Result from UserCheck API with status/error info         |


## License

Released under the MIT License.
