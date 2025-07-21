# mtg_node

Fetch Magic: The Gathering card or set data via the public MTG API.

## Features
- Query Magic: The Gathering API for cards or sets
- Flexible queries (e.g. search by name or set code)
- Returns structured API responses for downstream processing

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
  - id: mtg
    build: pip install -e .
    path: mtg_node
    inputs:
      resource_type: input/resource_type
      query: input/query
    outputs:
      - api_response
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
  - id: mtg
    build: pip install -e .
    path: mtg_node
    inputs:
      resource_type: input/resource_type
      query: input/query
    outputs:
      - api_response

  - id: consumer
    build: pip install your-consumer
    path: your-consumer-node
    inputs:
      api_response: mtg/api_response
```

Your point source must output:

* Topic: `resource_type`
* Data: string ('cards' or 'sets')
* Topic: `query`
* Data: string (e.g., `?name=Llanowar Elves` or empty string)
* Metadata:

  ```json
  {
    "resource_type": "string (cards or sets)",
    "query": "string (optional)"
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                   |
| --------------- | ------ | --------------------------------------------- |
| resource_type   | str    | Specify 'cards' or 'sets' to access that API  |
| query           | str    | (Optional) Query string for API filter/search |

### Output Topics

| Topic         | Type | Description                               |
| ------------- | ---- | ----------------------------------------- |
| api_response  | dict | JSON response from MTG API or error dict  |


## License

Released under the MIT License.
