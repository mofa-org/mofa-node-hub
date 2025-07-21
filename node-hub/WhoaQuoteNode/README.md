# whoa_quote_node

Random 'Woah' Quotes Fetcher Node for Dora-rs/MOFA

## Features
- Fetches 5 random 'woah' quotes from a public API
- Simple integration with other nodes via standard input/output topics
- Handles errors gracefully and returns diagnostic information

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: whoa_quote_node
    build: pip install -e .
    path: whoa_quote_node
    inputs:
      user_input: input/user_input
    outputs:
      - woah_quotes
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
  - id: your_node
    build: pip install your-node
    path: your-node
    outputs:
      - user_input
  - id: whoa_quote_node
    build: pip install -e .
    path: whoa_quote_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - woah_quotes
```

Your point source must output:

* Topic: `user_input`
* Data: String or structured user input (if applicable)
* Metadata:

  ```json
  {
    "type": "string"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ----------| ------ | ----------------------------------------- |
| user_input | string | Input parameter for the quote fetch agent |

### Output Topics

| Topic        | Type     | Description                         |
| ------------| -------- | ----------------------------------- |
| woah_quotes | object   | JSON list of random woah quotes or error message |


## License

Released under the MIT License.
