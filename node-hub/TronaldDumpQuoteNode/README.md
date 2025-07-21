# tronald_dump_node

A Dora-rs node fetching random quotes from Tronald Dump API, delivering whimsical, tweet-like Donald Trump quotes for fun or research pipelines.

## Features
- Fetches fresh random quotes from tronalddump.io
- Outputs structured metadata (quote, source, tags, timeline info)
- Simple API for integration in Dora/Mofa data flows

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
  - id: tronald_quote
    build: pip install -e tronald_dump_node
    path: tronald_dump_node
    inputs:
      user_input: input/user_input
    outputs:
      - tronald_dump_quote
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
  - id: my_custom_node
    build: pip install -e my_custom_node
    path: my_custom_node
    outputs:
      - user_input
  - id: tronald_quote
    build: pip install -e tronald_dump_node
    path: tronald_dump_node
    inputs:
      user_input: my_custom_node/user_input
    outputs:
      - tronald_dump_quote
```

Your point source must output:

* Topic: `user_input`
* Data: Any string, triggers fetching a quote
* Metadata:

  ```json
  {
    "dtype": "string",
    "description": "User input, triggers the Tronald Dump quote fetch."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| user_input  | string | Input that triggers quote fetching (any value) |

### Output Topics

| Topic                | Type  | Description                                  |
| -------------------- | ----- | -------------------------------------------- |
| tronald_dump_quote   | dict  | Contains either quote info or error message  |

## License

Released under the MIT License.
