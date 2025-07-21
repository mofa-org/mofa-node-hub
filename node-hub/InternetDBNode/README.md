# internetdb_node

Minimal Shodan InternetDB lookup Dora-rs node

## Features
- Performs Shodan InternetDB lookups on a given IP address
- Retries queries for resilience with timeout configuration
- Compatible with Dora-rs orchestration and MOFA agent interface

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
  - id: internetdb
    build: pip install -e .
    path: .
    inputs:
      user_input: input/user_input
    outputs:
      - internetdb_result
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
  - id: your_input
    build: pip install your_input_node
    path: your_input_node
    outputs:
      - user_input

  - id: internetdb
    build: pip install -e .
    path: .
    inputs:
      user_input: your_input/user_input
    outputs:
      - internetdb_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (dummy input or IP address for future extensions)
* Metadata:

  ```json
  {
    "description": "Dummy parameter."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type      | Description  |
| ----------- | --------- | ------------ |
| user_input  | any       | Dummy param for orchestration compatibility |

### Output Topics

| Topic              | Type            | Description                                     |
| ------------------ | --------------- | ----------------------------------------------- |
| internetdb_result  | str/dict/list   | Raw result or error from Shodan InternetDB query |


## License

Released under the MIT License.
