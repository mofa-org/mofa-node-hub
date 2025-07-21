# user_agent_parser_node

Automated User Agent String Parsing Node for Dora-rs

## Features
- Parses user agent strings using the UserAgent.App API
- Supports default and custom user agent strings via config or message
- Structured API key/environment integration and error reporting

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
  - id: user_agent_parser
    build: pip install -e user_agent_parser_node
    path: user_agent_parser_node
    env:
      USERAGENT_APP_KEY: "your-useragent-app-key"
      DEFAULT_USER_AGENT: "Mozilla/5.0 (compatible; ExampleBot/1.0)"
    inputs:
      user_input: input/user_input  # Can optionally be omitted if not used
      ua: input/ua
    outputs:
      - parsed_user_agent
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
  - id: point_source
    build: pip install your-node
    path: your-point-source-node
    outputs:
      - ua
  - id: user_agent_parser
    build: pip install -e user_agent_parser_node
    path: user_agent_parser_node
    inputs:
      ua: point_source/ua
    outputs:
      - parsed_user_agent
```

Your point source must output:

* Topic: `ua`
* Data: User agent string (UTF-8 encoded or string)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "User-Agent string to parse. For example: 'Mozilla/5.0 ...'"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                  |
| ----------- | ------ | --------------------------- |
| user_input  | any    | (Optional) Additional user parameters or input ctx |
| ua          | string | User agent string to parse   |

### Output Topics

| Topic              | Type   | Description                                                  |
| ------------------ | ------ | ------------------------------------------------------------ |
| parsed_user_agent  | dict   | Parsed user agent output or error info (see below)           |


## License

Released under the MIT License.
