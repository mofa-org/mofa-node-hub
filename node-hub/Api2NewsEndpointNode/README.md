# api2news_endpoint

A Dora node for fetching the latest news using the api2.news HTTP endpoint. This node allows seamless integration of real-time news article fetching into Dora-rs pipelines, sending downstream the latest results as structured JSON or text. Plug it into your workflows to stay continuously informed with minimal configuration.

## Features
- Fetches the latest news articles from https://endpoint.api2.news/
- Outputs news article data in native JSON or plain text
- Gracefully handles connection and API errors for robust operation

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
  - id: news_fetcher
    build: pip install -e api2news_endpoint
    path: api2news_endpoint
    inputs:
      user_input: input/user_input
    outputs:
      - news_articles
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
  - id: my_input_node
    build: pip install -e my_input_node
    path: my_input_node
    outputs:
      - user_input
  - id: news_fetcher
    build: pip install -e api2news_endpoint
    path: api2news_endpoint
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - news_articles
```

Your point source must output:

* Topic: `user_input`
* Data: any input (user_input is not used but must be present for interface compliance)
* Metadata:

  ```json
  {
    "description": "Any payload; placeholder to satisfy input requirement."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type      | Description                             |
| ---------- | --------- | --------------------------------------- |
| user_input | any       | Placeholder required by interface.      |

### Output Topics

| Topic         | Type    | Description                                             |
| ------------- | ------- | ----------------------------------------------------- |
| news_articles | object  | Latest news articles as JSON or raw text; error report |


## License

Released under the MIT License.
