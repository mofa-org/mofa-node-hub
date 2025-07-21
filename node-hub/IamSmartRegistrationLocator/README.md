# iam_smart_locator

Locate All iAM Smart Registration Points in Hong Kong via Open Data

## Features
- Downloads all iAM Smart public Hong Kong registration service data endpoints
- Aggregates results from multiple official datasets into a single output
- Robust error reporting and returns for each data source

## Getting Started

### Installation
Install via pip:
```bash
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: iam_smart_locator
    build: pip install -e .
    path: iam_smart_locator
    inputs:
      user_input: input/user_input
    outputs:
      - registration_data
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
  - id: my_entry_point
    build: pip install my-entry-point
    path: my-entry-point
    outputs:
      - user_input
  - id: iam_smart_locator
    build: pip install -e .
    path: iam_smart_locator
    inputs:
      user_input: my_entry_point/user_input
    outputs:
      - registration_data
```

Your point source must output:

* Topic: `user_input`
* Data: None (input just triggers fetch)
* Metadata:

  ```json
  {
    "description": "Trigger for iAM Smart registration data fetch, contents ignored."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                                           |
| ----------| --------- | -----------------------------------------------------|
| user_input | Any/None  | Triggers fetch and aggregation of the data sources    |

### Output Topics

| Topic             | Type   | Description                                                     |
| ----------------- | ------ | ---------------------------------------------------------------|
| registration_data | dict   | Aggregated dataset: endpoint URLs as keys, JSON/result as value |

## License

Released under the MIT License.
