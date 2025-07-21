# openfoodfacts_node

A Dora node that fetches product data for Nutella (barcode: 3017620422003) from the OpenFoodFacts API. Designed for invocation as part of a Dora pipeline—on receiving a parameter, it queries the API and outputs structured product information or error details.

## Features
- Fetches food product data from OpenFoodFacts
- Outputs full JSON product results or friendly error messages
- Simple API for downstream integration

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: openfoodfacts
    build: pip install -e .
    path: openfoodfacts_node
    inputs:
      user_input: input/user_input
    outputs:
      - api_output
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
  - id: user_input_node
    build: pip install my-user-input-node
    path: my_user_input_node
    outputs:
      - user_input
  - id: openfoodfacts
    build: pip install -e .
    path: openfoodfacts_node
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - api_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any (used to trigger fetching Nutella data)
* Metadata:

  ```json
  {
    "type": "trigger",
    "description": "This parameter triggers the OpenFoodFactsNode to fetch product data."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                 |
| ---------- | ------ | --------------------------- |
| user_input | any    | Triggers fetching from API. |

### Output Topics

| Topic      | Type           | Description                                                    |
| ---------- | --------------| ---------------------------------------------------------------|
| api_output | dict (JSON)    | API response data or error details from OpenFoodFacts API.      |


## License

Released under the MIT License.

````
