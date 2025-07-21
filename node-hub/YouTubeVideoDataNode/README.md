# youtube_video_node

Fetch YouTube Metadata via Text Search

## Features
- Text-based YouTube video search
- Automatic fallback to default search queries
- Structured API responses with error handling

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
  - id: youtube_video_node
    build: pip install -e .
    path: youtube_video_node
    inputs:
      search_text: input/search_text
    outputs:
      - youtube_video_data
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
  - id: text_source
    build: pip install your-custom-source
    path: your_custom_source
    outputs:
      - search_text
  - id: youtube_video_node
    build: pip install -e .
    path: youtube_video_node
    inputs:
      search_text: text_source/search_text
    outputs:
      - youtube_video_data
```

Your point source must output:

* Topic: `search_text`
* Data: Raw string representing search text
* Metadata:

  ```json
  { "type": "string", "description": "Query for YouTube video search" }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                 |
| ------------| ------ | --------------------------- |
| search_text | string | Text query for YouTube search |

### Output Topics

| Topic              | Type   | Description                        |
| ------------------ | ------ | ---------------------------------- |
| youtube_video_data | object | JSON results from YouTube search API |


## License

Released under the MIT License.
