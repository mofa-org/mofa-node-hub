# oldest_person_node

Dora node for retrieving world record oldest living and ever-recorded persons using real-time data from whoistheoldest.com.

## Features
- Fetches oldest living and oldest ever person records from public API
- Works in both restricted and unrestricted Python environments (requests fallback)
- Returns API data as structured outputs consumable by other Dora nodes

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
  - id: oldest_person
    build: pip install -e .
    path: oldest_person_node
    inputs:
      user_input: input/user_input   # Optional (simply triggers fetch)
    outputs:
      - oldest_person_data
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
  # Your input/trigger node
  - id: user_input_node
    build: pip install your-trigger-node
    path: your-trigger-node
    outputs:
      - user_input

  # Oldest person record fetcher
  - id: oldest_person
    build: pip install -e .
    path: oldest_person_node
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - oldest_person_data

  # Example display/consumer node
  - id: display
    build: pip install your-display-node
    path: your-display-node
    inputs:
      oldest_person_data: oldest_person/oldest_person_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any (unused in this node)
* Metadata:

  ```json
  {
    "description": "Any payload, triggers oldest-person data retrieval"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                          |
| ----------- | ------ | ------------------------------------ |
| user_input  | Any    | Input (triggers fetch; unused value) |

### Output Topics

| Topic               | Type   | Description                                               |
| ------------------- | ------ | --------------------------------------------------------- |
| oldest_person_data  | JSON   | Contains keys `oldest_living` and `oldest_ever` with API data |

## License

Released under the MIT License.
