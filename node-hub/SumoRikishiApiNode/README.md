# sumo_rikishi_node

Sumo wrestler data retrieval node for Dora-MOFA pipelines

## Features
- Retrieves rikishi (sumo wrestler) data from the Sumo API (https://www.sumo-api.com/api/rikishis)
- Configurable query parameters (`limit`, `skip`)
- Streams data into your Dora pipeline for downstream processing

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
  - id: sumo_rikishi_node
    build: pip install -e .
    path: sumo_rikishi_node
    inputs:
      parameters: input/parameters
    outputs:
      - rikishi_data
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
  - id: param_source
    build: pip install your-param-source
    path: your-param-source
    outputs:
      - parameters

  - id: sumo_rikishi_node
    build: pip install -e .
    path: sumo_rikishi_node
    inputs:
      parameters: param_source/parameters
    outputs:
      - rikishi_data
```

Your point source must output:

* Topic: `parameters`
* Data: dictionary with `limit` and `skip` as string values (optional, can omit for defaults)
* Metadata:

  ```json
  {
      "parameters": ["limit", "skip"],
      "types": {"limit": "string", "skip": "string"}
  }
  ```

## API Reference

### Input Topics

| Topic     | Type             | Description                                          |
|-----------|------------------|------------------------------------------------------|
| parameters| dict (str->str)  | Query options: `limit`, `skip` for pagination (str)  |

### Output Topics

| Topic        | Type  | Description                                         |
|--------------|-------|-----------------------------------------------------|
| rikishi_data | dict/list | Raw JSON returned by the Sumo API (rikishi records or error info) |

## License

Released under the MIT License.
