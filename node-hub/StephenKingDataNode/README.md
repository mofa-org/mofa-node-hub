# stephen_king_node

A Dora-rs node providing comprehensive Stephen King universe data (books, villains, shorts) via a RESTful API. Supports integration into pipelines requiring real-time knowledge about Stephen King's works.

## Features
- Fetch Stephen King's books, villains, and short stories from a public API
- Seamless integration with Dora workflows and other nodes
- Single-command output for easy downstream consumption

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
  - id: stephen_king
    build: pip install -e .
    path: stephen_king_node
    inputs:
      user_input: input/user_input
    outputs:
      - stephen_king_data
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
  - id: stephen_king
    build: pip install -e .
    path: stephen_king_node
    inputs:
      user_input: input/user_input
    outputs:
      - stephen_king_data

  - id: your_node
    build: pip install your-node
    path: your_node
    inputs:
      stephen_king: stephen_king/stephen_king_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (serves as a trigger)
* Metadata:

  ```json
  {
    "usage": "Pass any value to 'user_input' input; serves only as an API call trigger."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                        |
| ----------- | ------ | -------------------------------------------------- |
| user_input  | Any    | Triggers fetch of Stephen King API data            |

### Output Topics

| Topic              | Type   | Description                                       |
| ------------------ | ------ | ------------------------------------------------- |
| stephen_king_data  | dict   | Dict with keys `books`, `villains`, `shorts`. Each is result from API.
|

## License

Released under the MIT License.

