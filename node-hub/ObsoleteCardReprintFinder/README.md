# obsolete_card_reprint

Agent for discovering obsolete Magic: The Gathering cards, superior/inferior versions, and listing functional reprints via the strictlybetter.eu API.

## Features
- List all obsolete cards and their functional reprints
- Look up superior/inferior (obsoleting) versions for a specific card
- Robust error handling and fully stateless agent interface

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
  - id: obsolete_card_reprint
    path: obsolete_card_reprint
    build: pip install -e .
    inputs:
      - user_input
      - card_name  # Optional: if you want to look up a specific card
    outputs:
      - reprints_result
      - obsoletes_result
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
  - id: my_custom_input
    path: my_custom_input_node
    build: pip install -e my_custom_input
    outputs:
      - user_input
      - card_name
  - id: obsolete_card_reprint
    path: obsolete_card_reprint
    build: pip install -e .
    inputs:
      user_input: my_custom_input/user_input
      card_name: my_custom_input/card_name
    outputs:
      - reprints_result
      - obsoletes_result
      - error
```

Your point source must output:

* Topic: `card_name`
* Data: The card name string
* Metadata:

  ```json
  {
    "dtype": "str",
    "desc": "Name of the card to look up for superior/inferior versions. If omitted, all functional reprints are listed."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                      |
| ------------| ------ | ------------------------------------------------ |
| user_input   | str    | Reserved for stateless chaining and future use   |
| card_name    | str    | Card to look up (optional, triggers obsoletes lookup) |

### Output Topics

| Topic              | Type   | Description                                        |
| ------------------ | ------ | -------------------------------------------------- |
| reprints_result    | dict   | All obsolete cards with their functional reprints   |
| obsoletes_result   | dict   | Obsoletes for a specific card (superior/inferior versions) |
| error              | dict   | Any error encountered; serialized as a dictionary   |

## License

Released under the MIT License.
