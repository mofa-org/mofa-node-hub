# StGallenNewbornNamesNode

Query the official Kanton St. Gallen newborn names dataset via Dora for a given year and gender, returning the top names for that year.

## Features
- Query Swiss Open Data API for newborn names in St. Gallen
- Year and gender parameterized lookup
- Outputs structured name statistics per input query

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
  - id: stgallen_names
    build: pip install -e .
    path: stgallen_names_node
    inputs:
      year: input/year
      gender: input/gender
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
  - id: year_gender_node
    build: pip install year-gender-input-node  # Replace with your input node
    path: year_gender_input_node
    outputs:
      - year
      - gender

  - id: stgallen_names
    build: pip install -e .
    path: stgallen_names_node
    inputs:
      year: year_gender_node/year
      gender: year_gender_node/gender
    outputs:
      - api_response
```

Your point source must output:

* Topic: `year`, `gender`
* Data: String values for year (e.g., "1991"), and gender ("1" for male, "2" for female)
* Metadata:

  ```json
  {
    "year": "1991",
    "gender": "1"
  }
  ```

## API Reference

### Input Topics

| Topic    | Type | Description                   |
|----------|------|-------------------------------|
| year     | str  | Birth year (e.g., '1991')     |
| gender   | str  | '1' for male, '2' for female  |

### Output Topics

| Topic        | Type      | Description                               |
|--------------|-----------|-------------------------------------------|
| api_response | dict/str  | API output or error message as dictionary |

## License

Released under the MIT License.
