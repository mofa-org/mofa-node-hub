# currency_exchange_node

A Dora-rs node providing access to live currency exchange rates and conversions via the Unirate API. This node supports conversion, rate lookup, and listing available currencies, making it easy to add real-time global currency data to your agent or pipeline workflows.

## Features
- Real-time currency conversion between any supported pairs
- Retrieve live exchange rates for a specified base currency
- List all supported currencies from Unirate API

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
  - id: currency_exchange
    build: pip install -e .
    path: currency_exchange_node
    inputs:
      user_input: input/user_input
      action: input/action
      amount: input/amount # Required if action is 'convert'
      from: input/from
      to: input/to         # Required if action is 'convert'
    outputs:
      - currency_exchange_output
    env:
      UNIRATE_API_KEY: "<your_unirate_api_key>"
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
    build: pip install -e .
    path: your_input_node
    outputs:
      - action
      - user_input
      - from
      - to
      - amount

  - id: currency_exchange
    build: pip install -e .
    path: currency_exchange_node
    inputs:
      user_input: your_input_node/user_input
      action: your_input_node/action
      from: your_input_node/from
      to: your_input_node/to
      amount: your_input_node/amount
    outputs:
      - currency_exchange_output
```

Your point source must output:

* Topic: `user_input`, `action`, `from`, `to`, `amount`
* Data: As string (except amount, which should be numeric/parsable as float)
* Metadata:

  ```json
  {
    "required": [
      "user_input",
      "action",
      "from",
      "to",
      "amount"
    ],
    "notes": "'to' and 'amount' required only for 'convert' action. All fields are strings except 'amount'."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                           |
| ------------| ------ | --------------------------------------------------------------------- |
| user_input   | str    | Required by pipeline; not acted on directly, for node-linking         |
| action       | str    | One of: 'convert', 'rates', 'currencies'                              |
| amount       | float  | Amount to convert (required if action='convert')                      |
| from         | str    | Source currency code (e.g., 'USD')                                    |
| to           | str    | Destination currency code (required if action='convert')              |

### Output Topics

| Topic                     | Type      | Description                                                |
| ------------------------- | --------- | ---------------------------------------------------------- |
| currency_exchange_output  | dict/json | Result from Unirate API (conversion/rates/currencies data) |


## License

Released under the MIT License.
