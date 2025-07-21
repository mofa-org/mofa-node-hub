# telegram_channel_api

A Dora-rs node for querying and mirroring the contents of a Telegram channel or public link via HTTP. It enables downstream Dora flow nodes to fetch and inspect the HTML content or status of a Telegram channel.

## Features
- Fetches content from a specified Telegram channel or public link
- Exposes content, HTTP status code, and error reporting as structured output
- Simple input-driven invocation for integration in complex flows

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
  - id: telegram_channel_api
    build: pip install -e .
    path: telegram_channel_api
    inputs:
      user_input: input/user_input
    outputs:
      - telegram_channel_response
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
  - id: your_upstream_node
    build: ... # your build command
    path: ... # your path
    outputs:
      - user_input

  - id: telegram_channel_api
    build: pip install -e .
    path: telegram_channel_api
    inputs:
      user_input: your_upstream_node/user_input
    outputs:
      - telegram_channel_response
```

Your point source must output:

* Topic: `user_input`
* Data: Your input parameter (string or structure as needed)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Downstream API trigger or input text for the Telegram API node"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                          |
| -------------| ------ | ------------------------------------ |
| user_input    | string | User parameter or API trigger input  |

### Output Topics

| Topic                     | Type              | Description                                                     |
| ------------------------- | ----------------- | --------------------------------------------------------------- |
| telegram_channel_response | dict (JSON-serializable) | Telegram channel HTML response or error object               |


## License

Released under the MIT License.
