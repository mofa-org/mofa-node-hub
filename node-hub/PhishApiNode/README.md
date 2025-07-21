# phish_api_node

A Dora-rs node for retrieving the latest Phish show information from the Phish.in REST API and broadcasting it to your dataflow pipeline.

## Features
- Fetches current Phish show data from https://phish.in/api/v2/shows
- Handles and gracefully reports errors and API anomalies
- Integrates with mofa-agent architecture and can be triggered by other nodes

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
  - id: phish_api_node
    build: pip install -e phish_api_node
    path: phish_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - phish_show_data
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
  - id: phish_api_node
    build: pip install -e phish_api_node
    path: phish_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - phish_show_data
  - id: your_node
    build: pip install -e your_node
    path: your_node
    inputs:
      phish_show_data: phish_api_node/phish_show_data
```

Your point source must output:

* Topic: `phish_show_data`
* Data: Show data as returned from the Phish.in API (JSON-serializable dict)
* Metadata:

  ```json
  {
    "source": "phish.in/api/v2/shows",
    "format": "application/json"
  }
  ```

## API Reference

### Input Topics

| Topic               | Type      | Description                                           |
| ------------------- | --------- | ----------------------------------------------------- |
| user_input          | any       | Trigger event to fetch the show data (can be ignored) |

### Output Topics

| Topic             | Type    | Description                            |
| ----------------- | ------- | -------------------------------------- |
| phish_show_data   | dict    | JSON dict containing latest show info  |


## License

Released under the MIT License.
