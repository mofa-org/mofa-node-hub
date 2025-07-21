# first_news_node

Simple Dora-rs node for fetching the latest headlines from FIRST.org's security news API.

## Features
- Pulls latest security news headlines via HTTP GET from https://api.first.org/data/v1/news
- Robust error handling and unified JSON output format
- Ready-to-use in Dora-rs pipelines or as a standalone agent

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
  - id: first_news
    build: pip install -e .
    path: first_news_node
    outputs:
      - first_news_response
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
  - id: first_news
    build: pip install -e .
    path: first_news_node
    outputs:
      - first_news_response
  - id: my_processor
    build: pip install -e .
    path: my_processor_node
    inputs:
      news: first_news/first_news_response
```

Your point source must output:

* Topic: `first_news_response`
* Data: JSON-serializable dict (news payload or error message)
* Metadata:

  ```json
  {
    "error": false,
    "message": "",
    "data": [ { "id": "string", "title": "string", ... } ]
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| user_input  | Any    | (Unused) Placeholder for future compliance  |

### Output Topics

| Topic                | Type  | Description                                  |
| -------------------- | ----- | -------------------------------------------- |
| first_news_response  | dict  | Latest news headlines or error response      |


## License

Released under the MIT License.
