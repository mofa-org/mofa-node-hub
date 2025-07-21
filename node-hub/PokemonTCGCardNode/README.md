# pokemon_tcg_node

A Dora-rs node for retrieving and previewing Pokémon Trading Card Game (TCG) cards via the Pokémon TCG public API.

## Features
- Fetches latest Pokémon TCG card data from the official API
- Returns a preview list of cards for safe handling in your Dora pipeline
- Integrates with external nodes via parameterized input/output topics

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
  - id: pokemon_tcg_node
    build: pip install -e .
    path: pokemon_tcg_node
    inputs:
      user_input: input/user_input
    outputs:
      - pokemon_tcg_cards
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
  - id: point_source
    build: pip install your-node
    path: your-node
    outputs:
      - user_input
  - id: pokemon_tcg_node
    build: pip install -e .
    path: pokemon_tcg_node
    inputs:
      user_input: point_source/user_input
    outputs:
      - pokemon_tcg_cards
```

Your point source must output:

* Topic: `user_input`
* Data: String or dictionary for parameter passing
* Metadata:

  ```json
  {
    "description": "Parameter input for the Pokémon TCG card node; should specify user-trigger or query context as needed."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type        | Description                    |
| ----------- | ----------- | ------------------------------ |
| user_input  | Any (dict or string) | Input parameter to trigger card lookup |

### Output Topics

| Topic              | Type   | Description                              |
| ------------------ | ------ | ---------------------------------------- |
| pokemon_tcg_cards  | dict   | Preview list of Pokémon TCG cards or error info |

## License

Released under the MIT License.
