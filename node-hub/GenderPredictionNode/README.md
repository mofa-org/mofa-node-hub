# gender_prediction_node

Predict gender from a name using the Genderize API.

## Features
- Predicts gender (male, female, unknown) for a given name
- Structured error handling for invalid input or API errors
- Exposes a simple Dora-compatible API for dataflow integration

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
  - id: gender_predictor
    build: pip install -e .
    path: gender_prediction_node
    inputs:
      name: input/name
    outputs:
      - gender_prediction
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
  - id: your_input_node
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - name

  - id: gender_predictor
    build: pip install -e .
    path: gender_prediction_node
    inputs:
      name: your_input_node/name
    outputs:
      - gender_prediction
```

Your point source must output:

* Topic: `name`
* Data: A string with the name to predict gender for
* Metadata:

  ```json
  {
    "datatype": "str",
    "description": "Person name for gender prediction"
  }
  ```

## API Reference

### Input Topics

| Topic | Type | Description |
|-------|------|-------------|
| name  | str  | Name to predict gender for |

### Output Topics

| Topic             | Type  | Description                           |
|-------------------|-------|---------------------------------------|
| gender_prediction | dict  | API result or error message (see below)|


## License

Released under the MIT License.
