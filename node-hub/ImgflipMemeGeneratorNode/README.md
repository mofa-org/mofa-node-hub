# imgflip_meme_node

Query Imgflip's Meme API and expose meme template metadata for downstream Dora-rs applications.

## Features
- Fetches Imgflip meme template catalog via API
- Simple Dora node interface for integration
- Robust error handling with serializable JSON output

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
  - id: meme_fetcher
    build: pip install -e imgflip_meme_node
    path: imgflip_meme_node
    inputs:
      user_input: input/user_input  # Dummy input for framework compatibility
    outputs:
      - memes_api_response
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
  - id: meme_fetcher
    build: pip install -e imgflip_meme_node
    path: imgflip_meme_node
    inputs:
      user_input: input/user_input  # Required for API trigger; can be any data.
    outputs:
      - memes_api_response
  - id: consumer_node
    build: pip install your-consumer
    path: path/to/your-consumer
    inputs:
      memes_api_response: meme_fetcher/memes_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any dummy value (string, int, etc.)
* Metadata:

  ```json
  {
    "dtype": "str",
    "desc": "Dummy trigger for Imgflip meme node"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                  |
| ---------- | ------ | --------------------------- |
| user_input | any    | Dummy input; triggers fetch. |

### Output Topics

| Topic               | Type   | Description                           |
| ------------------- | ------ | ------------------------------------- |
| memes_api_response  | dict   | JSON API response or error message.   |


## License

Released under the MIT License.
