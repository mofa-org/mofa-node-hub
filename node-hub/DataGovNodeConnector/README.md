# data_gov_connector

Query US Data.gov endpoints and relay search and group listings through a Dora-rs node interface.

## Features
- Fetches latest dataset listings from Data.gov
- Retrieves group metadata from Data.gov
- Outputs full JSON from the API, ready for downstream nodes

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
  - id: data_gov_connector
    build: pip install -e .
    path: .
    outputs:
      - data_gov_results
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
  - id: point_source
    outputs:
      - data_gov_user_input
  - id: data_gov_connector
    inputs:
      user_input: point_source/data_gov_user_input
    outputs:
      - data_gov_results
```

Your point source must output:

* Topic: `user_input`
* Data: Any (placeholder, interaction trigger)
* Metadata:

  ```json
  {
    "description": "Can be any type; serves to trigger Data.gov fetch."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                 |
| ---------- | ------ | -------------------------- |
| user_input | any    | (Optional) triggers fetch. |

### Output Topics

| Topic             | Type                 | Description                                  |
| ----------------- | ------------------- | -------------------------------------------- |
| data_gov_results  | dict (JSON-serial.) | Search and group result from Data.gov (JSON) |


## License

Released under the MIT License.
