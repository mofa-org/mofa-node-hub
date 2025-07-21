# coinpaprika_node

A Dora-rs node for fetching cryptocurrency information and tags from the Coinpaprika API. This node demonstrates how to aggregate live Bitcoin data and taxonomy tags into a single output that is accessible in a Dora-rs pipeline.

## Features
- Fetches coin information for Bitcoin from Coinpaprika
- Retrieves an exhaustive list of crypto tags (categories) from Coinpaprika
- Simple request/response model with error reporting in output

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
  - id: coinpaprika_node
    build: pip install -e .
    path: coinpaprika_node
    inputs:
      user_input: input/user_input
    outputs:
      - coinpaprika_output
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
  - id: coin_source
    build: pip install your-coin-source
    path: your-coin-source
    outputs:
      - user_input
  - id: coinpaprika_node
    build: pip install -e .
    path: coinpaprika_node
    inputs:
      user_input: coin_source/user_input
    outputs:
      - coinpaprika_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or dict payload
* Metadata:

  ```json
  {
    "description": "User request trigger for Coinpaprika fetch. Can be empty or include params."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type          | Description                          |
| ----------- | -------------| ------------------------------------ |
| user_input  | any (string, dict) | User input (request trigger)         |

### Output Topics

| Topic               | Type          | Description                                   |
| ------------------- |-------------- | --------------------------------------------- |
| coinpaprika_output  | dict          | JSON object of BTC info & tags (w/ errors)    |


## License

Released under the MIT License.
