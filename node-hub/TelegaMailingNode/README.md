# telega_mailing_node

Telegram API Mailing Node for Dora/AI pipelines

## Features
- Create new Telegram mailings to up to 1000 recipients via TelegaSend API
- Check mailing status by mailing id
- Easy integration with dora-rs or MOFA workflows

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
  - id: telega-mailer
    build: pip install -e .
    path: telega_mailing_node
    inputs:
      user_input: input/user_input
      input_json: input/input_json
    outputs:
      - telega_response
    env:
      TELEGASEND_API_KEY: "<your_telegasend_api_key>"
      TELEGASEND_API_BASE_URL: "https://app.telegasend.ru/api/v1"  # optional
      REQUEST_TIMEOUT: "30"  # optional
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
  - id: your-input-node
    outputs:
      - input_json
      - user_input
  - id: telega-mailer
    path: telega_mailing_node
    inputs:
      user_input: your-input-node/user_input
      input_json: your-input-node/input_json
    outputs:
      - telega_response
```

Your point source must output:

* Topic: `input_json`
* Data: JSON string like:

  ```json
  {
    "action": "create",  // or "status"
    "mailing_data": {...},  // required for "create"
    "mailing_id": "..."    // required for "status"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type     | Description                            |
| ------------| -------- | -------------------------------------- |
| user_input  | any      | (Required) For dataflow compatibility  |
| input_json  | str      | JSON-encoded command (see above)       |

### Output Topics

| Topic           | Type   | Description                   |
| --------------- | ------ | ----------------------------- |
| telega_response | dict   | API response or error         |

## License

Released under the MIT License.
