# makeup_product_fetcher

Efficient API-based fetcher for cosmetic product data using the Makeup API. Allows dynamic selection of brands and product types with error handling for unsupported inputs.

## Features
- Fetches products for the Maybelline brand
- Fetches Covergirl lipstick products
- Returns meaningful error messages for unsupported queries

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
  - id: makeup_fetcher
    build: pip install -e makeup_product_fetcher
    path: makeup_product_fetcher
    inputs:
      user_input: input/user_input
      brand: input/brand
      product_type: input/product_type
    outputs:
      - products
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
  - id: point_source
    build: pip install your-custom-source
    path: your_point_source
    outputs:
      - brand
      - product_type
      - user_input

  - id: makeup_fetcher
    build: pip install -e makeup_product_fetcher
    path: makeup_product_fetcher
    inputs:
      user_input: point_source/user_input
      brand: point_source/brand
      product_type: point_source/product_type
    outputs:
      - products
      - error
```

Your point source must output:

* Topic: `brand`, `product_type`, `user_input`
* Data: String value for each parameter
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Brand, product_type, or user_input command for the fetcher. Required: brand (maybelline or covergirl), product_type (lipstick if using covergirl)."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                         |
| ------------| ------ | ------------------------------------------------------------------- |
| user_input   | string | Optional free-form input, can be used for pipeline flexibility      |
| brand        | string | Brand name, must be 'maybelline' or 'covergirl'                    |
| product_type | string | Product type, required only for 'covergirl' (must be 'lipstick')    |

### Output Topics

| Topic    | Type      | Description                                        |
| -------- | --------- | -------------------------------------------------- |
| products | list(dict)| List of product records from the Makeup API         |
| error    | string    | Error message if any issue occurs or invalid input  |


## License

Released under the MIT License.
