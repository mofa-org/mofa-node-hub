# flyff_api_node

A Dora-rs node exposing the official Flyff MMO API as a robust, query-driven microservice node. Easily fetch class and world information through parameterized endpoint calls, making MMO data accessible to your pipeline!

## Features
- Query any supported Flyff MMO API endpoint dynamically
- Built-in retry and error reporting for robust operation
- JSON output fully compatible with Dora dataflow

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
  - id: flyff_api
    build: pip install -e .
    path: flyff_api_node
    inputs:
      endpoint_name: input/endpoint_name
      user_input: input/user_input
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
  - id: my_input_node
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - endpoint_name
      - user_input

  - id: flyff_api
    build: pip install -e .
    path: flyff_api_node
    inputs:
      endpoint_name: my_input_node/endpoint_name
      user_input: my_input_node/user_input
    outputs:
      - api_response

  - id: my_downstream
    build: pip install my-downstream-node
    path: my_downstream
    inputs:
      api_response: flyff_api/api_response
```

Your point source must output:

* Topic: `endpoint_name`, `user_input`
* Data: Strings (endpoint_name must be one of `get_all_class_ids`, `get_class_764`, `get_all_world_ids`, `get_world_6063`)
* Metadata:

  ```json
  {
    "endpoint_name": "string (one of: get_all_class_ids, get_class_764, get_all_world_ids, get_world_6063)",
    "user_input": "string (arbitrary, for dataflow only)"
  }
  ```

## API Reference

### Input Topics

| Topic          | Type   | Description                                                                                     |
| --------------| ------ | ---------------------------------------------------------------------------------------------- |
| endpoint_name  | str    | Name of the API endpoint to call (`get_all_class_ids`, `get_class_764`, `get_all_world_ids`, `get_world_6063`) |
| user_input     | str    | Dataflow facilitator, not used in logic                                                         |

### Output Topics

| Topic        | Type         | Description                                                      |
| ------------| ------------ | --------------------------------------------------------------- |
| api_response | dict or list | API response from Flyff server, or error dict on failure         |


## License

Released under the MIT License.
