# glitch_logo_node

Generate glitch effect logos via the Abhi API.

## Features
- On-the-fly logo generation with glitch visual effect
- Stateless input support for dynamic pipeline updates
- Robust error handling and status reporting

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
  - id: glitch_logo
    build: pip install -e .
    path: glitch_logo_node
    inputs:
      user_input: upstream/user_input
      text: upstream/text
    outputs:
      - glitch_logo_result
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
    build: pip install your-point-source-node
    path: your-point-source-node
    outputs:
      - user_input
      - text
  - id: glitch_logo
    build: pip install -e .
    path: glitch_logo_node
    inputs:
      user_input: point_source/user_input
      text: point_source/text
    outputs:
      - glitch_logo_result
```

Your point source must output:

* Topic: `user_input`/`text`
* Data: Strings (for `text`), could be empty for `user_input`
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Input text for logo generation or user input trigger."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                   |
|-------------|--------|-----------------------------------------------|
| user_input  | string | Input trigger to allow upstream dataflow      |
| text        | string | Text to be displayed with glitch effect style |

### Output Topics

| Topic               | Type   | Description                                                          |
|---------------------|--------|----------------------------------------------------------------------|
| glitch_logo_result  | dict   | Result dictionary with image URL/status/message and input parameters  |

## License

Released under the MIT License.
