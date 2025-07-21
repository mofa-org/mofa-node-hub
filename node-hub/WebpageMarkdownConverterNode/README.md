# webpage_markdown_node

A Dora-rs node that converts a given webpage URL to Markdown format using the publicly hosted `urltomarkdown` API. 

## Features
- Converts webpage content at a given URL to Markdown.
- Simple API: provide a URL, get Markdown output or error.
- Handles network and input validation errors gracefully.

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
  - id: webpage_markdown_node
    build: pip install -e .
    path: webpage_markdown_node
    inputs:
      url: input/url
    outputs:
      - markdown_result
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
  - id: your_url_source_node
    build: pip install -e .
    path: your_url_source_node
    outputs:
      - url

  - id: webpage_markdown_node
    build: pip install -e .
    path: webpage_markdown_node
    inputs:
      url: your_url_source_node/url
    outputs:
      - markdown_result
```

Your point source must output:

* Topic: `url`
* Data: string containing the webpage URL
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Webpage URL to convert to Markdown"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                |
|-------|--------|----------------------------|
| url   | str    | Webpage URL for conversion |

### Output Topics

| Topic           | Type        | Description                            |
|-----------------|------------|----------------------------------------|
| markdown_result | dict       | Markdown content or error information  |


## License

Released under the MIT License.
