# numbers_facts_node

Fetch random interesting math facts as a Dora node! This node enables your pipeline to retrieve live mathematical trivia using Numbers API and outputs them in a structured format.

## Features
- Fetches random math facts from the Numbers API
- Robust error handling with structured error reporting
- Integrates easily with other Dora/Mofa nodes

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
  - id: numbers_facts
    build: pip install -e numbers_facts_node
    path: numbers_facts_node
    inputs:
      user_input: input/user_input  # required to trigger fact fetch
    outputs:
      - fact
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
  - id: user_input
    build: pip install your-own-input-node
    path: your_input_node
    outputs:
      - user_input
  - id: numbers_facts
    build: pip install -e numbers_facts_node
    path: numbers_facts_node
    inputs:
      user_input: user_input/user_input
    outputs:
      - fact
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value to trigger fetch
* Metadata:

  ```json
  {
    "description": "Any value to signal fact fetching. Actual value ignored; just triggers fetch."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                 |
| ----------- | ------ | ------------------------------------------- |
| user_input  | Any    | Triggers fetching a random math fact        |

### Output Topics

| Topic | Type   | Description                                              |
|-------|--------|----------------------------------------------------------|
| fact  | dict   | Contains the numbers fact (JSON) or error message        |

## License

Released under the MIT License.
