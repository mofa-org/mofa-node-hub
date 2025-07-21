# open_north_representatives

Lookup Canadian government representatives using the Open North Represent API.

## Features
- Query representatives by first name (partial string search)
- Query representatives by Canadian postal code
- Easy integration with Dora/MOFA agent pipelines

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
  - id: open_north_representatives
    build: pip install -e .
    path: open_north_representatives
    inputs:
      first_name: input/first_name  # (optional) user's first name
      postcode: input/postcode      # (optional) user's postal code
    outputs:
      - representatives_by_name
      - representatives_by_postcode
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
    build: pip install -e .
    path: your_input_node
    outputs:
      - first_name
      - postcode
  - id: open_north_representatives
    build: pip install -e .
    path: open_north_representatives
    inputs:
      first_name: your_input_node/first_name
      postcode: your_input_node/postcode
    outputs:
      - representatives_by_name
      - representatives_by_postcode
```

Your point source must output:

* Topic: `first_name` or `postcode`
* Data: String containing either a first name or a valid Canadian postal code
* Metadata:

  ```json
  {
    "type": "string",
    "description": "User's first name (for name search) or postal code (for postcode search)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| first_name | string | The first name to search representatives by   |
| postcode   | string | The postal code to look up representatives   |

### Output Topics

| Topic                     | Type | Description                                                           |
| ------------------------- | ---- | --------------------------------------------------------------------- |
| representatives_by_name   | dict | List of representatives data returned from Open North by first name    |
| representatives_by_postcode | dict | List of representatives data returned by postal code                  |

## License

Released under the MIT License.
