# facebook_video_node

Easily integrate Facebook video downloading into your Dora-rs pipeline with this simple node. Provide a Facebook video URL and receive direct download links or metadata using a public API, all handled automatically for you.

## Features
- Accepts Facebook video URL as input parameter
- Fetches and returns video download information from a public API
- Handles errors gracefully, reporting via output topics

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
  - id: fb_downloader
    build: pip install -e .
    path: facebook_video_node
    inputs:
      url: input/url  # Provide the Facebook video URL here
    outputs:
      - video_download_info
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
  - id: url_source
    build: pip install your-input-node # Your source node
    path: your-input-node
    outputs:
      - url
  - id: fb_downloader
    build: pip install -e .
    path: facebook_video_node
    inputs:
      url: url_source/url
    outputs:
      - video_download_info
      - error
```

Your point source must output:

* Topic: `url`
* Data: Facebook video URL as a string
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Facebook video URL. Example: https://facebook.com/watch?v=xxxx"
  }
  ```

## API Reference

### Input Topics

| Topic | Type  | Description                       |
|-------|-------|-----------------------------------|
| url   | str   | Facebook video URL to download    |

### Output Topics

| Topic               | Type         | Description                              |
|---------------------|--------------|------------------------------------------|
| video_download_info | JSON/string  | Download info or direct links from API   |
| error               | string       | Error message, if any                    |


## License

Released under the MIT License.
