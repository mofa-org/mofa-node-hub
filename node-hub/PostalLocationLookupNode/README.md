# postal_location_node

A Dora-rs node for fetching postal location information from the Zippopotam.us API for Switzerland (CH) and the United States (US).

## Features
- Fetches location details for predefined postal codes (CH-3007, US-90210) from Zippopotam.us.
- Aggregates responses and provides unified output.
- Accepts optional user-trigger input for compatibility with dynamic integration.

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
  - id: postal_location
    build: pip install -e .
    path: postal_location_node
    inputs:
      user_input: input/user_input
    outputs:
      - postal_location_outputs
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
  - id: custom_input
    build: pip install -e ./custom_input_node
    path: custom_input_node
    outputs:
      - user_input
  - id: postal_location
    build: pip install -e .
    path: postal_location_node
    inputs:
      user_input: custom_input/user_input
    outputs:
      - postal_location_outputs
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary trigger or request
* Metadata:

  ```json
  {"description": "Request trigger. Content can be any string or JSON to initiate a postal lookup."}
  ```

## API Reference

### Input Topics

| Topic        | Type         | Description                                      |
| ------------| ------------| ------------------------------------------------ |
| user_input  | Any/String   | Triggers the agent to fetch postal location data. |

### Output Topics

| Topic                    | Type     | Description                                        |
| ------------------------ | -------- | -------------------------------------------------- |
| postal_location_outputs  | dict     | Aggregated JSON responses by country or errors.     |

## License

Released under the MIT License.
