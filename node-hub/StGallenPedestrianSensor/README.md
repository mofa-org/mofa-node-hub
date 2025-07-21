# stgallen_pedestrian_sensor

A Dora-rs node that fetches recent pedestrian count records from St. Gallen’s Vadianstrasse pedestrian sensor public dataset (via HTTP GET). The node outputs the latest observation batch as JSON for use in other nodes or pipelines.

## Features
- Retrieves live pedestrian counts via HTTP from Stadt St.Gallen’s open data API
- Simple integration with Dora; output easily consumed downstream
- Robust error handling and JSON serialization

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
  - id: stgallen-pedestrian
    build: pip install -e .
    path: stgallen_pedestrian_sensor
    inputs:
      user_input: input/user_input
    outputs:
      - pedestrian_data
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
  - id: stgallen-pedestrian
    build: pip install -e .
    path: stgallen_pedestrian_sensor
    inputs:
      user_input: input/user_input
    outputs:
      - pedestrian_data
  - id: process-data
    path: your_processing_node
    inputs:
      pedestrian_data: stgallen-pedestrian/pedestrian_data
    outputs:
      - result
```

Your point source must output:

* Topic: `pedestrian_data`
* Data: JSON containing St. Gallen pedestrian sensor data or error message
* Metadata:

  ```json
  {
    "content_type": "application/json",
    "endpoint": "https://daten.stadt.sg.ch/api/explore/v2.1/catalog/datasets/fussganger-stgaller-innenstadt-vadianstrasse/records?order_by=datum_tag%20DESC&limit=20"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type               | Description                       |
| -------------| ------------------ | --------------------------------- |
| user_input    | any                | Placeholder for future extension  |

### Output Topics

| Topic             | Type   | Description                                             |
| ----------------- | ------ | ------------------------------------------------------- |
| pedestrian_data   | json   | 20 latest St. Gallen Vadianstrasse pedestrian records, or error info |


## License

Released under the MIT License.
