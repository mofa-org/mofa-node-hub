# profanity_filter_node

A Dora node that filters profanity from input text using the Purgomalum API. The node takes a string and outputs the censored result (or an error structure in case of problems), making it easy to add moderation steps to natural language flows in a Dora pipeline.

## Features
- Filters profanity from input text in real time
- Uses the Purgomalum public API for robust filtering
- Gracefully handles API and input errors with clear outputs

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
  - id: profanity_filter
    build: pip install -e .
    path: profanity_filter_node
    inputs:
      input_text: input/input_text
    outputs:
      - filtered_text
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
  - id: my_source
    build: pip install my-node
    path: my-node
    outputs:
      - input_text
  - id: profanity_filter
    build: pip install -e .
    path: profanity_filter_node
    inputs:
      input_text: my_source/input_text
    outputs:
      - filtered_text
```

Your point source must output:

* Topic: `input_text`
* Data: The text string to be checked for profanity
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Input text to be filtered for profanity"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                 |
| ----------- | ------ | -------------------------- |
| input_text  | string | Text to be filtered        |

### Output Topics

| Topic         | Type   | Description                                  |
| ------------- | ------ | -------------------------------------------- |
| filtered_text | string | Censored result or error JSON structure      |

## License

Released under the MIT License.
