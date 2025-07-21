# YandeAPIV2Node

A Dora-rs node for querying the YandeRe v2 JSON API endpoint and returning the results as Dora messages.

## Features
- Fetches latest data from the YandeRe v2 API endpoint
- Outputs API results (JSON: list or dict) for further downstream processing
- Robust error handling for network or API failures

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
  - id: yande
    build: pip install -e yande_api_v2_node
    path: yande_api_v2_node
    outputs:
      - yande_api_v2_response
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
  - id: yande
    build: pip install -e yande_api_v2_node
    path: yande_api_v2_node
    outputs:
      - yande_api_v2_response
  # Example downstream node:
  - id: downstream
    build: pip install -e your_downstream_node
    path: your_downstream_node
    inputs:
      yande_api_v2_response: yande/yande_api_v2_response
```

Your point source must output:

* Topic: `yande_api_v2_response`
* Data: Dictionary or list matching the YandeRe v2 API JSON response
* Metadata:

  ```json
  {
    "error": false,
    "format": "json",
    "api_version": 2
  }
  ```

## API Reference

### Input Topics

| Topic      | Type                | Description                               |
| ---------- | ------------------- | ----------------------------------------- |
| user_input | any (not used)      | Dummy parameter for pipeline compatibility |

### Output Topics

| Topic                  | Type   | Description                                             |
| ---------------------- | ------ | ------------------------------------------------------- |
| yande_api_v2_response  | dict/list | YandeRe v2 API response or error object                 |


## License

Released under the MIT License.
