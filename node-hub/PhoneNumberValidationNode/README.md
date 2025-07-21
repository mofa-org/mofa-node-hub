# phone_number_validator

A stateless Dora-rs node for phone number validation using NumLookupAPI. This node receives a phone number, validates it against NumLookupAPI, and outputs the full validation response or descriptive error information. Designed for seamless integration as a validation module in your Dora flow.

## Features
- Stateless phone number validation via NumLookupAPI
- Robust error handling and informative outputs
- Easy environment variable configuration for API credentials

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
  - id: phone_validator
    build: pip install -e .
    path: phone_number_validator
    inputs:
      phone_number: input/phone_number
      user_input: input/user_input
    outputs:
      - validation_result
    env:
      NUMLOOKUP_API_KEY: "YOUR_API_KEY_HERE"
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
  - id: your_input_source
    build: pip install your-node
    path: your-node
    outputs:
      - phone_number
      - user_input

  - id: phone_validator
    build: pip install -e .
    path: phone_number_validator
    inputs:
      phone_number: your_input_source/phone_number
      user_input: your_input_source/user_input
    outputs:
      - validation_result
```

Your point source must output:

* Topic: `phone_number`
* Data: String containing the phone number to validate (e.g., "+8801812345678")
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Phone number to be validated"
  }
  ```

## API Reference

### Input Topics

| Topic          | Type   | Description                                              |
| --------------| ------ | -------------------------------------------------------- |
| phone_number   | string | Phone number in string format to be validated            |
| user_input    | any    | Placeholder for upstream compatibility (not processed)   |

### Output Topics

| Topic             | Type    | Description                                                        |
| ---------------- | ------- | ------------------------------------------------------------------ |
| validation_result | object  | Validation result or error info. Success flagged with 'success'.   |

## License

Released under the MIT License.
