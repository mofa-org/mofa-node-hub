# ai_cat_gallery

A Dora-rs node for querying and integrating the ai-cats.net API, supporting random cat images, search, similar cats, statistics, themes, and metadata retrieval for cat images via simple message-based commands.

## Features
- Query random cat images from ai-cats.net
- Search cat images with filters (query, theme, size, limit)
- Retrieve similar cats, count by theme, info, and auto-complete query suggestions

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
  - id: ai_cat_gallery_node
    build: pip install -e ai_cat_gallery
    path: ai_cat_gallery
    inputs:
      action: input/action
      user_input: input/user_input
    outputs:
      - random_cat
      - search_results
      - cat_count
      - cat_by_id
      - similar_cats
      - theme_list
      - cat_info
      - search_completion_suggestions
      - error
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
  - id: my_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - action
      - user_input

  - id: ai_cat_gallery_node
    build: pip install -e ai_cat_gallery
    path: ai_cat_gallery
    inputs:
      action: my_input_node/action
      user_input: my_input_node/user_input
    outputs:
      - random_cat
      - search_results
      - cat_count
      - cat_by_id
      - similar_cats
      - theme_list
      - cat_info
      - search_completion_suggestions
      - error
```

Your point source must output:

* Topic: `action`
* Topic: `user_input`
* Data: Both as strings (JSON string for search actions if needed)
* Metadata:

  ```json
  {
    "action": "random | search | count | by_id | similar | themes | info | search_completion",
    "user_input": "Context-dependent string. Use JSON string for search queries; otherwise, provide plain string ID or theme."
  }
  ```

## API Reference

### Input Topics

| Topic     | Type   | Description                                             |
|-----------|--------|--------------------------------------------------------|
| action    | str    | One of ['random', 'search', 'count', 'by_id', 'similar', 'themes', 'info', 'search_completion'] |
| user_input| str    | Input value varies by action; see details below        |

### Output Topics

| Topic                       | Type   | Description                                     |
|-----------------------------|--------|-------------------------------------------------|
| random_cat                  | dict   | Random cat image object                         |
| search_results              | list   | List of cat images matching search              |
| cat_count                   | dict   | Count of cats (optionally by theme)             |
| cat_by_id                   | dict   | Cat image object by ID                          |
| similar_cats                | list   | List of similar cat images to given ID          |
| theme_list                  | list   | List of available cat image themes              |
| cat_info                    | dict   | Metadata/info for a cat image by ID             |
| search_completion_suggestions | list | Autocomplete suggestions for query and theme    |
| error                       | dict   | Error message                                   |


## License

Released under the MIT License.

