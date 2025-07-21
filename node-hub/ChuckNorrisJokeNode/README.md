# chuck_norris_joke_node

A Dora-rs node for fetching Chuck Norris jokes from the public API, with optional category-based filtering.

## Features
- Retrieves a random Chuck Norris joke from https://api.chucknorris.io
- Supports optional category specification via the `category` input parameter
- Outputs joke text and joke ID or error message

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
  - id: chuck_norris_joke_node
    build: pip install -e chuck_norris_joke_node
    path: chuck_norris_joke_node
    inputs:
      category: input/category
    outputs:
      - joke_output
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
  - id: my_category_source
    build: pip install -e my-category-node
    path: my-category-node
    outputs:
      - category

  - id: chuck_norris_joke_node
    build: pip install -e chuck_norris_joke_node
    path: chuck_norris_joke_node
    inputs:
      category: my_category_source/category
    outputs:
      - joke_output
```

Your point source must output:

* Topic: `category`
* Data: string (category name)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Joke category (e.g. animal, dev, food, etc)",
    "optional": true
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                 |
|----------|--------|-----------------------------|
| category | str    | Optional joke category name |

### Output Topics

| Topic       | Type                | Description                                     |
|-------------|---------------------|-------------------------------------------------|
| joke_output | dict or str         | The returned joke object or error information    |


## License

Released under the MIT License.
