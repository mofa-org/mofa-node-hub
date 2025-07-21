# public_ip_node

Get Your Public IP Easily with Dora!

## Features
- Fetches your current public IP address from multiple sources
- Robust error handling and service fallback
- Easily integrates into Dora node pipelines

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
  - id: public_ip_node
    build: pip install -e .
    path: public_ip_node
    inputs:
      user_input: input/user_input
    outputs:
      - public_ip
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
    build: pip install -e your_input_node
    path: your_input_node
    outputs:
      - user_input

  - id: public_ip_node
    build: pip install -e .
    path: public_ip_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - public_ip
```

Your point source must output:

* Topic: `user_input`
* Data: User-defined trigger or message
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Any string to trigger the public IP fetch."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
| ----------| ------ | ---------------------------------- |
| user_input | str    | User input or trigger to initiate IP fetch |

### Output Topics

| Topic      | Type   | Description                                             |
| ----------| ------ | ------------------------------------------------------- |
| public_ip  | dict   | Public IP result as {"ip": str, "source": str}, or error details |

## License

Released under the MIT License.
