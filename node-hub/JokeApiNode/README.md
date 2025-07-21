# joke_api_node

A Dora-rs node that fetches jokes from the JokeAPI service, supporting optional blacklist filtering and German language output. The node allows dynamic joke type selection via configuration or runtime parameters.

## Features
- Fetch jokes from https://v2.jokeapi.dev/.
- Supports blacklist filtering to exclude racist jokes.
- Fetches jokes in German language.

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
  - id: joke_api_node
    build: pip install -e .
    path: joke_api_node
    inputs:
      joke_type: input/joke_type
    outputs:
      - joke_response
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
  - id: my_param_source
    build: pip install my-param-source
    path: my_param_source
    outputs:
      - joke_type
  - id: joke_api_node
    build: pip install -e .
    path: joke_api_node
    inputs:
      joke_type: my_param_source/joke_type
    outputs:
      - joke_response
```

Your point source must output:

* Topic: `joke_type`
* Data: String value (e.g. 'blacklist' or 'german')
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Joke type. Must be one of 'blacklist' or 'german'"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                      |
| ----------- | ------ | -------------------------------- |
| joke_type   | string | Joke selection: 'blacklist' or 'german' |

### Output Topics

| Topic         | Type      | Description                            |
| ------------- | --------- | -------------------------------------- |
| joke_response | dict      | JokeAPI response or error information. |


## License

Released under the MIT License.
