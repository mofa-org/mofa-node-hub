# formula_one_car_data

Easily fetch Formula 1 driver information and car telemetry from the OpenF1 API with a Dora-rs compatible node.

## Features
- Access real-time and historical Formula 1 driver and car telemetry data
- Filter telemetry by driver number, session, and minimum speed threshold
- Simple YAML-based configuration for quick integration in Dora pipelines

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
  - id: openf1-data
    build: pip install -e .
    path: formula_one_car_data
    inputs:
      user_input: input/user_input
      driver_number: input/driver_number
      session_key: input/session_key
      mode: input/mode
      speed: input/speed
    outputs:
      - openf1_drivers
      - openf1_car_data
      - error
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
    build: pip install your-custom-node
    path: your-custom-node
    outputs:
      - user_input
      - driver_number
      - session_key
      - mode
      - speed
  - id: openf1-data
    build: pip install -e .
    path: formula_one_car_data
    inputs:
      user_input: point_source/user_input
      driver_number: point_source/driver_number
      session_key: point_source/session_key
      mode: point_source/mode
      speed: point_source/speed
    outputs:
      - openf1_drivers
      - openf1_car_data
      - error
```

Your point source must output:

* Topic: `user_input`, `driver_number`, `session_key`, `mode`, `speed`
* Data: Literal values or parameter dicts
* Metadata:

  ```json
  {
    "description": "OpenF1 agent parameters",
    "example": {
      "driver_number": "44",
      "session_key": "9158",
      "mode": "car_data",
      "speed": "320"
    }
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                 |
| -------------|--------|---------------------------------------------|
| user_input    | any    | User command or additional parameters        |
| driver_number | str    | Driver's racing number (e.g. '44' for HAM)  |
| session_key   | str    | Session identifier (practice, quali, race)  |
| mode          | str    | Either 'drivers' or 'car_data'              |
| speed         | str    | Minimum speed for telemetry filtering       |

### Output Topics

| Topic            | Type      | Description                                      |
|------------------|-----------|--------------------------------------------------|
| openf1_drivers   | list/dict | Driver information for the requested session      |
| openf1_car_data  | list/dict | Telemetry data filtered by speed and parameters   |
| error            | dict      | Error feedback if request fails or is invalid     |


## License

Released under the MIT License.
