# deck_of_cards_node

Interact with the public Deck of Cards API as a Dora node. This node allows you to shuffle, draw, and create new decks of playing cards on demand, controlled by configuration or upstream messaging.

## Features
- Shuffle an existing or new deck using the Deck of Cards REST API
- Draw a configurable number of cards from the deck
- Flexible configuration via YAML, environment variables, or dynamic messages

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
  - id: deck_node
    build: pip install -e deck_of_cards_node
    path: deck_of_cards_node
    inputs:
      user_input: input/user_input
    outputs:
      - deck_api_response
    env:
      deck_id: "1xou3n64udg9"
      deck_count: "1"
      draw_count: "2"
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
  - id: your_input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input
  - id: deck_node
    build: pip install -e deck_of_cards_node
    path: deck_of_cards_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - deck_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: String action keyword, e.g. "draw", "shuffle", or "new deck"
* Metadata:

  ```json
  {
    "type": "string",
    "description": "The requested action for the card deck node (draw, shuffle, new_deck)"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                 |
| ------------| -------|---------------------------------------------|
| user_input  | string | User command: "draw", "shuffle", "new deck" |

### Output Topics

| Topic             | Type    | Description                                         |
| -----------------|---------|-----------------------------------------------------|
| deck_api_response | object  | Response from Deck of Cards API (JSON as dictionary)|


## License

Released under the MIT License.
