# crisis_core_materia_node

Dora-rs node for interacting with the Crisis Core Materia Fusion API.

## Features
- Query all available materia from the Crisis Core API
- Fuse two materia dynamically through API calls
- Health check for remote API

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
  - id: materia
    build: pip install -e ./crisis_core_materia_node
    path: crisis_core_materia_node
    inputs:
      parameters: input/parameters   # Provide params: action etc.
    outputs:
      - materia_list
      - health_status
      - fusion_result
      - error
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
  # Your node that generates parameters (e.g., UI or CLI)
  - id: param_source
    build: pip install -e ./your-params-node
    path: your-params-node
    outputs:
      - parameters

  - id: materia
    build: pip install -e ./crisis_core_materia_node
    path: crisis_core_materia_node
    inputs:
      parameters: param_source/parameters
    outputs:
      - materia_list
      - health_status
      - fusion_result
      - error
```

Your point source must output:

* Topic: `parameters`
* Data: Dict with action and (optionally) materia1, materia2
* Metadata:

  ```json
  {
    "required_keys": ["action"],
    "optional_keys": ["materia1", "materia2"],
    "example": {"action": "fuse_materia", "materia1": "Fire", "materia2": "Fira"}
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                                 |
|------------|--------|-----------------------------------------------------------------------------|
| parameters | dict   | Parameters for agent action (keys: action, materia1, materia2). See below.  |

### Output Topics

| Topic         | Type   | Description                                                                   |
|---------------|--------|-------------------------------------------------------------------------------|
| materia_list  | dict   | List of all materia from API                                                  |
| health_status | dict   | Health status report from API                                                 |
| fusion_result | dict   | Result of fusion (success or error info)                                      |
| error         | dict   | Any error encountered (parameter or API error)                                |

## License

Released under the MIT License.
