# tarot_card_api

A Dora-rs node for retrieving tarot card information via the public tarotapi.dev API.

## Features
- Fetch all tarot card data, a random tarot card, or only court cards
- Simple integration with Dora via input parameters
- Robust API error handling and informative outputs

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
  - id: tarot_card_api
    build: pip install -e .
    path: tarot_card_api
    inputs:
      card_type: input/card_type
    outputs:
      - tarot_card_output
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
  - id: card_type_source
    build: pip install your-node
    path: your-card-type-source
    outputs:
      - card_type

  - id: tarot_card_api
    build: pip install -e .
    path: tarot_card_api
    inputs:
      card_type: card_type_source/card_type
    outputs:
      - tarot_card_output
```

Your point source must output:

* Topic: `card_type`
* Data: String value; One of `"all"`, `"random"`, or `"courts"`
* Metadata:

  ```json
  {
    "type": "string",
    "enum": ["all", "random", "courts"],
    "description": "Specifies which tarot cards to fetch."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                     |
| ------------|--------|------------------------------------------------|
| card_type    | string | Which tarot card(s) to fetch ('all', 'random', or 'courts') |

### Output Topics

| Topic             | Type   | Description                                             |
|-------------------|--------|--------------------------------------------------------|
| tarot_card_output | dict   | Tarot card(s) data or error message from tarotapi.dev   |

## License

Released under the MIT License.
