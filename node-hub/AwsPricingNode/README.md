# aws_pricing_node

Fetch AWS EC2 & RDS Pricing for Dora-rs Pipelines

## Features
- Fetches up-to-date AWS EC2 prices and hardware specifications
- Fetches AWS RDS (Relational Database Service) prices
- Outputs both EC2 and RDS data in a serialized format for downstream Dora nodes

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
  - id: aws_pricing
    build: pip install -e aws_pricing_node
    path: aws_pricing_node
    inputs:
      user_input: input/user_input
    outputs:
      - aws_pricing_output
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
  - id: my_point_source
    build: pip install -e my_point_source
    path: my_point_source
    outputs:
      - user_input

  - id: aws_pricing
    build: pip install -e aws_pricing_node
    path: aws_pricing_node
    inputs:
      user_input: my_point_source/user_input
    outputs:
      - aws_pricing_output
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary string or dict (any user input, optional)
* Metadata:

  ```json
  {
    "description": "User input payload from upstream node, can be empty or used for custom triggers."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                       |
| ---------- | ------ | --------------------------------- |
| user_input | Any    | Arbitrary input to trigger query   |

### Output Topics

| Topic              | Type      | Description                                      |
| ------------------ | --------- | ------------------------------------------------ |
| aws_pricing_output | dict/json | JSON result with keys 'ec2' and 'rds'            |


## License

Released under the MIT License.
