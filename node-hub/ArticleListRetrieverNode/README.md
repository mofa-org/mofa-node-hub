# article_list_node

RESTful eLife Article List Fetcher Node

## Features
- Fetches the latest articles from the eLife REST API
- Robust error handling with error output on failures
- Ready for integration in dataflow pipelines via parameter and output ports

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
  - id: article_list_node
    build: pip install -e .
    path: article_list_node
    inputs:
      user_input: input/user_input
    outputs:
      - article_list
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
  - id: article_list_node
    build: pip install -e .
    path: article_list_node
    inputs:
      user_input: input/user_input
    outputs:
      - article_list
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (the port exists for compatibility, but is not required by this node)
* Metadata:

  ```json
  {
    "description": "Placeholder input; not utilized by the node but present for dataflow compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                |
| ----------- | ------ | ----------------------------------------------------------|
| user_input  | any    | Placeholder input for dataflow compatibility; not required |

### Output Topics

| Topic        | Type         | Description                                                        |
| ------------ | ------------| ------------------------------------------------------------------ |
| article_list | List[Object] | List of article objects from the eLife API or error as JSON object |


## License

Released under the MIT License.
