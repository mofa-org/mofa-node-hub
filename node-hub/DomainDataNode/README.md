# domain_data_node

Query domain intelligence and bulk data from FishFish API, with Dora-compatible input/output ports for simple integration.

## Features
- Fetch details for specific domains (e.g., discordpartner.com) from FishFish API
- Bulk list available domains with minimal configuration
- Dora/Mofa agent compatible input/output for easy orchestration

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
  - id: domain_data_node
    build: pip install -e .
    path: domain_data_node
    inputs:
      user_input: orchestrator/user_input
    outputs:
      - single_domain_details
      - domains_list
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
    build: pip install -e my-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: domain_data_node
    build: pip install -e .
    path: domain_data_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - single_domain_details
      - domains_list
```

Your point source must output:

* Topic: `user_input`
* Data: Any (can be empty/null, used to trigger fetching)
* Metadata:

  ```json
  {
    "type": "trigger",
    "description": "Used to trigger the domain fetch process."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                  |
| ------------| -------| ---------------------------- |
| user_input  | Any    | Triggers domain data fetch   |

### Output Topics

| Topic                 | Type   | Description                      |
| --------------------- | ------ | -------------------------------- |
| single_domain_details | dict   | Details for discordpartner.com   |
| domains_list          | dict   | Bulk list of available domains   |


## License

Released under the MIT License.
