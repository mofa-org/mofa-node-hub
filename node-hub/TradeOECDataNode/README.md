# trade_oec_node

Agent-based Dora-rs node for fetching international trade data from the OEC (Observatory of Economic Complexity) public API with flexible query configuration. Suited for analytical data workflows and fast integration into Dora-based pipelines.

## Features
- Fetch trade data by year, country, and commodity granularity
- Customizable drilldowns, measures, and sorting for API results
- Structured error reporting and robust parameter handling

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
  - id: oec_fetcher
    build: pip install -e trade_oec_node
    path: trade_oec_node
    inputs:
      parameters: input/parameters
    outputs:
      - trade_data
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
  - id: my_param_source
    build: pip install your-param-source
    path: your-param-source
    outputs:
      - parameters
  - id: oec_fetcher
    build: pip install -e trade_oec_node
    path: trade_oec_node
    inputs:
      parameters: my_param_source/parameters
    outputs:
      - trade_data
```

Your point source must output:

* Topic: `parameters`
* Data: Dict with keys matching field list below (any subset, must contain `year`)
* Metadata:

  ```json
  {
    "fields": ["year", "exporter_country", "drilldowns", "cube", "measures", "sort", "properties", "locale"],
    "required": ["year"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                               |
|------------|--------|-----------------------------------------------------------|
| parameters | dict   | Configuration parameters for OEC data fetch (see fields)  |

### Output Topics

| Topic      | Type   | Description                                               |
|------------|--------|-----------------------------------------------------------|
| trade_data | dict   | OEC API response data or error message                    |


## License

Released under the MIT License.
