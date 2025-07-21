# autobahn_node

Dora-rs node for fetching real-time Autobahn service data.

## Features
- Fetches electric charging station information for Autobahn A1
- Retrieves active roadworks details from Autobahn API
- Aggregates multiple Autobahn endpoints into unified output

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
  - id: autobahn_node
    build: pip install -e .
    path: autobahn_node
    inputs:
      user_input: input/user_input
    outputs:
      - autobahn_data
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
  - id: your_point_source
    build: pip install your_point_source
    path: your_point_source
    outputs:
      - user_input

  - id: autobahn_node
    build: pip install -e .
    path: autobahn_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - autobahn_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (parameter passed to trigger Autobahn query)
* Metadata:

  ```json
  {
    "description": "Arbitrary parameter to trigger API fetch"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type       | Description                             |
| ---------- | ---------- | --------------------------------------- |
| user_input | Any        | Pass-through trigger to perform queries |

### Output Topics

| Topic         | Type   | Description                                                   |
| ------------- | ------ | ------------------------------------------------------------- |
| autobahn_data | dict   | Object containing keys `data` (API results), `errors` (dict)  |

## License

Released under the MIT License.
