# coffee_image_node

Random Coffee Image Fetcher Node

## Features
- Fetches a random coffee image from an external API
- Accepts user input parameters for flexible operation
- Designed for integration with Dora/Mofa agent networks

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
  - id: coffee_image
    build: pip install -e .
    path: coffee_image_node
    inputs:
      user_input: input/user_input  # Pass arbitrary input if needed
    outputs:
      - coffee_image_json
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
  - id: your_point_source
    build: pip install your-source
    path: your-point-source
    outputs:
      - user_input
  - id: coffee_image
    build: pip install -e .
    path: coffee_image_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - coffee_image_json
```

Your point source must output:

* Topic: `user_input`
* Data: (Any valid input supported by your pipeline)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Arbitrary user input for coffee image node"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                       |
|-------------|--------|-----------------------------------|
| user_input  | Any    | User parameter to trigger request |

### Output Topics

| Topic              | Type   | Description                         |
|--------------------|--------|-------------------------------------|
| coffee_image_json  | JSON   | Coffee image API response or error  |


## License

Released under the MIT License.
