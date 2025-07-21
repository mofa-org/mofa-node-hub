# aareguru_weather_node

Access real-time Swiss river Aare water data via a Dora-rs compatible node.

## Features
- Fetch current Aare river temperature for a city
- Retrieve all weather data for a specified city or all supported cities
- List all supported cities with valid weather data endpoints

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
  - id: weather
    build: pip install -e .
    path: aareguru_weather_node
    inputs:
      action: input/action  # Input topic for command
      city: input/city      # Optional, default: 'bern'
    outputs:
      - weather_data
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
  - id: city_selector
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - action
      - city

  - id: weather
    build: pip install -e .
    path: aareguru_weather_node
    inputs:
      action: city_selector/action
      city: city_selector/city
    outputs:
      - weather_data
```

Your point source must output:

* Topic: `action`
* Topic: `city` (optional)
* Data: string values, e.g. action: 'current_temperature', city: 'bern'
* Metadata:

  ```json
  {
    "action": "string, required: one of 'current_temperature', 'all_data_city', 'all_data_all_cities', 'list_cities'",
    "city": "string (optional), default: 'bern'"
  }
  ```

## API Reference

### Input Topics

| Topic  | Type   | Description                                      |
| ------ | ------ | ------------------------------------------------ |
| action | str    | Requested command (see below for supported)      |
| city   | str    | City name (optional; used for certain commands)  |

### Output Topics

| Topic        | Type       | Description                                      |
| ------------ | ---------- | ------------------------------------------------ |
| weather_data | dict/str   | Output data; AareGuru data or error as JSON/dict |

## License

Released under the MIT License.
