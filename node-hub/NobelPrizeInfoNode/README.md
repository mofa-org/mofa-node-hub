# nobel_prize_node

NobelPrizeInfoNode: Dora node for fetching and streaming Nobel Prize API data

## Features
- Fetches data from Nobel Prize API (prizes, laureates)
- Returns recent results via Dora output topics
- Handles API failures and provides structured error reporting

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
  - id: nobel_prize_node
    build: pip install -e .
    path: nobel_prize_node
    inputs:
      user_input: input/user_input
    outputs:
      - nobel_api_results
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
  - id: your_node
    build: pip install -e your_node
    path: your_node
    outputs:
      - user_input
  - id: nobel_prize_node
    build: pip install -e nobel_prize_node
    path: nobel_prize_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - nobel_api_results
```

Your point source must output:

* Topic: `user_input`
* Data: String or parameters for trigger (can be any data your pipeline provides)
* Metadata:

  ```json
  {
    "data_type": "string",
    "description": "Input parameter, used to trigger Nobel Prize API fetch. Value is ignored by default node implementation."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                    |
| ----------- | ------ | ---------------------------------------------- |
| user_input  | Any    | Input parameter to trigger API fetch (ignored) |

### Output Topics

| Topic             | Type          | Description                                   |
| ----------------- | ------------- | --------------------------------------------- |
| nobel_api_results | dict or error | Contains fetched data or error information    |

## License

Released under the MIT License.
