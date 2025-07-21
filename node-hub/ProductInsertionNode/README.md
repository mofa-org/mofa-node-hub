# product_insertion_node

Automated Product Insertion Node for the Predic8 Shop API

## Features
- Accepts product data as a JSON string parameter
- Inserts a product into the Predic8 Shop API using HTTP POST
- Returns structured API response with status code and result details

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
  - id: product_insertion
    path: product_insertion_node
    build: pip install -e .
    inputs:
      product_data: input/product_data
    outputs:
      - product_insertion_result
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
  - id: product_creator
    path: your-product-source
    build: pip install -e your-product-source
    outputs:
      - product_data
  - id: product_insertion
    path: product_insertion_node
    build: pip install -e .
    inputs:
      product_data: product_creator/product_data
    outputs:
      - product_insertion_result
```

Your point source must output:

* Topic: `product_data`
* Data: JSON string with product fields (name, price, etc)
* Metadata:

  ```json
  {
    "content_type": "application/json",
    "description": "Product object as JSON string"
  }
  ```

## API Reference

### Input Topics

| Topic          | Type     | Description                                    |
| -------------- | -------- | ---------------------------------------------- |
| product_data   | string   | JSON string representing product to be created |

### Output Topics

| Topic                   | Type  | Description                                        |
| ----------------------- | ----- | -------------------------------------------------- |
| product_insertion_result| dict  | API response, status code, any error or raw reply  |


## License

Released under the MIT License.
