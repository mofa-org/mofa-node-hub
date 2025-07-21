# cat_image_fetcher

A Dora-rs compatible node for fetching random cat image URLs using TheCatAPI. This node is ideal for workflows or pipelines that require random cat images, either for testing, fun, or sample data generation.

## Features
- Fetches random cat image URLs from TheCatAPI
- Respects the configurable 'limit' parameter for the number of images fetched
- Returns a JSON-serializable list of image URLs

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
  - id: cat_fetcher
    build: pip install -e .
    path: cat_image_fetcher
    inputs:
      user_input: external/user_input # Optional
      limit: external/limit          # Optional
    outputs:
      - cat_image_urls
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
  - id: my_input_node
    # ... Configure your node to output "limit" or "user_input"
    outputs:
      - limit
      - user_input
  - id: cat_fetcher
    build: pip install -e .
    path: cat_image_fetcher
    inputs:
      user_input: my_input_node/user_input  # Optional
      limit: my_input_node/limit            # Optional
    outputs:
      - cat_image_urls
```

Your point source must output:

* Topic: `limit`
* Data: Integer as string (e.g., "5")
* Metadata:

  ```json
  {
    "description": "Number of cat images to fetch",
    "type": "string",
    "example": "3"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ----------| ------ | ----------------------------------------- |
| user_input| string | Unused/optional passthrough for compatibility |
| limit     | string | Number of cat images to fetch (as string) |

### Output Topics

| Topic           | Type            | Description                         |
| ---------------| --------------- | ----------------------------------- |
| cat_image_urls  | list of strings | List of fetched cat image URLs      |


## License

Released under the MIT License.
