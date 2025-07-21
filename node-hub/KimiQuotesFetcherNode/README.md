# kimi_quotes_node

A Dora-rs node that fetches a random Kimi Räikkönen quote from an online API and exposes it as an output topic. Intended for use as a demonstration or to provide fun/novelty output in multimodal pipelines.

## Features
- Fetches random Kimi Räikkönen quotes via HTTP
- Simple API and integration for Dora-compatible pipelines
- Handles request errors gracefully and returns error info if needed

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
  - id: kimi-quote
    build: pip install -e .
    path: kimi_quotes_node
    outputs:
      - kimi_quote
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
  - id: kimi-quote
    build: pip install -e .
    path: kimi_quotes_node
    outputs:
      - kimi_quote
  - id: downstream-node
    build: pip install your-consumer-node
    path: your_consumer_node
    inputs:
      kimi_quote: kimi-quote/kimi_quote
```

Your point source must output:

* Topic: `points_to_track`
* Data: Flattened array of coordinates
* Metadata:

  ```json
  {
    "num_points": 0,
    "dtype": "float32",
    "shape": [0, 2]
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description           |
| ----------- | ------ | --------------------- |
| user_input  | any    | Optional downstream parameter |

### Output Topics

| Topic       | Type       | Description                            |
| ----------- | ----------| -------------------------------------- |
| kimi_quote  | dict      | Fetched Kimi Räikkönen quote or error  |
|             |           |                                        |


## License

Released under the MIT License.
