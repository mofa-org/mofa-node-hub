# teehee_joke_node

Fetch random jokes from [teehee.dev](https://teehee.dev/) and provide them as structured output to other Dora nodes.

## Features
- Retrieves jokes from the [teehee.dev](https://teehee.dev/) API
- Outputs structured joke data with question/answer fields
- Gracefully handles network or API errors

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
  - id: joke_retriever
    build: pip install -e teehee_joke_node
    path: teehee_joke_node
    inputs:
      user_input: input/user_input
    outputs:
      - joke_data
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
  - id: your_node
    build: pip install -e your_node_repo
    path: your_node_repo
    inputs:
      # ...
    outputs:
      - user_input

  - id: joke_retriever
    build: pip install -e teehee_joke_node
    path: teehee_joke_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - joke_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any user input string
* Metadata:

  ```json
  {
    "type": "string",
    "description": "User input, triggers joke fetch"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                         |
| ----------- | ------ | ----------------------------------- |
| user_input  | string | User input; triggers joke retrieval |

### Output Topics

| Topic      | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| joke_data  | object | Returned joke or error information |


## License

Released under the MIT License.
