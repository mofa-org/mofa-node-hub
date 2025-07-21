# cheapshark_deals_node

CheapSharkDealsNode: Query CheapShark for game deals by title as a Dora-rs node

## Features
- Query CheapShark API for game deals by title
- Configurable search parameter (title) with sensible default
- Robust error handling and response forwarding

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
  - id: deals_node
    build: pip install -e .
    path: cheapshark_deals_node
    parameters:
      title: "batman"
    outputs:
      - deals_output
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
  - id: input_node
    path: your_input_node
    outputs:
    - title_param
  - id: deals_node
    build: pip install -e .
    path: cheapshark_deals_node
    inputs:
      title: input_node/title_param
    outputs:
      - deals_output
```

Your point source must output:

* Topic: `title`
* Data: String (game title)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Game title to search"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                     |
|-------|--------|---------------------------------|
| title | String | Game title for deal search      |

### Output Topics

| Topic        | Type   | Description                      |
|--------------|--------|----------------------------------|
| deals_output | Object | Game deals JSON or error message |

## License

Released under the MIT License.
