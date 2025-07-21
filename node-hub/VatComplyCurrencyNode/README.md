# vatcomply_node

A Dora-rs node for real-time currency exchange, VAT validation, and country geolocation leveraging the [VATComply](https://www.vatcomply.com/api/) public API. Provides programmatic access to current and historical FX rates, supported currencies, VAT number validation, and quick country geolocation via simple Dora pipeline integration.

## Features
- Query live and historical exchange rates
- Validate VAT numbers and geolocate by IP in real time
- Retrieve full currency and country code information

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
  - id: currency_node
    build: pip install -e .
    path: vatcomply_node
    inputs:
      action: input/action
      base: input/base
      date: input/date
      vat_number: input/vat_number
    outputs:
      - vatcomply_response
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
  - id: fx_query
    build: pip install my-fx-task
    path: my-fx-task
    outputs:
      - action
      - base
      - date
  - id: currency_node
    build: pip install -e .
    path: vatcomply_node
    inputs:
      action: fx_query/action
      base: fx_query/base
      date: fx_query/date
    outputs:
      - vatcomply_response
```

Your point source must output:

* Topic: `action`
* Data: String indicating operation (e.g., 'rates', 'base_rates', 'historical_rates', 'currencies', 'vat', or 'geolocate')
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Operation to request from vatcomply_node. One of: rates, base_rates, historical_rates, currencies, vat, geolocate."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                          |
| ------------|--------|----------------------------------------------------------------------|
| action      | string | Operation to request: 'rates', 'base_rates', 'currencies', 'historical_rates', 'vat', 'geolocate' |
| base        | string | Currency (e.g., USD, EUR) for base_rates; ignored otherwise          |
| date        | string | Date in format YYYY-MM-DD for historical_rates operation; optional   |
| vat_number  | string | VAT number for validation; used only for 'vat' operation             |

### Output Topics

| Topic                | Type    | Description                         |
|----------------------|---------|-------------------------------------|
| vatcomply_response   | object  | Response from VATComply API in JSON |


## License

Released under the MIT License.
