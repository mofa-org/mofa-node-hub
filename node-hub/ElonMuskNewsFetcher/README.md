# elon_musk_news

Fetch the latest Elon Musk news headlines from https://elonmu.sh/api and output them as structured JSON using the MOFA agent architecture.

## Features
- Fetches real-time Elon Musk news articles from a public API
- Robust error-handling with structured error messages
- Easy integration as a MOFA dataflow agent

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
  - id: elon_musk_news
    build: pip install -e .
    path: elon_musk_news
    inputs:
      user_input: input/user_input  # Dummy input for dataflow consistency
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
  # Your data-triggering node
  - id: input
    build: pip install your-trigger-node
    path: your-trigger-node
    outputs:
      - user_input

  - id: elon_musk_news
    build: pip install -e .
    path: elon_musk_news
    inputs:
      user_input: input/user_input
    outputs:
      - news_articles
```

Your point source must output:

* Topic: `user_input`
* Data: Any dummy data type (for triggering)
* Metadata:

  ```json
  {
    "type": "trigger",
    "description": "Dummy input for dataflow orchestration"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                              |
|-------------|--------|------------------------------------------|
| user_input  | any    | Trigger (not used in logic, only for orchestration) |

### Output Topics

| Topic         | Type   | Description                                    |
|---------------|--------|------------------------------------------------|
| news_articles | object | JSON with Elon Musk news articles or error info |


## License

Released under the MIT License.
