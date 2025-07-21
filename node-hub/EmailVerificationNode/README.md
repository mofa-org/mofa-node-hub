# email_verification_node

Email verification node for Dora-rs pipelines

## Features
- Real-time verification of email addresses via public API
- Error reporting and input validation
- Seamless integration with Dora-rs/MofaAgent workflows

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
  - id: email_verification_node
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input
    outputs:
      - api_verification_result
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
    build: pip install your-node
    path: your-node-path
    outputs:
      - user_input
  - id: email_verification_node
    build: pip install -e .
    path: .
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - api_verification_result
```

Your point source must output:

* Topic: `user_input`
* Data: String containing email address
* Metadata:

  ```json
  {
    "description": "User email address to verify",
    "type": "string"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description             |
| ---------- | ------ | ----------------------- |
| user_input | string | Email address to verify |

### Output Topics

| Topic                  | Type    | Description                                              |
| ---------------------- | ------- | -------------------------------------------------------- |
| api_verification_result| object  | API result for email verification or error info (dict)   |

## License

Released under the MIT License.