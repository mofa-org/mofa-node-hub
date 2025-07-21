# zipcode_location_node

Zip code to Location lookup for Dora-rs and Mofa nodes

## Features
- Lookup city, state, country by US or international zip/postal code
- Robust error handling for invalid or missing zip codes
- Simple, single-step API for easy integration into pipelines

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
  - id: zipcode_lookup
    build: pip install -e .
    path: zipcode_location_node
    inputs:
      zip_code: input/zip_code
    outputs:
      - location_info
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
  - id: source_zip
    build: pip install your-input-source
    path: your-input-source
    outputs:
      - zip_code

  - id: zipcode_lookup
    build: pip install -e .
    path: zipcode_location_node
    inputs:
      zip_code: source_zip/zip_code
    outputs:
      - location_info
```

Your point source must output:

* Topic: `zip_code`
* Data: String
* Metadata:

  ```json
  {
    "dtype": "string"
  }
  ```

## API Reference

### Input Topics

| Topic     | Type   | Description                              |
| --------- | ------ | ---------------------------------------- |
| zip_code  | string | Zip or postal code as string (required)  |

### Output Topics

| Topic         | Type         | Description                                      |
| -------------| ------------ | ------------------------------------------------ |
| location_info| object (dict)| Location details or error message. See below.     |

The `location_info` output will always include at least:
- `error`: True/False
- If `error: False`: `city`, `state`, `country`, `zip_code` (all strings)
- If `error: True`: `error_msg` (string)

## License

Released under the MIT License.
