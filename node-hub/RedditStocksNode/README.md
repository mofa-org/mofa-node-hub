# reddit_stocks_node

Fetch trending Reddit stock sentiment (tickers and scores) from the public tradestie.com Reddit Stocks API and expose the results in a Dora-compatible node format.

## Features
- Pulls latest trending stock sentiment data from Reddit via Tradestie public API
- Fault-tolerant: outputs error details if API call fails
- Seamless integration as a data source node in Dora/MOFA pipelines

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
  - id: reddit-stocks
    build: pip install -e reddit_stocks_node
    path: reddit_stocks_node
    inputs:
      user_input: dora/parameters/user_input # Placeholder for dataflow compatibility
    outputs:
      - reddit_stocks
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
  - id: reddit-stocks
    build: pip install -e reddit_stocks_node
    path: reddit_stocks_node
    inputs:
      user_input: dora/parameters/user_input # Required for compatibility
    outputs:
      - reddit_stocks
  - id: custom-consumer
    build: pip install -e your_custom_node
    path: your_custom_node
    inputs:
      reddit_data: reddit-stocks/reddit_stocks
```

Your point source must output:

* Topic: `reddit_stocks`
* Data: List of stocks or error dict
* Metadata:

  ```json
  {
    "type": "list|dict",
    "description": "Reddit trending stocks response or error message"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | any    | Placeholder for dataflow compat; not required |

### Output Topics

| Topic         | Type         | Description                                    |
| ------------- | ------------ | ---------------------------------------------- |
| reddit_stocks | list or dict | Trending Reddit stocks or error information     |


## License

Released under the MIT License.
