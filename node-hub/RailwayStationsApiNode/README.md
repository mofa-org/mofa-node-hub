# railway_stations_node

Multi-operation Dora node for railway-stations.org API queries

## Features
- Retrieve aggregated stats from railway-stations.org
- Query photo station summaries by country code
- Fetch all photos and info for a given station ID

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
  - id: railway_api
    build: pip install -e .
    path: railway_stations_node
    inputs:
      tick: dora/timer/millis/5000
    outputs:
      - api_response
    params:
      operation: stats
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
  - id: railway_api
    build: pip install -e .
    path: railway_stations_node
    inputs:
      trigger: your_point_source/out_topic
    outputs:
      - api_response
    params:
      operation: by_country
      country_code: de
```

Your point source must output:

* Topic: `operation_params`
* Data: Dict with the following keys (at least one set):
* Metadata:

  ```json
  {
    "operation": "stats | by_country | photos_by_id",  
    "country_code": "de" ,   // for by_country
    "station_id": "de/2513"  // for photos_by_id
  }
  ```

## API Reference

### Input Topics

| Topic             | Type        | Description                                                      |
| ---------------- | ----------- | --------------------------------------------------------------- |
| operation        | string      | API operation to perform: 'stats', 'by_country', 'photos_by_id' |
| country_code     | string      | (if by_country) Country to query, e.g. 'de', 'ch', 'fr'         |
| station_id       | string      | (if photos_by_id) Station id per railway-stations.org           |

### Output Topics

| Topic         | Type   | Description                                                         |
| -------------| ------ | ------------------------------------------------------------------- |
| api_response | dict   | API response object or error, as returned from railway-stations.org  |


## License

Released under the MIT License.
