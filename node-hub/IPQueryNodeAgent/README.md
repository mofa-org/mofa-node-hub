# ipquery_node

A Dora-rs node that provides IP geolocation lookup by calling the public IPQuery API. This node receives an upstream message for chaining, invokes the API, and outputs a serializable JSON result containing location and network data for the caller's public IP address.

## Features
- Fetches geolocation and network information by querying the IPQuery API
- Ensures upstream chaining with a dummy input parameter (`user_input`)
- Robust error handling with serializable error messages

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
  - id: ipquery_node
    build: pip install -e .
    path: ipquery_node
    inputs:
      user_input: input/user_input
    outputs:
      - ipquery_response
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
    build: pip install -e my_input_node
    path: my_input_node
    outputs:
      - user_input

  - id: ipquery_node
    build: pip install -e .
    path: ipquery_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - ipquery_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy data; not used by IPQueryNodeAgent)
* Metadata:

  ```json
  {
    "description": "Placeholder parameter for flow consistency.",
    "required": true
  }
  ```

## API Reference

### Input Topics

| Topic       | Type      | Description                                            |
| ----------- | --------- | ----------------------------------------------------- |
| user_input  | Any       | Dummy parameter to facilitate upstream chaining       |

### Output Topics

| Topic            | Type      | Description                                        |
| ---------------- | --------- | -------------------------------------------------- |
| ipquery_response | dict      | IP geolocation/network data or error info as JSON  |


## License

Released under the MIT License.
