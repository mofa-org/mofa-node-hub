# cocktail_lookup_node

Cocktail DB Query Node for Dora-rs (CocktailLookupNode)

## Features
- Supports three search actions: random cocktail, ingredient lookup, and drink name search
- Easily composable with other nodes by parameterized commands
- Simple JSON output compatible with downstream processing

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
  - id: cocktail_lookup
    build: pip install -e .
    path: cocktail_lookup_node
    inputs:
      action: input/action   # Source node provides 'action' command (e.g., random_cocktail)
      param: input/param     # Optional param (e.g., 'vodka')
    outputs:
      - lookup_result
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
  - id: command_source
    build: pip install -e your_command_source
    path: your_command_source
    outputs:
      - action
      - param

  - id: cocktail_lookup
    build: pip install -e .
    path: cocktail_lookup_node
    inputs:
      action: command_source/action
      param: command_source/param
    outputs:
      - lookup_result
```

Your point source must output:

* Topic: `action` (string)
* Topic: `param` (string, can be empty)
* Data: Send plain strings for each topic.
* Metadata:

  ```json
  {
    "dtype": "str",
    "shape": "()"
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                              |
| ------- | ------ | ---------------------------------------- |
| action  | str    | Command action: random_cocktail, ingredient_search, or drink_search |
| param   | str    | Parameter for search (e.g., ingredient or drink name); can be empty for random |

### Output Topics

| Topic         | Type   | Description                       |
| ------------- | ------ | --------------------------------- |
| lookup_result | JSON   | Result of the CocktailDB query (parsed JSON or error info) |

## License

Released under the MIT License.
