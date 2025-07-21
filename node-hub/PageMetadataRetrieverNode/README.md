# page_metadata_node

A Dora node that retrieves and outputs website metadata using Microlink.io API from a provided URL. This node can be used in Dora workflows to fetch link previews, summaries, and metadata for automation and enrichment tasks.

## Features
- Fetches rich metadata for URLs using the Microlink API
- Handles errors and invalid inputs gracefully, outputting a clear error message
- Integrates as a plug-and-play node in Dora/Mofa data flows

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
  - id: page_metadata
    build: pip install -e .
    path: page_metadata_node
    inputs:
      target_url: input/target_url
    outputs:
      - metadata_output

  - id: demo_input
    build: pip install dora-demo-input-node
    path: dora-demo-input-node
    outputs:
      - target_url
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
  - id: your_url_source
    build: pip install your-url-node
    path: your-url-node
    outputs:
      - target_url
  - id: page_metadata
    build: pip install -e .
    path: page_metadata_node
    inputs:
      target_url: your_url_source/target_url
    outputs:
      - metadata_output
```

Your point source must output:

* Topic: `target_url`
* Data: String URL to query
* Metadata:

  ```json
  {
    "type": "string",
    "description": "URL to fetch metadata for"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                          |
| ------------| ------ | ------------------------------------ |
| target_url  | string | URL to fetch metadata for (required) |

### Output Topics

| Topic           | Type | Description                                           |
| --------------- | ---- | -----------------------------------------------------|
| metadata_output | dict | Metadata result from Microlink API, or error details |

## License

Released under the MIT License.
