# magic_eight_ball_node

A Dora-rs node that provides responses from an online Magic 8-Ball API on demand. Supports easy integration with other Dora nodes and parameterized queries for interaction.

## Features
- On-demand fortune responses using the Magic 8-Ball cloud API
- Easy integration with other Dora nodes via messaging
- Wraps the API in a Dora/Mofa agent interface for straightforward pipeline use

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
  - id: magic_8_ball
    build: pip install -e .
    path: magic_eight_ball_node
    inputs:
      user_input: input/user_input
    outputs:
      - magic_eight_ball_response
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
  - id: question_source
    build: pip install your-node
    path: question_source
    outputs:
      - user_input
  - id: magic_8_ball
    build: pip install -e .
    path: magic_eight_ball_node
    inputs:
      user_input: question_source/user_input
    outputs:
      - magic_eight_ball_response
```

Your point source must output:

* Topic: `user_input`
* Data: String or JSON serializable input (ignored by API, but required for pipeline call)
* Metadata:

  ```json
  {
    "description": "String or dict containing the user's question (API ignores value)."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                  |
|-------------|--------|--------------------------------------------------------------|
| user_input  | Any    | Required for triggering a request. Value is ignored by API.   |

### Output Topics

| Topic                     | Type  | Description                                  |
|---------------------------|-------|----------------------------------------------|
| magic_eight_ball_response | dict  | Magic 8-Ball API response (JSON/dict/string) |


## License

Released under the MIT License.
