# cat_fact_node

A simple Dora-rs node for fetching random cat facts from an online API, outputting the fact via the Dora dataflow messaging system.

## Features
- Fetches a random cat fact from an external API on demand
- Receives user input trigger for customizable workflows
- Emits the retrieved cat fact for downstream consumption

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
  - id: cat_fact_node
    build: pip install -e .
    path: cat_fact_node
    # Receives input from a previous node in the flow
    inputs:
      user_input: input/user_input
    outputs:
      - cat_fact
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
  - id: user_trigger
    build: pip install your-trigger-node
    path: your-trigger-node
    outputs:
      - user_input

  - id: cat_fact_node
    build: pip install -e .
    path: cat_fact_node
    inputs:
      user_input: user_trigger/user_input
    outputs:
      - cat_fact
```

Your point source must output:

* Topic: `user_input`
* Data: Any triggering data, e.g., a string or dict
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Arbitrary user input or workflow trigger."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                  |
| ----------- | ------- | ---------------------------- |
| user_input  | string  | Arbitrary input or workflow trigger |

### Output Topics

| Topic     | Type   | Description                          |
| --------- | ------ | ------------------------------------ |
| cat_fact  | string | Retrieved random cat fact (or error) |


## License

Released under the MIT License.
