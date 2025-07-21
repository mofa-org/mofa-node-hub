# crossref_metadata_node

A Dora-rs node for connecting to the Crossref API and reporting its heartbeat status. This node can be used as a health-check for the Crossref metadata service within dataflow pipelines.

## Features
- Queries the Crossref API heartbeat endpoint
- Returns JSON heartbeat response or error
- Integrates easily with Dora-based dataflow pipelines

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
  - id: crossref_heartbeat_node
    build: pip install -e crossref_metadata_node
    path: crossref_metadata_node
    inputs:
      user_input: input/user_input
    outputs:
      - crossref_heartbeat
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
  - id: my_trigger_node
    build: pip install my-trigger-node
    path: my_trigger_node
    outputs:
      - user_input    # Output trigger

  - id: crossref_heartbeat_node
    build: pip install -e crossref_metadata_node
    path: crossref_metadata_node
    inputs:
      user_input: my_trigger_node/user_input
    outputs:
      - crossref_heartbeat

  # Downstream consumer node
  - id: downstream_consumer
    build: pip install my-consumer-node
    path: my_consumer_node
    inputs:
      crossref_heartbeat: crossref_heartbeat_node/crossref_heartbeat
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (serves as a trigger)
* Metadata:

  ```json
  {
    "description": "Any value used to trigger the Crossref heartbeat check"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                      |
| ---------- | ------ | -------------------------------- |
| user_input | Any    | Trigger for heartbeat invocation  |

### Output Topics

| Topic              | Type   | Description                                                      |
| ------------------ | ------ | ---------------------------------------------------------------- |
| crossref_heartbeat | dict or str | Crossref heartbeat JSON response or error message |


## License

Released under the MIT License.
