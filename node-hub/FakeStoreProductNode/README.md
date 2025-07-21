# fakestore_node

A Dora node for interfacing with the public FakeStoreAPI, enabling product, category, and sorted listing retrieval for e-commerce prototyping and AI-powered shopping assistants.

## Features
- Fetch all available products from FakeStoreAPI
- Retrieve a single product by ID (Product 1)
- List all product categories and get products sorted in descending order

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
  - id: fakestore
    build: pip install -e fakestore_node
    path: fakestore_node
    inputs:
      action: input/action     # Supply desired action: get_all_products, get_product_1, etc.
    outputs:
      - all_products
      - product_1
      - all_categories
      - sorted_products
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
  - id: your_controller
    build: pip install your-controller
    path: your-controller
    outputs:
      - action
  - id: fakestore
    build: pip install -e fakestore_node
    path: fakestore_node
    inputs:
      action: your_controller/action
    outputs:
      - all_products
      - product_1
      - all_categories
      - sorted_products
```

Your point source must output:

* Topic: `action`
* Data: string with one of
    - `get_all_products`
    - `get_product_1`
    - `get_all_categories`
    - `get_products_sorted_desc`
* Metadata:

  ```json
  {
    "type": "string",
    "allowed": [
      "get_all_products",
      "get_product_1",
      "get_all_categories",
      "get_products_sorted_desc"
    ]
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                                        |
| ------- | ------ | -------------------------------------------------- |
| action  | string | Action string: One of the 4 allowed API behaviors  |

### Output Topics

| Topic           | Type        | Description                                             |
| --------------  | ---------- | ------------------------------------------------------- |
| all_products    | list/dict   | List of all products from the FakeStoreAPI              |
| product_1       | dict        | Information about product with ID=1                     |
| all_categories  | list        | List of all product categories from the API             |
| sorted_products | list/dict   | List of products sorted by descending order             |
| error           | dict        | Error information if action is invalid or on exception  |

## License

Released under the MIT License.
