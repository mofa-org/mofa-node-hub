# public_holiday_api_node

Retrieve Public Holidays via Nager.Date API

## Features
- Fetches public holidays for a given year and country code
- Robust error reporting (invalid inputs, API errors)
- Customizable via agent parameters

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
  - id: public_holiday_api_node
    build: pip install -e public_holiday_api_node
    path: public_holiday_api_node
    inputs:
      parameters: input/parameters
    outputs:
      - holidays
      - error
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
  - id: parameter_source
    build: pip install your-parameter-source
    path: your-parameter-source
    outputs:
      - parameters

  - id: public_holiday_api_node
    build: pip install -e public_holiday_api_node
    path: public_holiday_api_node
    inputs:
      parameters: parameter_source/parameters
    outputs:
      - holidays
      - error
```

Your point source must output:

* Topic: `parameters`
* Data: Dict of parameters including 'year' (string/int) and 'country' (string, ISO country code)
* Metadata:

  ```json
  {
    "required": ["year", "country"],
    "examples": {"year": "2024", "country": "CH"}
  }
  ```

## API Reference

### Input Topics

| Topic      | Type        | Description                         |
| ---------- | ----------- | ----------------------------------- |
| parameters | dict        | Dict with 'year' and 'country' keys |

### Output Topics

| Topic    | Type        | Description                 |
| -------- | ----------- | --------------------------- |
| holidays | list/dict   | Public holiday data (API)   |
| error    | str         | Error message (if any)      |


## License

Released under the MIT License.
