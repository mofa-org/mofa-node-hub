# country_population

Fetches and outputs global country population data using https://countriesnow.space API, packaged as a Dora node with a simple, single-step ingress/egress.

## Features
- Retrieves fresh population data for all countries
- Outputs structured JSON via Dora node interface
- Resilient error handling with clear output reporting

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
  - id: country_population
    build: pip install -e .
    path: country_population
    inputs:
      user_input: input/user_input
    outputs:
      - country_population_data
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
  - id: input
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input

  - id: country_population
    build: pip install -e .
    path: country_population
    inputs:
      user_input: input/user_input
    outputs:
      - country_population_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any indicator (string/int/JSON) to trigger processing; the value is unused (but must be sent to maintain Dora node graph integrity).
* Metadata:

  ```json
  {
    "type": "string or any",
    "usage": "Placeholder; triggers country data retrieval"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                             |
|-------------|---------|---------------------------------------------------------|
| user_input  | any     | Dummy input to facilitate node linking, value ignored.  |

### Output Topics

| Topic                   | Type          | Description                                                       |
|-------------------------|---------------|-------------------------------------------------------------------|
| country_population_data | dict or list  | API response with population data or error info if request failed |


## License

Released under the MIT License.
