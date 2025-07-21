# crypto_data_node

Query live and historical Bitcoin and cryptocurrency data via CoinGecko public API.

## Features
- Retrieve historical Bitcoin price for a specific date
- Search for any cryptocurrency using a keyword
- Simple Dora node integration with clear input/output parameter mapping

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
  - id: crypto_data
    build: pip install -e crypto_data_node
    path: crypto_data_node
    inputs:
      operation: input/operation
      date: input/date
      query: input/query
    outputs:
      - api_result
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
  - id: user_input
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - operation
      - date
      - query
  - id: crypto_data
    build: pip install -e crypto_data_node
    path: crypto_data_node
    inputs:
      operation: user_input/operation
      date: user_input/date
      query: user_input/query
    outputs:
      - api_result
  # Your downstream node
  - id: result_consumer
    build: pip install your-consumer
    path: your-consumer
    inputs:
      api_result: crypto_data/api_result
```

Your point source must output:

* Topic: `operation`, `date`, `query`
* Data: Strings as required for operation (see below)
* Metadata:

  ```json
  {
    "operation": "get_price" | "search", // Which API operation to perform
    "date": "dd-mm-yyyy", // Required only for get_price
    "query": "keyword",    // Required only for search
    "optional": true
  }
  ```

## API Reference

### Input Topics

| Topic      | Type | Description |
|------------|------|-------------|
| operation  | str  | Operation to perform: 'get_price' or 'search' |
| date       | str  | Date in 'dd-mm-yyyy' format (required for 'get_price') |
| query      | str  | Search keyword (required for 'search') |

### Output Topics

| Topic      | Type | Description |
|------------|------|-------------|
| api_result | dict | API response or error details |

## License

Released under the MIT License.
