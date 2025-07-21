# mexican_zipcode_node

Simple Dora node for batch-fetching data from the SEPOMEX Mexican zip code API.

## Features
- Groups multiple SEPOMEX REST endpoints (municipalities, zip codes, states, cities) in a single output
- Retries and safe error reporting for endpoint queries
- Simple integration as a stateless Dora node

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
  - id: zipcode_fetcher
    build: pip install -e .
    path: mexican_zipcode_node
    inputs:
      user_input: input/user_input
    outputs:
      - zipcode_api_data
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
    build: pip install your-node
    path: your-node
    outputs:
      - user_input

  - id: zipcode_fetcher
    build: pip install -e .
    path: mexican_zipcode_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - zipcode_api_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (compatibility; ignored)
* Metadata:

  ```json
  {
    "type": "any",
    "desc": "Placeholder, ignored by node"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                  |
| ---------- | ------ | ----------------------------|
| user_input | any    | Placeholder, ignored content |

### Output Topics

| Topic            | Type   | Description                                        |
| ---------------- | ------ | --------------------------------------------------|
| zipcode_api_data | dict   | Results for all REST endpoints or error objects     |


## License

Released under the MIT License.
