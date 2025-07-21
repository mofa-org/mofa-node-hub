# joke_api_node

Fetch Yo Mama Jokes with Customizable Category Support From API

## Features
- Fetches jokes from the yomama-jokes.com API
- Supports custom category input with fallback to random
- Easily integrates with Dora nodes via input/output topics

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
  - id: joke_api_node
    build: pip install -e .
    path: joke_api_node
    inputs:
      user_input: input/user_input
      category: input/category
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
  # Your node that sends categories
  - id: category_source
    build: pip install -e .
    path: your_category_node
    outputs:
      - category
      - user_input

  - id: joke_api_node
    build: pip install -e .
    path: joke_api_node
    inputs:
      category: category_source/category
      user_input: category_source/user_input
    outputs:
      - joke_data
```

Your point source must output:

* Topic: `category` (and/or `user_input`)
* Data: String (e.g., "old", "fat", or "random")
* Metadata:

  ```json
  {
    "type": "string",
    "example": "old"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                             |
| ------------| -------| -------------------------------------------------------|
| user_input   | string | General user or pipeline input parameter               |
| category     | string | Category for joke type: 'fat', 'old', or 'random'      |

### Output Topics

| Topic     | Type           | Description                               |
|-----------|----------------|-------------------------------------------|
| joke_data | string/list/dict| Joke (may be a string, list, or dict)     |


## License

Released under the MIT License.
