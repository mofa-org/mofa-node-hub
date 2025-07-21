# swissquote_forex_node

Swissquote Forex Quotes Node for Dora

## Features
- Fetches real-time forex quotes for XAU/USD (Gold) and EUR/USD currency pairs from Swissquote
- Handles error reporting per endpoint for robust integration
- Simple integration with Dora-MOFA agent messaging interface

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
  - id: swissquote_forex_node
    build: pip install -e .
    path: swissquote_forex_node
    inputs:
      user_input: input/user_input
    outputs:
      - forex_quotes
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
  - id: my_point_source
    build: pip install my-point-source
    path: my_point_source
    outputs:
      - user_input

  - id: swissquote_forex_node
    build: pip install -e .
    path: swissquote_forex_node
    inputs:
      user_input: my_point_source/user_input
    outputs:
      - forex_quotes
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable Python object (optional for triggering a fetch)
* Metadata:

  ```json
  {
    "description": "Optional triggering parameter. Content is forwarded as context if needed."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type                  | Description                             |
| ----------- | --------------------- | --------------------------------------- |
| user_input  | Any serializable type | Triggers the fetch of forex quote data. |

### Output Topics

| Topic        | Type           | Description                                            |
| ------------ | --------------| ------------------------------------------------------ |
| forex_quotes | List[Dict]     | List of responses/errors from Swissquote endpoints.    |

## License

Released under the MIT License.
