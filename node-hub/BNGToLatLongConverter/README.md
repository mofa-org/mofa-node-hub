# bng_to_latlong

Convert British National Grid (BNG) Easting/Northing coordinates to latitude/longitude using a public API.

## Features
- Converts BNG easting/northing pairs to WGS84 latitude/longitude
- Handles errors robustly (invalid input, network/API issues)
- Ready for use as a Dora node with chaining compatibility

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
  - id: bng_to_latlong
    build: pip install -e .
    path: bng_to_latlong
    inputs:
      easting: input/easting
      northing: input/northing
      user_input: input/user_input
    outputs:
      - latlong_result
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
  - id: your_source
    build: ...
    path: your_source
    outputs:
      - easting
      - northing
      - user_input
  - id: bng_to_latlong
    build: pip install -e .
    path: bng_to_latlong
    inputs:
      easting: your_source/easting
      northing: your_source/northing
      user_input: your_source/user_input
    outputs:
      - latlong_result
```

Your point source must output:

* Topic: `easting`, `northing`, and `user_input`
* Data: String (or float/int convertible to int for easting/northing)
* Metadata:

  ```json
  {
    "easting": "string|float|int",
    "northing": "string|float|int",
    "user_input": "any"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                       |
| -------------|--------|-----------------------------------|
| easting      | str/int/float | Easting (BNG coordinate, convertible to int) |
| northing     | str/int/float | Northing (BNG coordinate, convertible to int) |
| user_input   | any    | (Optional) For chaining/trigger   |

### Output Topics

| Topic           | Type   | Description                              |
|-----------------|--------|------------------------------------------|
| latlong_result  | dict   | API response: latitude/longitude or error|


## License

Released under the MIT License.
