# stadt_land_fluss_node

A Dora-rs node that fetches the official “Stadt, Land, Fluss” public dataset over HTTP and exposes it as an output topic. Intended for use as a data source for games, quizzes, or downstream task pipelines.

## Features
- Fetches up-to-date "Stadt, Land, Fluss" dataset from a remote JSON endpoint
- Resilient error handling: errors are reported as structured output
- Integration-ready: exposes HTTP dataset fetch via Dora node messaging

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
  - id: stadtlandfluss
    build: pip install -e .
    path: stadt_land_fluss_node
    inputs:
      user_input: input/user_input
    outputs:
      - stadt_land_fluss_data
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
  - id: stadtlandfluss
    build: pip install -e .
    path: stadt_land_fluss_node
    inputs:
      user_input: input/user_input
    outputs:
      - stadt_land_fluss_data
  - id: your_downstream_node
    build: pip install -e yournode
    path: yournode
    inputs:
      stadt_land_fluss_data: stadtlandfluss/stadt_land_fluss_data
    outputs:
      - some_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or relevant trigger
* Metadata:

  ```json
  {
    "description": "Dummy trigger for data refresh."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                         |
| ----------- | ------ | ----------------------------------- |
| user_input  | any    | Dummy trigger, required by agent     |

### Output Topics

| Topic                  | Type    | Description                                                           |
| ---------------------- | ------- | --------------------------------------------------------------------- |
| stadt_land_fluss_data  | dict    | "Stadt, Land, Fluss" data or error result from the remote HTTP fetch  |


## License

Released under the MIT License.
