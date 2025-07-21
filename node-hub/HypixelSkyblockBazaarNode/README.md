# hypixel_skyblock_bazaar

A Dora-rs node for integrating Hypixel Skyblock Bazaar data. This node fetches the latest bazaar information from the official Hypixel API and emits it via a Dora-compatible output. Useful for monitoring in-game economics, powering dashboards, or feeding live market data to other analysis/automation nodes.

## Features
- Retrieves current Hypixel Skyblock Bazaar statistics from the public API
- Returns full JSON response for maximal flexibility
- Graceful error handling with consistent output structure

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
  - id: hypixel_bazaar
    build: pip install -e .
    path: hypixel_skyblock_bazaar
    outputs:
      - bazaar_data
    parameters:
      user_input: ''  # No input required, left blank
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
  - id: hypixel_bazaar
    build: pip install -e .
    path: hypixel_skyblock_bazaar
    outputs:
      - bazaar_data
    parameters:
      user_input: ''

  - id: process_bazaar
    path: your_bazaar_processor
    inputs:
      bazaar_json: hypixel_bazaar/bazaar_data
    outputs:
      - processed_info
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": 0,
    "dtype": "float32",
    "shape": [0, 2]
  }
  ```

## API Reference

### Input Topics

| Topic        | Type    | Description                                |
| ------------| ------- | ------------------------------------------ |
| user_input   | String  | Dummy parameter (required by agent). No actual input needed for API call. |

### Output Topics

| Topic        | Type    | Description                   |
| ------------| ------- | ----------------------------- |
| bazaar_data | Dict    | Full JSON data from Hypixel Skyblock Bazaar API, or error message |


## License

Released under the MIT License.
