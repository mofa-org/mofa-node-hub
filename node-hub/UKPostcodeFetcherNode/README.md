# uk_postcode_fetcher

Fetch UK postcode information via [postcodes.io](https://postcodes.io/). Provides easy querying either for a random postcode or information about a specific postcode string.

## Features
- Fetches random UK postcode details
- Fetches information for a specific postcode string
- Clean separation of input validation, error handling, and response structure

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
  - id: uk_postcode_fetcher
    build: pip install -e uk_postcode_fetcher
    path: uk_postcode_fetcher
    inputs:
      action: input/action
      postcode: input/postcode
    outputs:
      - postcode_result
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
  - id: your_input_node
    outputs:
      - action
      - postcode
  - id: uk_postcode_fetcher
    build: pip install -e uk_postcode_fetcher
    path: uk_postcode_fetcher
    inputs:
      action: your_input_node/action
      postcode: your_input_node/postcode
    outputs:
      - postcode_result
```

Your point source must output:

* Topic: `postcode_result`
* Data: JSON with postcode data or error message
* Metadata:

  ```json
  {
    "description": "Results from postcode API. Contains full response from postcodes.io or error keys on failure."
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                        |
| -------- | ------ | ---------------------------------- |
| action   | str    | 'random' to fetch a random postcode, 'specific' to fetch a given postcode |
| postcode | str    | Postcode string (required if action is 'specific') |

### Output Topics

| Topic           | Type  | Description                                            |
| -------------- | ----- | ------------------------------------------------------ |
| postcode_result | dict  | Dict containing full response from postcodes.io or error key |


## License

Released under the MIT License.
