# pollen_forecast_node

A Dora node to fetch real-time pollen forecast data for user-specified locations and types using the Open-Meteo API.

## Features
- Retrieve pollen and air-quality data from Open-Meteo for any latitude/longitude
- Select specific pollen types (e.g., grass, tree, weed) for hourly forecasts
- Graceful error handling and robust retry logic for network failures

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
  - id: pollen-forecast
    build: pip install -e pollen_forecast_node
    path: pollen_forecast_node
    inputs:
      latitude: input/latitude
      longitude: input/longitude
      hourly: input/hourly
    outputs:
      - pollen_forecast
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
  - id: my-coordinates
    build: pip install my-coords-source
    path: my-coords-source
    outputs:
      - latitude
      - longitude
      - hourly
  - id: pollen-forecast
    build: pip install -e pollen_forecast_node
    path: pollen_forecast_node
    inputs:
      latitude: my-coordinates/latitude
      longitude: my-coordinates/longitude
      hourly: my-coordinates/hourly
    outputs:
      - pollen_forecast
```

Your point source must output:

* Topic: `latitude`, `longitude`, `hourly`
* Data: Each as a string (latitude and longitude as decimal degrees, hourly as comma-separated names)
* Metadata:

  ```json
  {
    "latitude": "string, decimal degrees (e.g., '51.5')",
    "longitude": "string, decimal degrees (e.g., '-0.13')",
    "hourly": "comma-separated string of pollen types (e.g., 'grass_pollen,tree_pollen,weed_pollen')"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                    |
| ---------- | ------ | -------------------------------------------------------------- |
| latitude   | str    | Latitude in decimal degrees (e.g., '51.5')                     |
| longitude  | str    | Longitude in decimal degrees (e.g., '-0.13')                   |
| hourly     | str    | Comma-separated pollen types (e.g., 'grass_pollen,tree_pollen')|

### Output Topics

| Topic           | Type             | Description                                              |
| --------------- | ---------------- | -------------------------------------------------------- |
| pollen_forecast | dict or str      | Full API response containing forecast or error message   |


## License

Released under the MIT License.
