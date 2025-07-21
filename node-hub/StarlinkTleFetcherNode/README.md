# starlink_tle_fetcher

Fetch Starlink TLEs via Public API and Provide as Node Output

## Features
- Retrieves latest Starlink Two-Line Element (TLE) data from Celestrak
- Outputs fully parsed JSON for downstream nodes
- Robust error handling for connectivity or API issues

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
  - id: starlink_tle_fetcher
    build: pip install -e .
    path: starlink_tle_fetcher
    inputs:
      user_input: input/user_input
    outputs:
      - starlink_tle_output
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
  - id: starlink_tle_fetcher
    build: pip install -e .
    path: starlink_tle_fetcher
    inputs:
      user_input: input/user_input
    outputs:
      - starlink_tle_output
  - id: downstream_consumer
    build: pip install your-downstream-node
    path: your-downstream-node
    inputs:
      starlink_tle: starlink_tle_fetcher/starlink_tle_output
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

| Topic      | Type         | Description                       |
| ---------- | ------------ | ---------------------------------- |
| user_input | Any/ignored  | Dummy input to harmonize interface |

### Output Topics

| Topic                | Type    | Description                   |
| -------------------- | ------- | ----------------------------- |
| starlink_tle_output  | JSON    | Latest Starlink TLE data or error |


## License

Released under the MIT License.
