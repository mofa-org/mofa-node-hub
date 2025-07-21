# star_wars_character

Fetch Star Wars Character Info from SWAPI in Dora pipelines

## Features
- Fetches information on Star Wars characters using the SWAPI (Star Wars API)
- Outputs result in JSON format compatible with Dora message passing
- Handles and reports network or parsing errors gracefully

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
  - id: star_wars_character
    build: pip install -e .
    path: star_wars_character
    inputs:
      user_input: input/user_input
    outputs:
      - character_info
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
  - id: my_input_node
    build: pip install -e my_input_node
    path: my_input_node
    outputs:
      - user_input
  - id: star_wars_character
    build: pip install -e .
    path: star_wars_character
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - character_info
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary string or trigger used for dataflow (e.g., pass-through for chaining)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Arbitrary user input or trigger to initiate SWAPI call. Not actively used."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                  |
| ------------| ------ | ---------------------------------------------|
| user_input  | string | Arbitrary user input or trigger (not used)    |

### Output Topics

| Topic           | Type  | Description                            |
| --------------- | ----- | -------------------------------------- |
| character_info  | JSON  | Star Wars character info from SWAPI, or error details |


## License

Released under the MIT License.
