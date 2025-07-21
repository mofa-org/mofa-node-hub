# nekos_best_node

A Dora-rs node for interfacing with nekos.best API endpoints, providing quick access to hug images, tickle gifs, or a current dynamic endpoint list with simple parameter selection.

## Features
- Fetch hug images or tickle gifs from nekos.best
- Dynamically retrieve supported API endpoint list
- Simple Dora-rs API: supply input parameter, receive parsed output

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
  - id: nekos_node
    build: pip install -e .
    path: nekos_best_node
    inputs:
      endpoint_type: input/endpoint_type
    outputs:
      - nekosbest_output
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
  - id: controller
    path: my-controller
    outputs:
      - endpoint_type
  - id: nekos_node
    build: pip install -e .
    path: nekos_best_node
    inputs:
      endpoint_type: controller/endpoint_type
    outputs:
      - nekosbest_output
```

Your point source must output:

* Topic: `endpoint_type`
* Data: String ('hug', 'tickle', or 'endpoints')
* Metadata:

  ```json
  {
    "dtype": "str",
    "values": ["hug", "tickle", "endpoints"]
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                         |
| ---------------| ------ | --------------------------------------------------- |
| endpoint_type   | str    | Selects nekos.best API ('hug', 'tickle', 'endpoints') |

### Output Topics

| Topic             | Type  | Description                    |
| -----------------| ----- | ------------------------------ |
| nekosbest_output | dict  | Parsed nekos.best API response |


## License

Released under the MIT License.
