# MathFunctionResolverNode

Agent for evaluating math expressions with variables using the oglimmer public math API via HTTP. Allows runtime parameterization of both the expression and variable (e.g., x) and returns a computation result or error.

## Features
- Resolve arbitrary math expressions with a variable (e.g., `3+4*x`)
- HTTP-based integration with the oglimmer math API
- Robust error handling and validation of numeric inputs

## Getting Started

### Installation
Install via pip:
```bash
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
agents:
  - id: math_function_node
    module: math_function_node
    class: MathFunctionResolverNode
    inputs:
      - expression
      - x
    outputs:
      - calculation_result
    env:
      ENDPOINT: "https://math.oglimmer.de/v1/calc"  # optional, default used if not set
```

Run the demo:

```bash
dora build demo.yml
dora start demo.yml
```

## Integration with Other Nodes

To connect with your existing node:

```yaml
agents:
  - id: upstream_node
    module: upstream_source
    outputs:
      - expression
      - x
  - id: math_function_node
    module: math_function_node
    inputs:
      - expression: upstream_node/expression
      - x: upstream_node/x
    outputs:
      - calculation_result
```

Your point source must output:

* Topic: `expression`
* Data: Expression string, e.g. `3+4*x`
* Topic: `x`
* Data: String or numeric value for `x`
* Metadata:

  ```json
  {
    "dtype": "str or float",
    "required": true
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                   |
| ----------- | ------ | ----------------------------- |
| expression  | str    | Math expression to evaluate   |
| x           | str/float | Value for variable x         |

### Output Topics

| Topic               | Type    | Description                                |
| ------------------- | ------- | ------------------------------------------ |
| calculation_result  | dict    | Result from oglimmer API or error info     |

## License

Released under the MIT License.
