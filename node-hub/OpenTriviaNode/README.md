# open_trivia_node

A Dora-rs node for fetching trivia questions from the Open Trivia Database (OpenTDB), supporting public and authenticated (token-based) access. Retrieves batches of questions and exposes them through Dora's messaging system for downstream consumption.

## Features
- Fetches trivia questions from OpenTDB
- Supports both token-based and public (no-token) API queries
- Exposes results as structured output for workflow integration

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
  - id: trivia_source
    build: pip install -e open_trivia_node
    path: open_trivia_node
    inputs:
      user_token: input/user_token  # Optional; can be omitted
    outputs:
      - trivia_results
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
  - id: custom_token_source
    build: pip install your-token-provider  # Or your source node
    path: your-token-node
    outputs:
      - user_token
  - id: trivia_source
    build: pip install -e open_trivia_node
    path: open_trivia_node
    inputs:
      user_token: custom_token_source/user_token
    outputs:
      - trivia_results
```

Your point source must output:

* Topic: `user_token`
* Data: String token (optional; empty string for anonymous access)
* Metadata:

  ```json
  {
    "type": "string",
    "optional": true
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                      |
| ----------- | ------ | ------------------------------------------------ |
| user_token  | string | Optional: Authentication token for OpenTDB API   |

### Output Topics

| Topic          | Type | Description                                                            |
| -------------- | ---- | ---------------------------------------------------------------------- |
| trivia_results | dict | JSON output with keys: 'status', 'results', and optional 'error' field |


## License

Released under the MIT License.
