# DisposableEmailVerifierNode

Check if a domain or email address is disposable using throwaway.cloud. This Dora node can be integrated into your dataflow to programmatically filter temporary email services.

## Features
- Detect and verify if an email domain is disposable
- Accept both full email addresses or bare domains
- Graceful error handling and clear result output

## Getting Started

### Installation
Install via pip:
```bash
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: disposable-email-node
    build: pip install -e .
    path: disposable_email_node
    inputs:
      domain: input/domain
      email: input/email
    outputs:
      - domain_check_result
      - email_check_result
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
  - id: my-input-node
    build: pip install -e my-input-node
    path: my_input_node
    outputs:
      - domain
      - email

  - id: disposable-email-node
    build: pip install -e .
    path: disposable_email_node
    inputs:
      domain: my-input-node/domain
      email: my-input-node/email
    outputs:
      - domain_check_result
      - email_check_result
```

Your point source must output:

* Topic: `domain` or `email`
* Data: String
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Input domain or email address to check for disposability. Either is accepted."
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                                |
| ------- | ------ | ------------------------------------------ |
| domain  | string | Domain name to check against disposable DB  |
| email   | string | Email address to check for disposability    |

### Output Topics

| Topic                | Type    | Description                                   |
| -------------------- | ------- | --------------------------------------------- |
| domain_check_result  | dict    | Result of domain disposability check          |
| email_check_result   | dict    | Result of email disposability check           |
| error                | dict    | Error output if neither input is provided     |


## License

Released under the MIT License.
