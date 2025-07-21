# logo_provider_node

Agent node for fetching logo resources from the logotypes.dev API. Supports retrieving all available logos or fetching a single random logo.

## Features
- Fetches all logo resources from logotypes.dev via API
- Retrieves a random logo for quick sampling or inspiration
- Graceful error handling with standardized error output

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
  - id: logo_provider
    build: pip install -e .
    path: logo_provider_node
    inputs:
      action: input/action
    outputs:
      - all_logos
      - random_logo
      - error
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
  - id: input
    build: pip install -e .
    path: input-provider
    outputs:
      - action

  - id: logo_provider
    build: pip install -e .
    path: logo_provider_node
    inputs:
      action: input/action
    outputs:
      - all_logos
      - random_logo
      - error
```

Your point source must output:

* Topic: `action`
* Data: String 'all' or 'random'
* Metadata:

  ```json
  {
      "type": "str",
      "description": "Action for logo provider: 'all' for all logos, 'random' for a random logo."
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                               |
| ------- | ------ | ----------------------------------------- |
| action  | str    | Action: 'all' (fetch all) or 'random'.    |

### Output Topics

| Topic        | Type   | Description                |
| ------------ | ------ | --------------------------|
| all_logos    | dict   | All logos (JSON response)  |
| random_logo  | dict   | Random logo (JSON object)  |
| error        | dict   | Error (if any occurred)    |

## License

Released under the MIT License.
