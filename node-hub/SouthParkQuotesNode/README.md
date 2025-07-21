# SouthParkQuotesNode

SouthParkQuotesNode: Fetches random and Kenny-specific quotes from the South Park Quotes API using Dora/Mofa agent architecture.

## Features
- Fetches three random South Park quotes
- Fetches Kenny-specific South Park quotes
- Simple REST API integration with Dora/Mofa agent support

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
  - id: southpark
    build: pip install -e southpark_quotes_node
    path: southpark_quotes_node
    inputs:
      user_input: input/user_input
    outputs:
      - southpark_quotes_api_results
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
    build: pip install -e your_input_node
    path: your_input_node
    outputs:
      - user_input

  - id: southpark
    build: pip install -e southpark_quotes_node
    path: southpark_quotes_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - southpark_quotes_api_results
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy to trigger the node)
* Metadata:

  ```json
  {"description": "Dummy input to orchestrate node run; any value accepted."}
  ```

## API Reference

### Input Topics

| Topic      | Type       | Description                               |
| ---------- | ---------- | ----------------------------------------- |
| user_input | any/dummy  | Triggers dataflow; no required structure. |

### Output Topics

| Topic                        | Type   | Description                                            |
| ---------------------------- | ------ | ------------------------------------------------------ |
| southpark_quotes_api_results | object | Results from South Park Quotes API (random + Kenny).   |


## License

Released under the MIT License.
