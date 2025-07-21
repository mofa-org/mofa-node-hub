# mealdb_node_connector

A Dora-rs node for querying TheMealDB public recipe API via flexible, easy-to-use actions for meal search, filtering, and exploration from your dataflow, with robust error handling.

## Features
- Search for meals by name, ingredient, or first letter
- Request a random meal as a demo or exploration tool
- Integration-ready API output for downstream nodes

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
  - id: mealdb_node
    build: pip install -e mealdb_node_connector
    path: mealdb_node_connector
    inputs:
      parameters: input/parameters
    outputs:
      - mealdb_result
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
  # Your parameter input node (e.g., generates 'action' and 'value')
  - id: parameters
    build: pip install your-parameter-source
    path: your-parameter-source
    outputs:
      - parameters

  # MealDB node configuration
  - id: mealdb_node
    build: pip install -e mealdb_node_connector
    path: mealdb_node_connector
    inputs:
      parameters: parameters/parameters
    outputs:
      - mealdb_result
```

Your point source must output:

* Topic: `parameters`
* Data: Dict with keys `action` (str) and `value` (str or empty)
* Metadata:

  ```json
  {
    "action": "random_meal|search_by_name|list_by_first_letter|filter_by_ingredient",
    "value": "string (depends on action)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                                                  |
| ---------- | ------- | ------------------------------------------------------------ |
| parameters | object  | Dict with `action` and `value` keys                          |

### Output Topics

| Topic           | Type   | Description                                                |
| --------------- | ------ | --------------------------------------------------------- |
| mealdb_result   | object | The API result from TheMealDB or error object on failures |

## License

Released under the MIT License.
