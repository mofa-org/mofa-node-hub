# html_creator_node

A Dora-rs node that fetches an HTML web page from uptodown.com and returns it as a string result for downstream processing. Designed to act as an API integration node within the Dora workflow, ready to be composed with other nodes via input/output topics.

## Features
- Retrieves the HTML content from a configured external website (https://html-creator.en.uptodown.com/android)
- Graceful error reporting on connection or parse failures
- Easily composable input/output interface with Dora nodes

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
  - id: html_creator
    build: pip install -e html_creator_node
    path: html_creator_node
    inputs:
      user_input: input/user_input
    outputs:
      - html_page
      - api_error
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
  - id: your_point_source
    build: pip install your-source
    path: your-source-path
    outputs:
      - user_input
  - id: html_creator
    build: pip install -e html_creator_node
    path: html_creator_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - html_page
      - api_error
```

Your point source must output:

* Topic: `user_input`
* Data: (can be any dummy value; not strictly used)
* Metadata:

  ```json
  {
    "description": "Dummy input required by html_creator_node; content ignored."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                      |
| ---------- | ------ | -------------------------------- |
| user_input | any    | Dummy input required to trigger API fetch |

### Output Topics

| Topic      | Type   | Description                   |
| ---------- | ------ | ----------------------------- |
| html_page  | str    | HTML content of main page     |
| api_error  | object | Error details, if an error occurs |


## License

Released under the MIT License.
