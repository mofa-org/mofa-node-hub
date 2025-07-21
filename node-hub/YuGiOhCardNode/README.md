# yugioh_card_node

A Dora-rs node that fetches full card databases from Yu-Gi-Oh! public JSON APIs, covering Speed Duel Skill Cards and Rush Duel cards. Compatible with MOFA agent system and designed for integration in multi-node Dora pipelines.

## Features
- Fetches full Yu-Gi-Oh! TCG Speed Duel Skill Card datasets automatically
- Fetches all Yu-Gi-Oh! Rush Duel cards in bulk (json)
- Robust error handling—reports API and network failures via outputs

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
  - id: yugioh_card_node
    build: pip install -e .
    path: yugioh_card_node
    inputs:
      user_input: input/user_input
    outputs:
      - yugioh_data
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
    build: pip install your-node
    path: your_node
    outputs:
      - user_input
  - id: yugioh_card_node
    build: pip install -e yugioh_card_node
    path: yugioh_card_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - yugioh_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any user-defined input for trigger or filtration
* Metadata:

  ```json
  {
    "description": "User input for querying or triggering the YuGiOhCardNode fetch operation (can be null or arbitrary string)"
  }
  ```

## API Reference

### Input Topics

| Topic              | Type              | Description                             |
| ------------------ | ---------------- | --------------------------------------- |
| user_input         | Any (string/obj) | User input to trigger or filter request |

### Output Topics

| Topic           | Type        | Description                                                                 |
| --------------  | ----------- | --------------------------------------------------------------------------- |
| yugioh_data     | JSON object | Fetched data from endpoints and error dict: `{ "results": ..., "errors": ... }` |


## License

Released under the MIT License.
