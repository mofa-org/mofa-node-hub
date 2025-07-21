# job_board_node

Fetch sponsored job board postings from Arbeitnow API via Dora-rs node interface.

## Features
- Fetch up-to-date job postings from the Arbeitnow public API
- Dora-rs node interface with parameter and output compatibility
- Robust error handling and output serialization

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
  - id: job_board_node
    build: pip install -e .
    path: job_board_node
    inputs:
      user_input: input/user_input  # Required for interface compatibility (can be dummy)
    outputs:
      - job_board_data
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
  - id: my_input_node
    build: pip install -e my_input_node
    path: my_input_node
    outputs:
      - user_input

  - id: job_board_node
    build: pip install -e job_board_node
    path: job_board_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - job_board_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (optional, as it's not used but must exist for compatibility)
* Metadata:

  ```json
  {"dtype": "str", "description": "Any user input string (ignored)."}
  ```

## API Reference

### Input Topics

| Topic                | Type  | Description                               |
| -------------------- | ----- | ----------------------------------------- |
| user_input           | str   | User input parameter (for compatibility). |

### Output Topics

| Topic           | Type            | Description                                         |
| --------------- | --------------- | --------------------------------------------------- |
| job_board_data  | dict/list/str   | Job board data fetched from Arbeitnow API or errors |


## License

Released under the MIT License.
