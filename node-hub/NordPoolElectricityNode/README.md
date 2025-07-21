# nordpool_electricity_node

Fetch Nord Pool Spot Electricity Prices via Elering API (Dora-rs Compatible)

## Features
- Query current electricity price for Estonia from Elering API with a simple mode switch
- Fetch price data for a date range using start and end parameters
- Robust error handling with informative messages sent to output topic

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
  - id: nordpool
    path: nordpool_electricity_node
    build: pip install -e nordpool_electricity_node
    inputs:
      user_input: input/user_input
      mode: input/mode
      start: input/start   # required for range mode
      end: input/end       # required for range mode
    outputs:
      - electricity_price
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
  - id: my_input
    path: my-input-node
    build: pip install -e my-input-node
    outputs:
      - user_input
      - mode
      - start
      - end

  - id: nordpool
    path: nordpool_electricity_node
    build: pip install -e nordpool_electricity_node
    inputs:
      user_input: my_input/user_input
      mode: my_input/mode
      start: my_input/start
      end: my_input/end
    outputs:
      - electricity_price
```

Your point source must output:

* Topic: `mode`, `user_input`, and optionally `start`, `end`
* Data: For `mode`, send `'current'` or `'range'` as string. For `start` and `end`, send timestamps in ISO8601 string format
* Metadata:

  ```json
  {
    "mode": "current|range", 
    "start": "YYYY-MM-DDTHH:MM:SSZ", 
    "end": "YYYY-MM-DDTHH:MM:SSZ"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                               |
| ------------| ------ | ---------------------------------------------------------|
| user_input   | str    | Additional user input (not used for API query)           |
| mode        | str    | 'current' for latest price, 'range' for ranged query     |
| start       | str    | Start time in ISO8601 (only for 'range' mode)            |
| end         | str    | End time in ISO8601 (only for 'range' mode)              |

### Output Topics

| Topic              | Type  | Description                                         |
| ------------------ | ----- | ---------------------------------------------------|
| electricity_price  | dict  | Dictionary of prices or error message if something fails |


## License

Released under the MIT License.
