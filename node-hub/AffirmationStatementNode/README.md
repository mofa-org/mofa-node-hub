# affirmation_node

Fetches a random inspirational affirmation from the [affirmations.dev](https://www.affirmations.dev/) API and outputs it as a structured message via the specified Dora agent output port.

## Features
- Returns a positive affirmation string in each invocation
- Handles and reports API/network errors gracefully
- Compatible as a drop-in node in Dora-rs pipelines

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
  - id: affirmation_agent
    build: pip install -e affirmation_node
    path: affirmation_node
    inputs:
      user_input: input/user_input
    outputs:
      - affirmation
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
  - id: custom_input
    build: pip install -e your-input-node
    path: your_input_node
    outputs:
      - user_input

  - id: affirmation_agent
    build: pip install -e affirmation_node
    path: affirmation_node
    inputs:
      user_input: custom_input/user_input
    outputs:
      - affirmation
```

Your point source must output:

* Topic: `user_input`
* Data: Any (ignored by affirmation_node, but required for interface compliance)
* Metadata:

  ```json
  {
    "type": "any",
    "description": "Dummy parameter for agent interface compliance. Ignored by affirmation_node."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type | Description                                     |
|-------------|------|-------------------------------------------------|
| user_input  | any  | Dummy parameter required for interface compliance. Value is ignored. |

### Output Topics

| Topic        | Type     | Description                                                           |
|--------------|----------|-----------------------------------------------------------------------|
| affirmation  | dict     | {"affirmation": string} on success, {"error": string} on error.     |


## License

Released under the MIT License.
