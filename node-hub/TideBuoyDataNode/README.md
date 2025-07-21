# tide_buoy_node

Query Tide and Buoy Data APIs for Wave Condition Monitoring

## Features
- Fetches tide predictions from NOAA via public SurfTruths API
- Retrieves real-time buoy data from NDBC using REST endpoint
- Exposes all results and any errors via unified Dora-rs output

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
  - id: tide_buoy_node
    build: pip install -e .
    path: tide_buoy_node
    inputs:
      user_input: input/user_input  # Optional, not required
    outputs:
      - tide_buoy_data
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
  - id: your_input_node
    build: pip install -e your_input_node
    path: your_input_node
    outputs:
      - user_input

  - id: tide_buoy_node
    build: pip install -e .
    path: tide_buoy_node
    inputs:
      user_input: your_input_node/user_input  # Optional, not required
    outputs:
      - tide_buoy_data
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary (not used by this node)
* Metadata:

  ```json
  {
    "description": "Any value; not used by tide_buoy_node. Triggers the API query if provided."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                                      |
| ---------- | --------- | ------------------------------------------------ |
| user_input | Any       | Triggers API request; actual value is unused      |

### Output Topics

| Topic          | Type   | Description                                                        |
| -------------  | ------ | ------------------------------------------------------------------ |
| tide_buoy_data | dict   | Contains `results` and `errors` fields for tide and buoy API calls  |


## License

Released under the MIT License.

