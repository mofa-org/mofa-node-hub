# nekosia_image_fetcher

A Dora-rs node that fetches random anime-style images from the Nekosia API in categories like "catgirl", "foxgirl", or "maid". Receives your chosen category as input and returns an API-supplied image info dict. Use in Dora pipelines to dynamically fetch images based on upstream logic or parameter selection.

## Features
- Fetches random images from the Nekosia anime API by category
- Robust error reporting for invalid categories or API failures
- Easy integration into Dora pipelines with parameterized control

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
  - id: image_fetcher
    build: pip install -e nekosia_image_fetcher
    path: nekosia_image_fetcher
    inputs:
      category: input/category
    outputs:
      - image_result
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
  - id: category_source
    build: pip install your-category-source
    path: your-category-source
    outputs:
      - category
  - id: image_fetcher
    build: pip install -e nekosia_image_fetcher
    path: nekosia_image_fetcher
    inputs:
      category: category_source/category
    outputs:
      - image_result
```

Your point source must output:

* Topic: `category`
* Data: String specifying the category to fetch (e.g., "catgirl")
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Category name from nekosia_endpoints (e.g., 'catgirl', 'maid', 'foxgirl', 'tail-with-ribbon', etc.)"
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                                               |
|----------|--------|-----------------------------------------------------------|
| category | str    | Category name for image fetch (see supported categories)  |

### Output Topics

| Topic        | Type     | Description                                                      |
|--------------|----------|------------------------------------------------------------------|
| image_result | dict     | Dict containing API result: error/message/data/category fields    |

## License

Released under the MIT License.
