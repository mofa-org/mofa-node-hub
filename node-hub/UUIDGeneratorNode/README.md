# uuid_generator_node

A Dora-rs node that generates lists of UUIDs by fetching them from an external API (uuidtools.com). It exposes parameters for custom UUID count and supports robust error handling, ensuring reliable downstream data delivery for pipeline integration.

## Features
- Fetches lists of UUIDs from uuidtools.com API
- Configurable number of UUIDs via input parameters
- Structured and serializable output including error reporting

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
  - id: uuid_generator
    build: pip install -e uuid_generator_node
    path: uuid_generator_node
    inputs:
      user_input: dora/input/user_input
      count: dora/input/count
    outputs:
      - uuid_list
    config:
      count: 3  # Default number of UUIDs if not specified
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
    build: pip install -e my_input_node
    path: my_input_node
    outputs:
      - user_input
      - count
  - id: uuid_generator
    build: pip install -e uuid_generator_node
    path: uuid_generator_node
    inputs:
      user_input: my_input_node/user_input
      count: my_input_node/count
    outputs:
      - uuid_list
```

Your point source must output:

* Topic: `user_input`
* Data: Any payload to signal UUID generation request
* Metadata:

  ```json
  {
    "description": "Any triggering payload. Not parsed, only presence required."
  }
  ```

* Topic: `count`
* Data: Integer number of UUIDs to generate (optional; defaults to 3)
* Metadata:
  ```json
  {
    "description": "Number of UUIDs to generate.",
    "dtype": "int"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                      |
| ------------|--------|--------------------------------------------------|
| user_input  | any    | Signal input to trigger UUID generation          |
| count       | int    | Number of UUIDs to generate (optional, default 3) |

### Output Topics

| Topic      | Type    | Description                                |
|------------|---------|--------------------------------------------|
| uuid_list | dict    | Dictionary with keys 'uuids', 'count', or 'error' |

## License

Released under the MIT License.
