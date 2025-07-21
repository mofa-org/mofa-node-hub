# ReqresApiNode

A Dora-rs node for making HTTP GET requests to the Reqres API (https://reqres.in/api/users?page=1), exposing API responses via Dora's output messaging. Designed for easy chaining with other nodes for real-time web API integration.

## Features
- Integrates seamlessly with Dora-rs node environments
- Retrieves and parses JSON data from the Reqres API endpoint
- Graceful error handling and JSON parse fallback

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
  - id: reqres_api
    build: pip install -e .
    path: reqres_api_node
    inputs:
      user_input: input/user_input  # Optional input for compliance
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
  - id: reqres_api
    build: pip install -e .
    path: reqres_api_node
    inputs:
      user_input: other_node/some_parameter # Optional, e.g. user command input
    outputs:
      - api_response

  - id: downstream_node
    build: pip install your-downstream-node
    path: downstream_node
    inputs:
      api_response: reqres_api/api_response
    outputs:
      - processed_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable user input specification (optional)
* Metadata:

  ```json
  {
    "description": "Optional placeholder input; can be any serializable value for interface compliance."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                           |
|-------------|--------|-------------------------------------------------------|
| user_input  | Any    | Optional parameter, required for interface compliance |

### Output Topics

| Topic        | Type    | Description                                                                                   |
|--------------|---------|----------------------------------------------------------------------------------------------|
| api_response | Object  | Response from the Reqres API. If error, contains error message and possibly raw response text. |


## License

Released under the MIT License.
