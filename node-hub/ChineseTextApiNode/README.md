# ChineseTextApiNode

Agent to access the Chinese Text Project's dictionary headwords via the public API and output them for downstream nodes.

## Features
- Retrieve dictionary headwords from the Chinese Text Project
- Robust error handling with automatic retries
- Output of headwords as JSON for integration into downstream flows

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: chinese_text_api
    build: pip install -e chinese_text_node
    path: chinese_text_node
    inputs:
      user_input: input/user_input
    outputs:
      - dictionary_headwords
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
  - id: user_node
    build: pip install your-node
    path: your-node
    outputs:
      - user_input

  - id: chinese_text_api
    build: pip install -e chinese_text_node
    path: chinese_text_node
    inputs:
      user_input: user_node/user_input
    outputs:
      - dictionary_headwords
```

Your point source must output:

* Topic: `user_input`
* Data: Any (placeholder for pipeline connection)
* Metadata:

  ```json
  {
    "description": "Placeholder input to facilitate downstream flow; content ignored."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                       |
| ----------- | ------ | -------------------------------------------------|
| user_input  | Any    | Placeholder input required for node connectivity. |

### Output Topics

| Topic                | Type         | Description                                                      |
| -------------------- | ------------ | ---------------------------------------------------------------- |
| dictionary_headwords | dict or list | Dictionary headwords from Chinese Text Project API, or error info |


## License

Released under the MIT License.
