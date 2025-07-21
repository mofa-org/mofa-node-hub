# nppes_provider_node

A Dora-rs node that queries the US NPPES NPI Registry API for healthcare provider data, returning the response as a structured dictionary. This node facilitates integration of external healthcare provider lookup into Dora pipelines.

## Features
- Calls the US NPPES (National Provider Identifier) Registry REST API
- Fully asynchronous request/response integration in Dora-rs compatible nodes
- Output is structured JSON from the NPPES API

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
  - id: nppes_query
    build: pip install -e nppes_provider_node
    path: nppes_provider_node
    inputs:
      user_input: dora/input/user_input
    outputs:
      - nppes_api_response
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
  - id: my_custom_input
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: nppes_query
    build: pip install -e nppes_provider_node
    path: nppes_provider_node
    inputs:
      user_input: my_custom_input/user_input
    outputs:
      - nppes_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (trigger/informational string)
* Metadata:

  ```json
  {
    "description": "Any value accepted. Triggers the query."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                                    |
| ---------- | ------- | ---------------------------------------------- |
| user_input | any     | Input parameter (not examined); triggers call  |

### Output Topics

| Topic              | Type       | Description                                             |
| ------------------ | ---------- | ------------------------------------------------------- |
| nppes_api_response | dict/json  | Dictionary from NPPES Registry API response or error    |


## License

Released under the MIT License.
