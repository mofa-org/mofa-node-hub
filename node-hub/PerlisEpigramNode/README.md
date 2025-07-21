# perlis_epigram_node

Random Perlis Epigram Fetcher Node for Dora-rs

## Features
- Fetches a random Perlis Epigram from https://perl.is/random
- Outputs epigram text in a serializable dictionary
- Handles and reports network and API errors

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
  - id: perlis_epigram_node
    build: pip install -e .
    path: perlis_epigram_node
    inputs:
      user_input: input/user_input
    outputs:
      - epigram_output
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
  - id: input_source
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input

  - id: perlis_epigram_node
    build: pip install -e .
    path: perlis_epigram_node
    inputs:
      user_input: input_source/user_input
    outputs:
      - epigram_output
```

Your point source must output:

* Topic: `user_input`
* Data: string or object
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Plainstring user input, contents unused"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description               |
| ------------ | ------ | ------------------------- |
| user_input   | any    | User input trigger (unused) |

### Output Topics

| Topic           | Type         | Description                                   |
| --------------- | ------------ | --------------------------------------------- |
| epigram_output  | dict         | Dictionary with 'epigram' or 'error' field     |

## License

Released under the MIT License.
