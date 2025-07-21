# foodbank_api_node

A Dora-rs node for programmatic access to UK food bank information using the GiveFood API. Query food banks by postcode/address or retrieve the full list, all via a unified node interface.

## Features
- Lookup nearby food banks by address or postcode
- Retrieve a list of all food bank organisations in the UK
- Structured error handling for bad input and API failures

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
  - id: foodbank_api_node
    build: pip install -e .
    path: foodbank_api_node
    inputs:
      parameter: input/action_or_address
    outputs:
      - foodbank_output
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
    build: pip install your-messaging-node
    path: your-messaging-node
    outputs:
      - action_or_address

  - id: foodbank_api_node
    build: pip install -e .
    path: foodbank_api_node
    inputs:
      parameter: your_input_node/action_or_address
    outputs:
      - foodbank_output

  - id: your_output_node
    build: pip install your-consumer-node
    path: your-consumer-node
    inputs:
      foodbank_output: foodbank_api_node/foodbank_output
```

Your point source must output:

* Topic: `action_or_address`
* Data: Dictionary with `action` ("search" or "list") and `address` (for "search") as string
* Metadata:

  ```json
  {
    "fields": [
      {"name": "action", "type": "str"},
      {"name": "address", "type": "str"}
    ],
    "required": ["action"]
  }
  ```

## API Reference

### Input Topics

| Topic    | Type       | Description                                  |
|----------|------------|----------------------------------------------|
| parameter| dict(str)  | Parameters: 'action' (search/list), and 'address' (required if action==search) |

### Output Topics

| Topic           | Type     | Description                  |
|-----------------|----------|------------------------------|
| foodbank_output | dict     | API result as JSON (list of foodbanks or search results, or error) |

## License

Released under the MIT License.
