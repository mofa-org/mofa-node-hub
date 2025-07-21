# user_agent_detection

A Dora-rs node for User-Agent string analysis via the apicagent.com API. This node accepts a user agent string and returns detailed analysis and metadata describing the browser, device, and platform.

## Features
- User-Agent string parsing and analysis via apicagent API
- Flexible integration into Dora-rs workflows
- Structured error reporting for robust automation

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
  - id: user_agent_detection
    build: pip install -e .
    path: user_agent_detection
    inputs:
      user_agent: input/user_agent  # Receives User-Agent strings
    outputs:
      - user_agent_info            # Outputs analysis result
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
  - id: my_source_node
    build: pip install my-ua-source
    path: my-ua-source
    outputs:
      - user_agent

  - id: user_agent_detection
    build: pip install -e .
    path: user_agent_detection
    inputs:
      user_agent: my_source_node/user_agent
    outputs:
      - user_agent_info
```

Your point source must output:

* Topic: `user_agent`
* Data: User-Agent string (UTF-8)
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "User-Agent string, required by analysis node"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type         | Description           |
| ------------| ------------ | --------------------- |
| user_agent  | String       | User-Agent HTTP header|

### Output Topics

| Topic            | Type     | Description                       |
| ----------------| -------- | --------------------------------- |
| user_agent_info | Object   | Parsed browser/device information |


## License

Released under the MIT License.
