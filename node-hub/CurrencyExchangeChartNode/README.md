# currency_exchange_chart

A Dora node for retrieving and visualizing currency exchange rates and historical exchange charts using the Kekkai API. Supports a variety of query modes for single-day rates, time-series charts, and period-based lookups between arbitrary currencies.

## Features
- Retrieve currency exchange rate for a single day
- Create currency exchange rate charts for past week or specified periods
- Flexible support for specifying base/quote currencies and date ranges

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
  - id: currency_exchange_chart
    build: pip install -e .
    path: currency_exchange_chart
    inputs:
      parameters: input/parameters
    outputs:
      - api_response
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
  - id: my_parameters_generator
    build: pip install -e ./my-generator
    path: my-generator
    outputs:
      - parameters
  - id: currency_exchange_chart
    build: pip install -e .
    path: currency_exchange_chart
    inputs:
      parameters: my_parameters_generator/parameters
    outputs:
      - api_response
```

Your point source must output:

* Topic: `parameters`
* Data: Dictionary with parameters
* Metadata:

  ```json
  {
    "operation": "chart_week | chart_period | rate_day | rate_period",
    "from_currency": "RUB | (any supported base currency)",
    "conv_currency": "USD | (any supported quote currency)",
    "date": "YYYY-MM-DD",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type        | Description                                                          |
| ----------- | ----------- | -------------------------------------------------------------------- |
| parameters  | dict        | Parameters dict; see below for possible keys                          |

### Output Topics

| Topic         | Type                | Description                                              |
| ------------- | ------------------- | -------------------------------------------------------- |
| api_response  | dict or str         | API result (JSON dict, or error/string if applicable)    |


## License

Released under the MIT License.
