# world_bank_region

Fetches and outputs the list of World Bank regions via the World Bank REST API. Designed for use in Dora/MOFA pipelines as a node producing region metadata for downstream processing.

## Features
- Retrieves latest region metadata from the World Bank API
- Simple stateless design: always fetches fresh data on trigger
- Compatible with MOFA/Dora agent pipeline protocols

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
  - id: world_bank_region
    build: pip install -e .
    path: world_bank_region
    inputs:
      user_input: input/user_input # placeholder to trigger fetch
    outputs:
      - regions
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
  - id: data_fetcher
    build: pip install -e .
    path: world_bank_region
    inputs:
      user_input: input/user_input # trigger input
    outputs:
      - regions

  - id: consumer
    build: pip install your-consumer-node   # replace with actual
    path: your-consumer-module
    inputs:
      regions: data_fetcher/regions
```

Your point source must output:

* Topic: `user_input`
* Data: Any (placeholder, e.g. a boolean or empty dict)
* Metadata:

  ```json
  {"description": "placeholder trigger for region node"}
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                                      |
| ---------- | --------- | ------------------------------------------------ |
| user_input | Any       | Placeholder trigger to initiate region fetch     |

### Output Topics

| Topic   | Type         | Description                                      |
| ------- | ------------ | ------------------------------------------------ |
| regions | List or Dict | List of regions or error dict from World Bank API |

## License

Released under the MIT License.
