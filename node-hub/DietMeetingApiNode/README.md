# diet_meeting_api

A Dora node to fetch Japanese National Diet meeting records from kokkai.ndl.go.jp via API. This node simplifies RESTful requests to retrieve National Diet session data based on flexible search parameters, outputting structured JSON.

## Features
- Access Japanese Diet (parliament) meeting records using official API
- Flexible search via configurable parameters (meeting name, max records, result format)
- JSON output for seamless integration with other nodes

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
  - id: diet_meeting_api
    build: pip install -e .
    path: diet_meeting_api
    inputs:
      parameters: input/parameters
    outputs:
      - diet_meeting_records
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
  - id: your_point_source
    build: pip install your-point-source
    path: your-point-source
    outputs:
      - parameters

  - id: diet_meeting_api
    build: pip install -e .
    path: diet_meeting_api
    inputs:
      parameters: your_point_source/parameters
    outputs:
      - diet_meeting_records
```

Your point source must output:

* Topic: `parameters`
* Data: Parameter dict as JSON
* Metadata:

  ```json
  {
    "fields": ["name_of_meeting", "maximum_records", "record_packing"],
    "description": "Parameters for National Diet meeting API."
  }
  ```

## API Reference

### Input Topics

| Topic             | Type     | Description                             |
| ---------------- | -------- | --------------------------------------- |
| parameters       | object   | Search parameters (meeting name, max records, result format) |

### Output Topics

| Topic               | Type    | Description                                  |
| ------------------ | ------- | -------------------------------------------- |
| diet_meeting_records | object | JSON with API query results or error message |

## License

Released under the MIT License.
