# shark_attack_node

Fetch worldwide shark attack records from the OpenDataSoft API, with optional filtering by month, for real-time integration with Dora-rs pipelines.

## Features
- Retrieve recent global shark attack incidents
- Filter by specific year/month via API query
- Structured Dora node output for flow integration

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
  - id: shark_attack_node
    build: pip install -e .
    path: shark_attack_node
    inputs:
      user_input: input/user_input
    outputs:
      - shark_attack_results
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
  - id: custom_input_node
    build: pip install your_input_node
    path: your_input_node
    outputs:
      - user_input

  - id: shark_attack_node
    build: pip install -e .
    path: shark_attack_node
    inputs:
      user_input: custom_input_node/user_input
    outputs:
      - shark_attack_results
```

Your point source must output:

* Topic: `user_input`
* Data: ISO month string, e.g. '2023/08' (for August 2023)
* Metadata:

  ```json
  {
    "dtype": "str",
    "example": "2023/08"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                       |
|-------------|--------|-----------------------------------|
| user_input  | str    | (Optional) Year/month ('YYYY/MM') |

### Output Topics

| Topic                 | Type   | Description                                   |
|-----------------------|--------|-----------------------------------------------|
| shark_attack_results  | dict   | List of API records or error message (dict)   |

## License

Released under the MIT License.
