# pokemon_fact_node

A Dora-rs compatible node that provides random Pokémon facts via HTTP, retrieving them live from pokefacts.vercel.app and streaming the fact as output. 

## Features
- Fetches random Pokémon facts from an external web API
- Outputs facts as structured messages for use in Dora pipelines
- Robust error handling and web integration for seamless downstream use

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
  - id: pokemon_fact
    build: pip install -e .
    path: pokemon_fact_node
    inputs:
      user_input: input/user_input
    outputs:
      - pokemon_fact
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
  - id: user_input_node
    build: pip install your-user-input-node
    path: user_input_node
    outputs:
      - user_input
  - id: pokemon_fact
    build: pip install -e .
    path: pokemon_fact_node
    inputs:
      user_input: user_input_node/user_input
    outputs:
      - pokemon_fact
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable input (not processed in this node)
* Metadata:

  ```json
  {
    "description": "User input trigger, content ignored; present for compatibility"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                 |
| ------------| ------ | ------------------------------------------- |
| user_input  | any    | Used as a trigger to fetch a Pokémon fact   |

### Output Topics

| Topic         | Type   | Description                          |
| ------------- | ------ | ------------------------------------- |
| pokemon_fact  | str    | Retrieved Pokémon fact or error message |


## License

Released under the MIT License.
