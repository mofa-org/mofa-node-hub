# leakcheck_userinfo

Check if an email has been part of a data breach using the Leakcheck API. Provides a Dora node interface for programmatically checking email addresses in dataflows.

## Features
- Query [Leakcheck.net Public API](https://leakcheck.net/) for email data breach checks
- Structured error handling with serializable responses
- Integrates as a MofaAgent compatible Dora node

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
  - id: leakcheck_userinfo
    build: pip install -e leakcheck_userinfo
    path: leakcheck_userinfo
    inputs:
      email: input/email
    outputs:
      - leakcheck_result
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
  - id: email_generator
    build: pip install -e your-email-generator
    path: your-email-generator
    outputs:
      - email

  - id: leakcheck_userinfo
    build: pip install -e leakcheck_userinfo
    path: leakcheck_userinfo
    inputs:
      email: email_generator/email
    outputs:
      - leakcheck_result
```

Your point source must output:

* Topic: `email`
* Data: string email address
* Metadata:

  ```json
  {
    "dtype": "string"
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                        |
| ------- | ------ | ---------------------------------- |
| email   | string | Email address to be checked        |

### Output Topics

| Topic             | Type   | Description                                  |
| ----------------- | ------ | -------------------------------------------- |
| leakcheck_result  | object | Result dictionary or error from Leakcheck API|

## License

Released under the MIT License.
