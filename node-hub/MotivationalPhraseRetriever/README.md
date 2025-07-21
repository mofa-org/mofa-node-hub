# motivational_phrase_node

A Dora node that retrieves up-to-date motivational phrases from an online JSON API and outputs them in a machine-readable format for downstream workflow steps.

## Features
- Fetches the latest motivational/inspirational phrases from a public API
- Error-handled, robust HTTP/JSON serialization for resilient pipelines
- Designed for plug-and-play use in dora-rs or mofa agent pipelines

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
  - id: motivator
    build: pip install -e motivational_phrase_node
    path: motivational_phrase_node
    inputs:
      user_input: input/user_input  # Optional; placeholder for expansion
    outputs:
      - motivational_phrases
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
  - id: motivator
    build: pip install -e motivational_phrase_node
    path: motivational_phrase_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - motivational_phrases
  - id: downstream
    build: pip install your-downstream-node
    path: your-downstream-node
    inputs:
      motivational_phrases: motivator/motivational_phrases
```

Your point source must output:

* Topic: `user_input`
* Data: Any data/placeholder (currently not processed)
* Metadata:

  ```json
  {
    "desc": "Placeholder string, number, or object to enable future dataflow extensibility."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                                                                                    |
| ---------- | ------- | ---------------------------------------------------------------------------------------------- |
| user_input | Any     | User-supplied or upstream value. Not consumed by the node but required for compliance/future expansion. |

### Output Topics

| Topic                 | Type           | Description                                        |
| --------------------- | -------------- | -------------------------------------------------- |
| motivational_phrases  | dict           | Dictionary of motivational phrases fetched from API, or error info on failure. |


## License

Released under the MIT License.
