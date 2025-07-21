# jokefather_node

A Dora-rs node that fetches a random joke from jokefather.com on demand and outputs it in a machine-readable format for downstream nodes or visualization.

## Features
- Fetches random jokes in real time from jokefather.com
- Seamless integration as a Dora MofaAgent node
- Error handling for API/network failures with structured output

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
  - id: jokefather_node
    build: pip install -e .
    path: jokefather_node
    inputs:
      user_input: input/user_input
    outputs:
      - joke_response
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
  - id: user_source
    build: pip install your-user-input-node
    path: user_input_node
    outputs:
      - user_input
  - id: jokefather_node
    build: pip install -e .
    path: jokefather_node
    inputs:
      user_input: user_source/user_input
    outputs:
      - joke_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable user input, typically a string or dict (can be empty if not required)
* Metadata:

  ```json
  {
    "type": "string or dict",
    "description": "Trigger input; actual content is ignored but required to activate joke fetch."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                |
| ----------- | ------- | ------------------------------------------ |
| user_input  | Any     | Ignored content, triggers joke fetch       |

### Output Topics

| Topic         | Type    | Description                                        |
| ------------- | ------- | -------------------------------------------------- |
| joke_response | dict    | Joke from API as JSON dict, or error message dict  |


## License

Released under the MIT License.
