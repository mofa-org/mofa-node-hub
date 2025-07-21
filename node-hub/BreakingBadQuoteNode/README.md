# breaking_bad_quote_node

A Dora-rs/Mofa node for fetching random quotes from the Breaking Bad Quotes API. Supports both single and batch retrieval; errors are always reported in the output for robust chaining.

## Features
- Fetches a single random Breaking Bad quote via public API
- Fetches a batch of five random Breaking Bad quotes in one call
- Outputs structured data including error reporting, suitable for node-based pipelines

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
  - id: breaking_bad_quote_node
    build: pip install -e .
    path: breaking_bad_quote_node
    inputs:
      user_input: any_node/user_input
    outputs:
      - breaking_bad_quotes
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
  - id: custom_source
    build: pip install your-node
    path: your-node-path
    outputs:
      - user_input

  - id: breaking_bad_quote_node
    build: pip install -e .
    path: breaking_bad_quote_node
    inputs:
      user_input: custom_source/user_input
    outputs:
      - breaking_bad_quotes

  - id: downstream_consumer
    build: pip install your-consumer-node
    path: your-consumer-path
    inputs:
      breaking_bad_quotes: breaking_bad_quote_node/breaking_bad_quotes
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable trigger (string, dict, etc.)
* Metadata:

  ```json
  {
    "type": "string or dict", 
    "purpose": "triggers the quote-fetching process; not used inside the agent"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type          | Description                          |
| ------------| ------------- | ------------------------------------ |
| user_input  | any           | Triggers the quote-fetching process. |

### Output Topics

| Topic                 | Type     | Description                                                                              |
| --------------------- | -------  | ---------------------------------------------------------------------------------------- |
| breaking_bad_quotes   | dict     | Dict with keys: single_quote (list), five_quotes (list), error (str or None; error info) |


## License

Released under the MIT License.
