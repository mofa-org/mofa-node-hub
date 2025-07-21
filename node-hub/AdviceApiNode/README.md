# advice_api_node

A Dora-rs node for accessing the <https://api.adviceslip.com/>. Fetches random advice or lets you search for advice by keyword. Fully stateless, self-contained, and easily integrated into Dora-based pipelines.

## Features
- Fetch random advice from adviceslip.com
- Search for advice containing a given keyword
- Robust error output for API or decoding issues

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
  - id: advice_api_node
    build: pip install -e .
    path: advice_api_node
    inputs:
      keyword: input/keyword
      user_input: input/user_input
    outputs:
      - advice_data
      - api_error
      - agent_error
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
  - id: your_source
    build: pip install your-source
    path: your_source
    outputs:
      - keyword

  - id: advice_api_node
    build: pip install -e .
    path: advice_api_node
    inputs:
      keyword: your_source/keyword
      user_input: input/user_input
    outputs:
      - advice_data
      - api_error
      - agent_error

  - id: your_sink
    build: pip install your-sink
    path: your_sink
    inputs:
      advice_data: advice_api_node/advice_data
      api_error: advice_api_node/api_error
      agent_error: advice_api_node/agent_error
```

Your point source must output:

* Topic: `keyword`
* Data: String (keyword for advice search)
* Metadata:

  ```json
  {
    "type": "string",
    "optional": true,
    "description": "Keyword to search for relevant advices"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                       |
| ---------- | ------ | -------------------------------------------------|
| keyword    | str    | Keyword to search advice (optional, can be empty) |
| user_input | any    | Default input passthrough                         |

### Output Topics

| Topic        | Type | Description                                |
| ------------ | ---- | ------------------------------------------ |
| advice_data  | dict | API result from adviceslip.com             |
| api_error    | dict | API-level or JSON decode error details      |
| agent_error  | dict | Uncaught exceptions or runtime errors       |


## License

Released under the MIT License.
