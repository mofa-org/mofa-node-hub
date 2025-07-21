# corporate_buzzphrase_node

A Dora-rs compatible node that generates random corporate buzzphrases using the public [corporatebs-generator](https://corporatebs-generator.sameerkumar.website/) API. Suitable for demo pipelines, fun data generation, or mocking NLP outputs.

## Features
- Generates a random corporate buzzphrase on demand
- Fully stateless, responds to every call
- Simple integration with other nodes via standard Dora/Mofa interfaces

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
  - id: buzz_gen
    build: pip install -e corporate_buzzphrase_node
    path: corporate_buzzphrase_node
    inputs:
      user_input: input/user_input  # Placeholder, ignored by node
    outputs:
      - buzzphrase
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
  - id: your_source
    build: pip install your-fancy-node
    path: your-fancy-node
    outputs:
      - user_input

  - id: buzz_gen
    build: pip install -e corporate_buzzphrase_node
    path: corporate_buzzphrase_node
    inputs:
      user_input: your_source/user_input
    outputs:
      - buzzphrase
```

Your point source must output:

* Topic: `user_input`
* Data: Any value; the input is ignored (kept for compatibility)
* Metadata:

  ```json
  {
    "description": "Ignored; present for dataflow compatibility"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                     |
|-------------|--------|---------------------------------|
| user_input  | any    | Placeholder trigger for output; ignored |

### Output Topics

| Topic      | Type   | Description                                     |
|------------|--------|-------------------------------------------------|
| buzzphrase | str    | The generated corporate BS phrase, or error text |

## License

Released under the MIT License.
