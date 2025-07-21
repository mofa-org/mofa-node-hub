# korean_json_node

Easy Korean JSON API Fetch Node for MOFA Agents

## Features
- Fetches public JSON data from https://koreanjson.com (`todos`, `comments`, `users`, or `posts`)
- Simple input interface for selecting resource type
- Error handling with informative messages

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
  - id: korean_json_node
    build: pip install -e .
    path: korean_json_node
    inputs:
      resource_type: input/resource_type  # Should be one of: 'todos', 'comments', 'users', 'posts'
    outputs:
      - korean_json_output
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
  - id: my_node
    build: pip install -e my_node
    path: my_node
    outputs:
      - resource_type  # Should send one of: 'todos', 'comments', 'users', 'posts'

  - id: korean_json_node
    build: pip install -e .
    path: korean_json_node
    inputs:
      resource_type: my_node/resource_type
    outputs:
      - korean_json_output
```

Your point source must output:

* Topic: `resource_type`
* Data: String ('todos', 'comments', 'users', or 'posts')
* Metadata:

  ```json
  {
    "type": "string",
    "allowed_values": ["todos", "comments", "users", "posts"]
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                                    |
| --------------- | ------ | -------------------------------------------------------------- |
| resource_type   | str    | Resource to fetch: one of 'todos', 'comments', 'users', 'posts'|

### Output Topics

| Topic               | Type        | Description                                            |
| ------------------- | ----------- | ------------------------------------------------------ |
| korean_json_output  | list/dict   | API response data or error object (on failure)         |

## License

Released under the MIT License.
