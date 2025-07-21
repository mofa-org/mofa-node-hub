# earthquake_event_fetcher

Fetch recent earthquake events from the USGS Earthquake API with flexible query parameters.

## Features
- Pull earthquake event data from the USGS API
- Specify time range and minimum magnitude for query
- Outputs event count and a summary of recent earthquakes

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
  - id: earthquake_fetcher
    build: pip install -e .
    path: earthquake_event_fetcher
    inputs:
      starttime: input/starttime
      endtime: input/endtime
      minmagnitude: input/minmagnitude
    outputs:
      - earthquake_data
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
  - id: custom_params
    build: pip install -e .  # Your own node
    path: custom_params_node
    outputs:
      - starttime
      - endtime
      - minmagnitude
  - id: earthquake_fetcher
    build: pip install -e .
    path: earthquake_event_fetcher
    inputs:
      starttime: custom_params/starttime
      endtime: custom_params/endtime
      minmagnitude: custom_params/minmagnitude
    outputs:
      - earthquake_data
```

Your point source must output:

* Topic: `starttime`, `endtime`, `minmagnitude`
* Data: String (ISO date for times, float-like string for magnitude)
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Standard ISO-format date for starttime/endtime; stringified float for minmagnitude"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                   |
| -------------|--------|-----------------------------------------------|
| starttime     | string | Start of window (ISO date, e.g., 2023-03-01)  |
| endtime       | string | End of window (ISO date, e.g., 2023-03-02)    |
| minmagnitude  | string | Minimum event magnitude (e.g., 5, 2.5)        |

### Output Topics

| Topic            | Type  | Description                                    |
|------------------|-------|------------------------------------------------|
| earthquake_data  | dict  | Contains `count` and summary/event list output |


## License

Released under the MIT License.
