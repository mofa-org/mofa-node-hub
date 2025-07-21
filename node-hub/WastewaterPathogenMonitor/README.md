# wastewater_pathogen_monitor

Monitor SARS-CoV-2 and Influenza A in Wastewater

## Features
- Fetch latest SARS-CoV-2 gene copy and case data from public API
- Fetch latest Influenza A gene copy and case data from public API
- Flexible query: select SARS-CoV-2, Influenza A, or both via parameter

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
  - id: pathogen_monitor
    build: pip install -e .
    path: wastewater_pathogen_monitor
    inputs:
      pathogen_type: input/pathogen_type
    outputs:
      - wastewater_pathogen_results
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
  - id: your_source
    build: pip install your-node
    path: your_node_path
    outputs:
      - pathogen_type

  - id: pathogen_monitor
    build: pip install -e .
    path: wastewater_pathogen_monitor
    inputs:
      pathogen_type: your_source/pathogen_type
    outputs:
      - wastewater_pathogen_results
```

Your point source must output:

* Topic: `pathogen_type`
* Data: String indicating "sars-cov-2", "influenza-a", or empty for both
* Metadata:

  ```json
  {
    "description": "Pathogen type to fetch ('sars-cov-2', 'influenza-a', or empty/all)",
    "examples": ["sars-cov-2", "influenza-a", ""]
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                  |
| ---------------|--------|----------------------------------------------|
| pathogen_type   | str    | Which pathogen to query ('sars-cov-2', 'influenza-a', or empty/all)	|

### Output Topics

| Topic                       | Type  | Description                                                    |
|-----------------------------|-------|----------------------------------------------------------------|
| wastewater_pathogen_results | dict  | Dictionary keyed by pathogen name with endpoint response JSON data or error info |

## License

Released under the MIT License.
