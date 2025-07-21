# jpl_orbital_node

Fetch close-approach data from NASA JPL's public API for minor planets, for use in MOFA/Dora dataflow pipelines.

## Features
- Retrieve close-approach data from JPL's Solar System Dynamics API
- Automatically emits results or errors as node outputs
- Easy integration in dataflow pipelines (Dora/MOFA)

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
  - id: jpl-orbital-node
    build: pip install -e .
    path: jpl_orbital_node
    inputs:
      user_input: input/user_input
    outputs:
      - close_approach_data
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
  - id: your-input-node
    build: pip install your-package
    path: your_input_node
    outputs:
      - user_input
  - id: jpl-orbital-node
    build: pip install -e .
    path: jpl_orbital_node
    inputs:
      user_input: your-input-node/user_input
    outputs:
      - close_approach_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or dictionary (not used in this node's implementation)
* Metadata:

  ```json
  {
    "type": "string|dict", 
    "description": "User-provided input, not utilized by this node but expected for pipeline compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type            | Description                               |
| ----------- | ---------------| ----------------------------------------- |
| user_input  | string or dict  | Input parameter (currently unused; placeholder) |

### Output Topics

| Topic               | Type                   | Description                     |
| ------------------- | ----------------------| ------------------------------- |
| close_approach_data | dict or string         | Result from JPL API or error block|


## License

Released under the MIT License.
