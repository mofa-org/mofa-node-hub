# name_age_estimator

Estimate Age by Name with Agify.io

## Features
- Estimates age based on a given first name using Agify.io API
- Accepts parameter input via node messaging system
- Returns structured JSON output with name, estimated age, and count (sample size)

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
  - id: name_age_estimator
    build: pip install -e .
    path: name_age_estimator
    inputs:
      name: input/name
    outputs:
      - estimated_age
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
      - name
  - id: name_age_estimator
    build: pip install -e .
    path: name_age_estimator
    inputs:
      name: my_input_node/name
    outputs:
      - estimated_age
```

Your point source must output:

* Topic: `name`
* Data: String (first name to estimate age for)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "First name to estimate age"
  }
  ```

## API Reference

### Input Topics

| Topic | Type  | Description                    |
|-------|-------|--------------------------------|
| name  | str   | First name to estimate age for |

### Output Topics

| Topic         | Type    | Description                                             |
|-------------- |---------|--------------------------------------------------------|
| estimated_age | object  | JSON object with fields: name, age, count. Or error.   |


## License

Released under the MIT License.
