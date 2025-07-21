# current_year_node

Retrieve the Current Year from an Online API Node

## Features
- Retrieves the current year by querying a public API (`getfullyear.com`).
- Returns results in a structured dictionary (`{"year": year}` or error description).
- Handles API and network errors gracefully, always outputs a result for dataflow reliability.

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
  - id: current_year
    build: pip install -e .
    path: current_year_node
    inputs:
      user_input: input/user_input
    outputs:
      - current_year
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
    path: your_node
    outputs:
      - user_input
  - id: current_year
    build: pip install -e .
    path: current_year_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - current_year
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (as required for triggering the year fetch)
* Metadata:

  ```json
  {
    "description": "Trigger for retrieving the current year, can be any value."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                                   |
|-------------|----------|-----------------------------------------------|
| user_input  | any      | Trigger for retrieving the current year. Value may be arbitrary, only used to trigger fetch. |

### Output Topics

| Topic         | Type           | Description                                            |
|---------------|----------------|--------------------------------------------------------|
| current_year  | dict           | `{ "year": year }` on success, `{ "error": msg }` on failure. |


## License

Released under the MIT License.
