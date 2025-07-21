# stgallen_parking_node

Retrieve parking records from Stadt St.Gallen Open Data API.

## Features
- Fetches latest parking records via Open Data API
- Accepts flexible URL-style query parameters for filtering results
- Provides structured output and error handling for Dora integration

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
  - id: stgallen_parking
    build: pip install -e stgallen_parking_node
    path: stgallen_parking_node
    inputs:
      user_input: input/user_input
    outputs:
      - parking_records
      - api_error
      - agent_error
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
  - id: my_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input

  - id: stgallen_parking
    build: pip install -e stgallen_parking_node
    path: stgallen_parking_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - parking_records
      - api_error
      - agent_error
```

Your point source must output:

* Topic: `user_input`
* Data: URL query string, e.g. `limit=10&phname=CityCenter`
* Metadata:

  ```json
  {
    "type": "string",
    "desc": "URL query string with parameters, e.g. 'limit=10&phname=CityCenter'"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                      |
| ----------- | ------ | ------------------------------------------------|
| user_input  | string | URL query string (e.g., 'limit=10&phname=LotA') |

### Output Topics

| Topic           | Type   | Description                                    |
| --------------- | ------ | ---------------------------------------------- |
| parking_records | dict   | Retrieved JSON response from St.Gallen API     |
| api_error       | string | API error message                             |
| agent_error     | string | Internal agent error during processing         |


## License

Released under the MIT License.
