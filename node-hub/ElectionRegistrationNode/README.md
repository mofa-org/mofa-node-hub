# election_registration_node

Facilitates API-based retrieval of U.S. voter registration state requirements, deadlines, and related information for use in Dora-rs pipelines.

## Features
- Query real-time state-by-state voter registration data
- Action-driven API: last-minute accepted, online not accepted, per-state info, and all states
- Graceful error handling with clear output topics

## Getting Started

### Installation
Install via pip:
```bash
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: election_registration_node
    build: pip install -e .
    path: election_registration_node
    inputs:
      action: input/action
      state_abbr: input/state_abbr
      user_input: input/user_input
    outputs:
      - api_result
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
  - id: input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - action
      - state_abbr
      - user_input

  - id: election_registration_node
    build: pip install -e .
    path: election_registration_node
    inputs:
      action: input_node/action
      state_abbr: input_node/state_abbr
      user_input: input_node/user_input
    outputs:
      - api_result
      - error

  - id: downstream_node
    build: pip install your-downstream-node
    path: your-downstream-node
    inputs:
      api_result: election_registration_node/api_result
      error: election_registration_node/error
```

Your point source must output:

* Topic: `action` (API target action)
* Topic: `state_abbr` (US state abbreviation, required if action is `state_info`)
* Topic: `user_input` (arbitrary string, optional, for compatibility)
* Data: Strings (e.g., `"last_minute_accepted"`, `"CA"`)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Election API action type or state abbreviation; see input documentation."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                                          |
| ------------| ------ | ------------------------------------------------------------------------------------ |
| action      | str    | The API action to perform. [last_minute_accepted, all_states, online_not_accepted, state_info] |
| state_abbr  | str    | US state abbreviation (e.g., CA, NY). Required for `state_info` action.                |
| user_input  | str    | Optional user request context.                                                         |

### Output Topics

| Topic      | Type         | Description                                             |
| ----------| ------------ | ------------------------------------------------------- |
| api_result| dict / str   | API response data according to requested action         |
| error     | dict         | Error info { error: <description>, status_code?: int }  |


## License

Released under the MIT License.
