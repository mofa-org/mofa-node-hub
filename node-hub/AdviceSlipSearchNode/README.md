# adviceslip_search_node

A Dora-rs node that queries the [Advice Slip JSON API](https://api.adviceslip.com/) with a fixed search term and returns the result (or error) as an output. Intended as an example node for API querying in Dora/Mofa agent networks.

## Features
- Fetches advice from the Advice Slip API using a sample search query
- Handles JSON and error responses gracefully, propagating error details
- Compatible with upstream nodes via dummy `user_input` parameter

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
  - id: adviceslip-search
    build: pip install -e .
    path: adviceslip_search_node
    inputs:
      user_input: input/user_input  # Can be a dummy upstream
    outputs:
      - advice_search_result
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
  - id: upstream
    build: pip install your-upstream
    path: upstream_node
    outputs:
      - user_input

  - id: adviceslip-search
    build: pip install -e .
    path: adviceslip_search_node
    inputs:
      user_input: upstream/user_input
    outputs:
      - advice_search_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any value or None (used only for triggering)
* Metadata:

  ```json
  {
    "desc": "Trigger input for AdviceSlipSearchNode. Ignored content; only used for pipeline compatibility."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                          |
| ----------- | -------- | ------------------------------------ |
| user_input  | Any      | Dummy input to trigger the node      |

### Output Topics

| Topic                 | Type    | Description                                                 |
| --------------------- | ------- | ----------------------------------------------------------- |
| advice_search_result  | dict    | Raw API result, or error info if request/JSON failed        |

## License

Released under the MIT License.
