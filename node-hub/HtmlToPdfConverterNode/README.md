# html_to_pdf_node

Convert HTML content to PDF via a REST API using a Dora-rs node agent.

## Features
- Converts arbitrary HTML content to a PDF document using a remote API
- Simple string-based input/output interface
- Outputs base64-encoded PDF data as result

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
  - id: html_to_pdf
    build: pip install -e .
    path: html_to_pdf_node
    inputs:
      html_content: input/html_content  # Connect this to your HTML input node
    outputs:
      - pdf_file
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
  - id: html_source
    build: pip install -e my-html-source
    path: my_html_source
    outputs:
      - html_content
  - id: html_to_pdf
    build: pip install -e .
    path: html_to_pdf_node
    inputs:
      html_content: html_source/html_content
    outputs:
      - pdf_file
```

Your point source must output:

* Topic: `html_content`
* Data: HTML string to convert
* Metadata:

  ```json
  {"type": "string", "format": "html"}
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description             |
| -------------|--------|-------------------------|
| html_content  | string | HTML string to convert  |

### Output Topics

| Topic     | Type    | Description                               |
|-----------|---------|-------------------------------------------|
| pdf_file  | object  | {"pdf_base64": ...} or error JSON object |


## License

Released under the MIT License.
