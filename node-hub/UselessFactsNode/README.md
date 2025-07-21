# useless_facts_node

A Dora-rs node that fetches a random or daily useless fact from https://uselessfacts.jsph.pl/. Facts can be retrieved in English or German, with configurable selection via input port.

## Features
- Fetch random useless facts in English
- Fetch today's fact in English
- Fetch random useless facts in German via configuration

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
  - id: facts
    path: useless_facts_node
    python: 3.10
    build: pip install requests mofa-agent-build
    inputs:
      fact_type: input/fact_type
    outputs:
      - useless_fact
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
  - id: fact-type-source
    path: my_custom_input_node
    outputs:
      - fact_type

  - id: facts
    path: useless_facts_node
    build: pip install requests mofa-agent-build
    inputs:
      fact_type: fact-type-source/fact_type
    outputs:
      - useless_fact
```

Your point source must output:

* Topic: `fact_type`
* Data: string value (`random`, `today`, or `random_de`)
* Metadata:

  ```json
  {
    "type": "string",
    "allowed_values": ["random", "today", "random_de"],
    "description": "Selects which fact to fetch."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                     |
| ----------- | ------ | ------------------------------- |
| fact_type   | string | Fact selection: 'random', 'today', or 'random_de' |

### Output Topics

| Topic         | Type      | Description                                           |
| ------------- | --------- | ----------------------------------------------------- |
| useless_fact  | dict      | Contains keys: text, source, language; or error info. |


## License

Released under the MIT License.
