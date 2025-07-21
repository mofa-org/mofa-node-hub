# restful_api_node

Call any RESTful API endpoint and stream the full JSON response to downstream Dora nodes.

## Features
- Fetch data from public or private HTTP REST APIs
- Parse and forward full JSON API responses
- Propagate HTTP and decoding errors downstream

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
  - id: restful_api_node
    build: pip install -e .
    path: restful_api_node
    inputs:
      user_input: input/user_input  # Placeholder; not required for HTTP fetch
    outputs:
      - api_response
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
  - id: your_upstream_node
    build: pip install your-upstream-node
    path: your-upstream-node
    outputs:
      - user_input

  - id: restful_api_node
    build: pip install -e .
    path: restful_api_node
    inputs:
      user_input: your_upstream_node/user_input
    outputs:
      - api_response

  - id: your_downstream_node
    build: pip install your-downstream-node
    path: your-downstream-node
    inputs:
      api_response: restful_api_node/api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any (not used by this node, required for chaining compatibility)
* Metadata:

  ```json
  {
    "topic": "user_input",
    "required": false,
    "description": "Any input; placeholder to facilitate message chaining."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                      |
| ----------- | ------ | ------------------------------------------------ |
| user_input  | any    | Placeholder input for compatibility and chaining |

### Output Topics

| Topic         | Type            | Description                                  |
| ------------- | --------------- | --------------------------------------------- |
| api_response  | dict / JSON     | JSON-decoded response or error message        |


## License

Released under the MIT License.

````