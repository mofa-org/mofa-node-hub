# insult_api_node

API-powered insult and corporate jargon generator node for Dora-rs/Mofa pipelines.

## Features
- Fetches realistic corporate jargon phrases from a public API
- Retrieves classic humorous insults from an online endpoint
- Single-call integration with other Dora-rs/Mofa nodes

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
  - id: insult_api
    build: pip install -e insult_api_node
    path: insult_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - insult_api_output
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
  - id: userinput
    build: pip install your-input-node
    path: userinput
    outputs:
      - user_input
  - id: insult_api
    build: pip install -e insult_api_node
    path: insult_api_node
    inputs:
      user_input: userinput/user_input
    outputs:
      - insult_api_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any payload (not used, just for triggering agent)
* Metadata:

  ```json
  {
    "input_kind": "trigger",
    "description": "Any value; just to trigger node execution."
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                              |
| -------------|--------|------------------------------------------|
| user_input   | Any    | Triggers the API node; payload is ignored |

### Output Topics

| Topic             | Type    | Description                                 |
| ---------------- | ------- | ------------------------------------------- |
| insult_api_output| JSON    | JSON dict with 'corporate_jargon', 'insult', or 'error' |

## License

Released under the MIT License.
