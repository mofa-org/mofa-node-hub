# jellybean_api_node

A Dora-rs node for querying the public Jelly Belly Beans API. Fetches a list of available jelly bean flavors and detailed information for a specific bean using REST endpoints.

## Features
- Fetches the full list of jelly bean flavors from Jelly Belly Wiki API
- Retrieves detailed information for a specific jelly bean (example: bean with id=1)
- Returns results as structured outputs for downstream processing

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
  - id: jellybean_api_node
    build: pip install -e .
    path: jellybean_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - beans_list
      - bean_detail
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
  - id: example_frontend
    build: pip install your-package  # hypothetical upstream node
    path: example_frontend_path
    outputs:
      - user_input
  - id: jellybean_api_node
    build: pip install -e .
    path: jellybean_api_node
    inputs:
      user_input: example_frontend/user_input
    outputs:
      - beans_list
      - bean_detail
```

Your point source must output:

* Topic: `user_input`
* Data: (any serializable object, may be null for compatibility)
* Metadata:

  ```json
  {
    "description": "Optional placeholder for user commands or triggers. Typically not required by this node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                           |
| ----------- | ------- | ----------------------------------------------------- |
| user_input  | Any     | Placeholder input for upstream compatibility. Not used |

### Output Topics

| Topic         | Type   | Description                                               |
| ------------- | ------ | --------------------------------------------------------- |
| beans_list    | dict   | List of all jelly bean flavors fetched from the API       |
| bean_detail   | dict   | Details for the bean with id=1 as fetched from the API    |


## License

Released under the MIT License.

````