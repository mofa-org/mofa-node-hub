# neon_text_logo_node

Create stunning neon-style PNG logo images from any input text using an easy Dora node interface!

## Features
- Renders input strings as neon-light PNG logo images
- Uses fast, public web API for logo generation—no local graphics libraries required
- Simple API: just provide your text, get an instant image link

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
  - id: neon-logo
    build: pip install -e .
    path: neon_text_logo_node
    inputs:
      user_input: input/user_input  # (for compatibility; can leave empty)
      text: input/text              # String: the text to render as neon
    outputs:
      - logo_url
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
  - id: my-text-source
    build: pip install my-source-node
    path: my_source_node
    outputs:
      - text
  - id: neon-logo
    build: pip install -e .
    path: neon_text_logo_node
    inputs:
      text: my-text-source/text
      user_input: input/user_input
    outputs:
      - logo_url
```

Your point source must output:

* Topic: `text`
* Data: String to convert to neon logo
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "Text to render as neon logo. Should be a non-empty string."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                |
| ------------| -------| ------------------------------------------ |
| user_input   | any    | Placeholder for compatibility (may be empty)|
| text         | string | The text to be rendered as a neon logo     |

### Output Topics

| Topic     | Type   | Description                                           |
| --------- | ------ | -----------------------------------------------------|
| logo_url  | dict   | {"logo_url": link, "error": bool, "message"?: string} |

## License

Released under the MIT License.
