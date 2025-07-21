# CatPhotoNode

Fetch random cat photos via HTTP for your Dora-rs/Mofa pipelines.

## Features
- Fetches random cat photos from the internet
- Outputs photo URL and HTTP status as JSON
- Robust error handling with stateless execution

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
  - id: cat_photo_node
    build: pip install -e cat_photo_node
    path: cat_photo_node
    inputs:
      user_input: input/user_input
    outputs:
      - cat_photo
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
  - id: my_trigger
    build: pip install <your-trigger-node>
    path: <your-trigger-node>
    outputs:
      - user_input

  - id: cat_photo_node
    build: pip install -e cat_photo_node
    path: cat_photo_node
    inputs:
      user_input: my_trigger/user_input
    outputs:
      - cat_photo
```

Your point source must output:

* Topic: `user_input`
* Data: any (can be null or a trigger value)
* Metadata:

  ```json
  {
    "description": "Any value to trigger fetching a cat photo. Not used by node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type | Description                                     |
| ---------- | ---- | ----------------------------------------------- |
| user_input | any  | Input to trigger fetching a photo (can be null) |

### Output Topics

| Topic     | Type | Description                                                         |
| --------- | ---- | ------------------------------------------------------------------- |
| cat_photo | JSON | Output dict: {'url', 'status_code'} or {'error': message}           |


## License

Released under the MIT License.
