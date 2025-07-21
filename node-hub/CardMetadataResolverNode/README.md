# card_metadata_resolver

A Dora-rs node that resolves credit/debit card metadata from card number digits. This node queries the [iinapi.com](https://iinapi.com) service to retrieve issuer/bank information and outputs a structured card metadata response or error details.

## Features
- Card metadata lookup using Bin/IIN digits
- Robust error handling with descriptive messages
- Easily integrates with Dora pipelines and other nodes

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
  - id: card_metadata_resolver_node
    build: pip install -e .
    path: card_metadata_resolver
    inputs:
      digits: input/digits
    outputs:
      - card_metadata
      - error
    env:
      IIN_API_KEY: "your_iin_api_key_here"
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
  - id: my_digits_source
    build: pip install your-source-node
    path: my-source
    outputs:
      - digits
  - id: card_metadata_resolver_node
    build: pip install -e .
    path: card_metadata_resolver
    inputs:
      digits: my_digits_source/digits
    outputs:
      - card_metadata
      - error
```

Your point source must output:

* Topic: `digits`
* Data: Card BIN/IIN digits as string (e.g., "45717360")
* Metadata:
  ```json
  {
    "example": "45717360",
    "description": "Bank Identification (or Issuer Identification) Number as string."
  }
  ```

## API Reference

### Input Topics

| Topic  | Type   | Description                                |
| ------ | ------ | ------------------------------------------ |
| digits | string | Card BIN/IIN digits (e.g., "45717360")     |

### Output Topics

| Topic         | Type        | Description                                   |
| -------------| ----------- | --------------------------------------------- |
| card_metadata | dict/string | Card and issuer metadata as received from API |
| error         | string      | Error message, if lookup fails                |


## License

Released under the MIT License.
