# dog_api_node

DogApiNode: Dora-rs node for fetching data from the Dog CEO API

## Features
- List all available dog breeds
- Retrieve a random dog image
- Get a random image of the Affenpinscher breed

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
  - id: dog_api_node
    build: pip install -e .
    path: dog_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - breeds_list
      - random_dog_image
      - affenpinscher_image
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
  - id: orchestrator
    build: pip install -e your-orchestrator
    path: your-orchestrator
    outputs:
      - user_input
  - id: dog_api_node
    build: pip install -e .
    path: dog_api_node
    inputs:
      user_input: orchestrator/user_input
    outputs:
      - breeds_list
      - random_dog_image
      - affenpinscher_image
      - error
```

Your point source must output:

* Topic: `user_input`
* Data: The string operation you wish to call, e.g. "list_breeds", "random_image", or "affenpinscher_image"
* Metadata:

  ```json
  {
    "type": "string",
    "description": "API operation to perform: list_breeds, random_image, affenpinscher_image."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                   |
| ---------- | ------ | ------------------------------------------------------------- |
| user_input | string | Operation to perform: list_breeds, random_image, affenpinscher_image |

### Output Topics

| Topic              | Type   | Description                                |
| ------------------ | ------ | ------------------------------------------ |
| breeds_list        | dict   | Dictionary with all dog breeds             |
| random_dog_image   | dict   | Random dog image data from API             |
| affenpinscher_image| dict   | Random Affenpinscher breed image from API  |
| error              | dict   | Error message, if any                      |


## License

Released under the MIT License.
