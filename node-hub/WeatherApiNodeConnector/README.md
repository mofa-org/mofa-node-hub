# weather_node_connector

Simple Dora-rs node for querying weather via GoWeather API.

A stateless node that receives a city name and outputs current weather data for Curitiba or Bern by querying the public GoWeather API.

## Features
- Query live weather data for Curitiba or Bern
- Graceful error handling for unsupported inputs or API failures
- Outputs machine-readable result (temperature, wind, description)

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
  - id: weather_node_connector
    build: pip install -e .
    path: weather_node_connector
    inputs:
      city_name: input/city_name
    outputs:
      - weather_result
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
  - id: city_source
    build: pip install your-city-node
    path: your-city-node
    outputs:
      - city_name

  - id: weather_node_connector
    build: pip install -e .
    path: weather_node_connector
    inputs:
      city_name: city_source/city_name
    outputs:
      - weather_result
```

Your point source must output:

* Topic: `city_name`
* Data: string (city name, e.g., "Curitiba" or "Bern")
* Metadata:

  ```json
  {
    "description": "City name string. Supported values: 'Curitiba', 'Bern'"
  }
  ```

## API Reference

### Input Topics

| Topic     | Type   | Description                                   |
|-----------|--------|-----------------------------------------------|
| city_name | string | Name of city to query ("Curitiba" or "Bern") |

### Output Topics

| Topic          | Type | Description                                                        |
|----------------|------|--------------------------------------------------------------------|
| weather_result | dict | Weather API response or {{ 'error': 'error message' }} on failure  |


## License

Released under the MIT License.
