# covid_trends_node

Get worldwide COVID-19 trends (cases, deaths, recoveries) using the open disease.sh API. Designed as a Dora-rs node for easy pipeline integration via MofaAgent.

## Features
- Fetches global COVID-19 case, death, and recovery history
- Gracefully handles API and JSON errors
- Integrates easily into Dora/MofaAgent pipelines

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
  - id: covid_trends_node
    build: pip install -e .
    path: covid_trends_node
    inputs:
      user_input: input/user_input
    outputs:
      - covid_trends
      - covid_trends_error
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
    build: pip install my-input-node
    path: my_input_node
    outputs:
      - user_input

  - id: covid_trends_node
    build: pip install -e .
    path: covid_trends_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - covid_trends
      - covid_trends_error
```

Your point source must output:

* Topic: `user_input`
* Data: Any dummy string (not used by the node, just triggers execution)
* Metadata:

  ```json
  {
    "description": "Dummy input to trigger Covid19TrendsNode execution.",
    "data_type": "string"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                   |
| ------------|--------|-----------------------------------------------|
| user_input   | string | Dummy parameter to trigger node execution     |

### Output Topics

| Topic                | Type       | Description                          |
|----------------------|------------|--------------------------------------|
| covid_trends         | dict/list  | Full COVID-19 trend data as JSON     |
| covid_trends_error   | string     | Error message, if any failure occurs |


## License

Released under the MIT License.
