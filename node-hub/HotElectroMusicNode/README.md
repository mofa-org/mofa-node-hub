# hot_electro_music

A Dora node that fetches the hottest Electro music tracks from Openwhyd and exposes the results via a structured output message. This node enables seamless integration of trending music metadata into Dora-based pipelines, suitable for recommendation engines, dashboards, or music exploration bots.

## Features
- Fetches hot Electro music data in real-time from Openwhyd
- Robust error handling with clear error messages in output
- Simple API with a single input and JSON output

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
  - id: hot_electro_music
    build: pip install -e .
    path: hot_electro_music
    inputs:
      user_input: input/user_input
    outputs:
      - hot_electro_music
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
  - id: your_source_node
    build: pip install your_source_node
    path: your_source_node
    outputs:
      - user_input

  - id: hot_electro_music
    build: pip install -e .
    path: hot_electro_music
    inputs:
      user_input: your_source_node/user_input
    outputs:
      - hot_electro_music
```

Your point source must output:

* Topic: `user_input`
* Data: Any data type (string, None, or dict)
* Metadata:

  ```json
  {
    "description": "This value is not used by hot_electro_music; acts as a trigger, can be null or any string value."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                     |
| ----------- | ------ | ----------------------------------------------- |
| user_input  | any    | (Optional) Input to trigger a hot music fetch   |

### Output Topics

| Topic             | Type | Description                                           |
| ----------------- | ---- | -----------------------------------------------------|
| hot_electro_music | dict | JSON with hot electro music data or error information |


## License

Released under the MIT License.
