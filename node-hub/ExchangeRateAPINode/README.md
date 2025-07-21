# exchange_rate_api_node

Query real-time USD exchange rates via the open.er-api.com API from a Dora node.

## Features
- Fetches latest exchange rates for USD against all available currencies
- Integrates as a Dora node parameterized by `user_input` (optional)
- Robust error handling, always yields a structured output

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
  - id: exchange_rate_api_node
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input  # Optional parameter; can be left disconnected
    outputs:
      - exchange_rate_data
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
  - id: my_scenario
    # ... other config
    outputs:
      - user_input
  - id: exchange_rate_api_node
    build: pip install -e .
    path: .
    inputs:
      user_input: my_scenario/user_input
    outputs:
      - exchange_rate_data
  - id: downstream_consumer
    inputs:
      exchange_rates: exchange_rate_api_node/exchange_rate_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (unused, serves as a trigger)
* Metadata:

  ```json
  {
    "description": "Unused. Included for interface consistency."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                                 |
| ----------|---------|---------------------------------------------|
| user_input | Any     | (Optional) Triggers the API call; unused.   |

### Output Topics

| Topic               | Type            | Description                                        |
|---------------------|-----------------|----------------------------------------------------|
| exchange_rate_data  | dict (JSON)     | Result from https://open.er-api.com/v6/latest/USD. |
|                     |                 | On error, contains keys `error` and `message`.     |


## License

Released under the MIT License.
