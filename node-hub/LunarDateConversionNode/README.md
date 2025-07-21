# lunar_date_node

Get Lunar Date Conversion via Hong Kong Observatory API

## Features
- Calls the Hong Kong Observatory open data lunar date API
- Receives a Gregorian date parameter and returns the lunar date as a response
- Robust error handling for missing/invalid input or API failure

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: lunar_date_node
    build: pip install -e .
    path: lunar_date_node
    inputs:
      date: input/date
    outputs:
      - lunar_date_response
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
  - id: source_node
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - date

  - id: lunar_date_node
    build: pip install -e .
    path: lunar_date_node
    inputs:
      date: source_node/date
    outputs:
      - lunar_date_response
```

Your point source must output:

* Topic: `date`
* Data: String (date in YYYY-MM-DD format)
* Metadata:

  ```json
  {
    "type": "string",
    "format": "YYYY-MM-DD",
    "description": "Gregorian date string to be converted to lunar date"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                         |
|-------|--------|-------------------------------------|
| date  | string | Gregorian date (format YYYY-MM-DD)  |

### Output Topics

| Topic                | Type | Description                           |
|----------------------|------|---------------------------------------|
| lunar_date_response  | dict | Lunar date API response or error info |

## License

Released under the MIT License.
