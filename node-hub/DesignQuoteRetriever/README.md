# design_quote_fetcher

Quote API node for Dora-rs: Fetches a random design quote from the Quotes on Design API and outputs it as a structured message. Useful for demonstration, creative pipelines, or as a template for HTTP-based node integrations.

## Features
- Fetches a random quote from "Quotes on Design" API
- Extracts quote text and author from API responses
- Structured output with error handling

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
  - id: design_quote_fetcher
    build: pip install -e .
    path: design_quote_fetcher
    inputs:
      user_input: input/user_input
    outputs:
      - quote_output
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
    inputs: {}
    outputs:
      - user_input
  - id: design_quote_fetcher
    build: pip install -e .
    path: design_quote_fetcher
    inputs:
      user_input: your_node/user_input
    outputs:
      - quote_output
```

Your point source must output:

* Topic: `user_input`
* Data: Any valid string or object (not used in API call, facilitates node chaining)
* Metadata:

  ```json
  {
    "description": "Any data to trigger quote fetch. Not used in API call."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                      |
| ----------- | ------ | ------------------------------------------------ |
| user_input  | any    | Trigger argument (not used, enables node chaining) |

### Output Topics

| Topic         | Type           | Description                                  |
| ------------- | -------------- | --------------------------------------------- |
| quote_output  | dict / object  | Dictionary with 'quote' and 'author' fields, or error message |


## License

Released under the MIT License.
