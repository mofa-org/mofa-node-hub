# artwork_node

A Dora-rs node for fetching artwork metadata from the Art Institute of Chicago API. Supports querying all artworks, a specific artwork by id, or searching for artworks (e.g., containing cats).

## Features
- Fetch metadata for a specific artwork (including image id and title)
- Retrieve all artworks metadata from the Art Institute API
- Search for artworks with specific keywords (e.g., 'cats')

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
  - id: artwork_node
    build: pip install -e .
    path: artwork_node
    inputs:
      user_input: input/user_input
      action_type: input/action_type
    outputs:
      - artwork_data
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
    build: pip install your_input_node
    path: your_input_node
    outputs:
      - user_input
      - action_type

  - id: artwork_node
    build: pip install -e .
    path: artwork_node
    inputs:
      user_input: your_input_node/user_input
      action_type: your_input_node/action_type
    outputs:
      - artwork_data
```

Your point source must output:

* Topic: `action_type`
* Data: String ("get_specific", "get_all", or "search")
* Metadata:

  ```json
  {
    "type": "string",
    "allowed_values": ["get_specific", "get_all", "search"]
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                |
| -------------|--------|--------------------------------------------|
| user_input    | any    | Placeholder for dataflow (not used/direct) |
| action_type   | string | Action to take: "get_specific", "get_all", or "search" |

### Output Topics

| Topic         | Type   | Description                         |
| ------------- |--------|-------------------------------------|
| artwork_data  | dict   | Response from the Art Institute API |
|               |        |                                     |


## License

Released under the MIT License.
