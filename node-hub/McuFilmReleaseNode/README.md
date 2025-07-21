# mcu_film_release

Fetch the Next MCU Film Release Date in Dora-rs Pipelines

## Features
- Retrieves up-to-date information on Marvel Cinematic Universe (MCU) film releases
- Simple REST API integration – no authentication or input required
- Easily composable in Dora graphs as a stateless info node

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
  - id: mcu_film_release_node
    build: pip install -e .
    path: mcu_film_release
    outputs:
      - mcu_film_release_info
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
  - id: mcu_film_release_node
    build: pip install -e .
    path: mcu_film_release
    outputs:
      - mcu_film_release_info
    # (Add further "inputs" as required by your workflow)
  - id: consumer
    build: pip install your-consumer-node
    path: your_consumer_module
    inputs:
      mcu_info: mcu_film_release_node/mcu_film_release_info
```

Your point source must output:

* Topic: `mcu_film_release_info`
* Data: MCU release info as a dict (converted to JSON automatically)
* Metadata:

  ```json
  {
    "description": "MCU release info returned directly from https://www.whenisthenextmcufilm.com/api (all keys as in their response; may include error field)",
    "content_type": "application/json"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                    |
| -------------|--------|------------------------------------------------|
| user_input   | any    | Dummy placeholder for DAG compatibility. Ignored |

### Output Topics

| Topic                | Type   | Description                                                           |
|----------------------|--------|-----------------------------------------------------------------------|
| mcu_film_release_info| dict   | MCU film release data (or error message) from the API response        |

## License

Released under the MIT License.
