# bacon_ipsum_node

A Dora-rs compatible node that fetches bacon ipsum placeholder text from the [Bacon Ipsum API](https://baconipsum.com/api/). Supports configurable output type ("meat-and-filler" or "all-meat") and integrates with other Dora nodes for seamless text generation workflows.

## Features
- Fetches bacon ipsum placeholder text from a public API
- Supports configurable output type (all-meat or meat-and-filler)
- Returns results as plain text or error details

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
  - id: bacon_ipsum
    build: pip install -e bacon_ipsum_node
    path: bacon_ipsum_node
    inputs:
      type: input/type
    outputs:
      - bacon_ipsum_output
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
  - id: custom_type_source
    build: pip install your-type-generator
    path: your-type-generator
    outputs:
      - type

  - id: bacon_ipsum
    build: pip install -e bacon_ipsum_node
    path: bacon_ipsum_node
    inputs:
      type: custom_type_source/type
    outputs:
      - bacon_ipsum_output
```

Your point source must output:

* Topic: `type`
* Data: String, one of "meat-and-filler", "all-meat"
* Metadata:

  ```json
  {
    "type": "str",
    "allowed": ["meat-and-filler", "all-meat"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ----------| ------ | ----------------------------------------- |
| type       | str    | Bacon ipsum text type: "meat-and-filler" or "all-meat" |
| user_input | str    | Fallback user input for type (optional)   |

### Output Topics

| Topic               | Type      | Description                                |
| ------------------- | --------- | ------------------------------------------ |
| bacon_ipsum_output  | list/str  | Generated bacon ipsum text or error details|


## License

Released under the MIT License.
