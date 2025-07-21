# openverse_image_search

A Dora-rs node for searching CC-licensed images using the Openverse public API. Fetches image metadata (URL, description, thumbnail, etc.) with configurable queries and integrates seamlessly into Dora pipelines.

## Features
- Seamless integration with Openverse image API for copyright-free image search
- Returns list of image URLs and metadata via Dora output stream
- Compatible with Dora-rs parameter passing and output messaging patterns

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
  - id: image_search
    build: pip install -e openverse_image_search
    path: openverse_image_search
    inputs:
      user_input: input/user_input  # Optional, for dataflow; not processed by this node
    outputs:
      - openverse_images
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
  - id: custom_input
    build: pip install your-input-node  # Replace with your input node
    path: your-input-node
    outputs:
      - user_input  # Any user input you want to forward (can be empty)

  - id: image_search
    build: pip install -e openverse_image_search
    path: openverse_image_search
    inputs:
      user_input: custom_input/user_input
    outputs:
      - openverse_images
  
  - id: consumer
    build: pip install your-output-node
    path: your-output-node
    inputs:
      openverse_images: image_search/openverse_images
```

Your point source must output:

* Topic: `user_input`
* Data: (Can be any type, ignored by this node)
* Metadata:

  ```json
  {
    "type": "string (optional)",
    "description": "Any metadata you want to forward as user input; this node ignores it."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                                      |
| ---------- | --------- | ------------------------------------------------ |
| user_input | Any       | Optional dataflow input, ignored by this agent   |

### Output Topics

| Topic            | Type    | Description                                       |
| ---------------- | ------- | ------------------------------------------------- |
| openverse_images | object  | List of image objects with id, title, url, etc.   |


## License

Released under the MIT License.
