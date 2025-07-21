# free_public_api_node

A Dora-rs node for aggregating and exploring open APIs using https://www.freepublicapis.com. Allows workflow-driven discovery, lookup, and randomization of public web APIs.

## Features
- Retrieve up-to-date info for a specific public API by ID
- List multiple available public APIs, with customizable sorting and limits
- Fetch random public API metadata for exploration or pipeline injection

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
  - id: freepublicapi
    build: pip install -e free_public_api_node
    path: free_public_api_node
    inputs:
      mode: input/mode
      api_id: input/api_id
      limit: input/limit
      sort: input/sort
      user_input: input/user_input  # For pipeline chaining (may be unused)
    outputs:
      - single_api_info
      - api_list
      - random_api_info
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
  - id: param_source
    build: pip install your-node
    path: your-node
    outputs:
      - mode
      - api_id
      - limit
      - sort
      - user_input
  - id: freepublicapi
    build: pip install -e free_public_api_node
    path: free_public_api_node
    inputs:
      mode: param_source/mode
      api_id: param_source/api_id
      limit: param_source/limit
      sort: param_source/sort
      user_input: param_source/user_input
    outputs:
      - single_api_info
      - api_list
      - random_api_info
      - error
```

Your point source must output:

* Topic: `mode`, `api_id`, `limit`, `sort`, `user_input`
* Data: String for all parameters (except `limit`, which can be int or string convertible)
* Metadata:

  ```json
  {
    "required": ["mode"],
    "optional": ["api_id", "limit", "sort", "user_input"],
    "mode_options": ["single", "list", "random"]
  }
  ```

## API Reference

### Input Topics

| Topic     | Type   | Description                                   |
|-----------|--------|-----------------------------------------------|
| mode      | String | Mode selection: one of [single, list, random] |
| api_id    | String | API id for lookup (mode: single)              |
| limit     | String | Number of results (mode: list, optional)      |
| sort      | String | Sorting key (mode: list, optional)            |
| user_input| String | For node chaining (optional, always consumed) |

### Output Topics

| Topic            | Type   | Description                                          |
|------------------|--------|------------------------------------------------------|
| single_api_info  | JSON   | Metadata for a specific API                          |
| api_list         | JSON   | Page of multiple API info entries                    |
| random_api_info  | JSON   | Metadata for a randomly-selected API                 |
| error            | String | Error description (on any failure)                   |


## License

Released under the MIT License.
