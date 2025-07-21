# CryptoHistoryQueryNode

Mofa agent node for querying real-time and historical cryptocurrency data using the CoinGecko API. Supports dynamic search and price history lookup in a Dora/Mofa pipeline.

## Features
- Search cryptocurrencies by name or symbol (fuzzy search, via CoinGecko)
- Get historical price and info for Bitcoin by specific date
- Automatic error messaging and parameter validation

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
  - id: crypto_query
    build: pip install -e crypto_history_query
    path: crypto_history_query
    inputs:
      query: input/query
      date: input/date
    outputs:
      - search_results
      - history_result
      - error
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
  - id: your_point_source
    build: pip install your-point-source-node
    path: your-point-source-node
    outputs:
      - query
      - date

  - id: crypto_query
    build: pip install -e crypto_history_query
    path: crypto_history_query
    inputs:
      query: your_point_source/query
      date: your_point_source/date
    outputs:
      - search_results
      - history_result
      - error
```

Your point source must output:

* Topic: `query` or `date`
* Data: String (query for coin search, or date as `'DD-MM-YYYY'`)
* Metadata:

  ```json
  {
    "type": "string",
    "example_query": "bitcoin",
    "example_date": "01-05-2024"
  }
  ```

## API Reference

### Input Topics

| Topic  | Type   | Description                            |
|--------|--------|----------------------------------------|
| query  | string | Query string to search for crypto coins |
| date   | string | Date string in 'DD-MM-YYYY' format for bitcoin price history |

### Output Topics

| Topic           | Type | Description                                                              |
|-----------------|------|--------------------------------------------------------------------------|
| search_results  | dict | JSON search results from CoinGecko for the query                         |
| history_result  | dict | Historical price/info for bitcoin for the specified date (from CoinGecko) |
| error           | dict/string | Error message, if any invalid parameter or exception occurs            |


## License

Released under the MIT License.
