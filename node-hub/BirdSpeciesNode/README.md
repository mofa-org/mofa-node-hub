# bird_species_node

Query Swiss Ornithological Institute's public bird species JSON API from Dora-rs nodes.

## Features
- Fetch metadata/details for a specific bird using its ID
- List all supported bird species from the Swiss Ornithological Institute
- Retrieve the "Bird of the Day" feature

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
  - id: birds
    build: pip install -e bird_species_node
    path: bird_species_node
    inputs:
      user_input: input/user_input
      action: input/action
      param: input/param
    outputs:
      - bird_data
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
  - id: bird_input
    build: pip install -e your-input-node
    path: your_input_node
    outputs:
      - action
      - param
  - id: birds
    build: pip install -e bird_species_node
    path: bird_species_node
    inputs:
      action: bird_input/action
      param: bird_input/param
    outputs:
      - bird_data
```

Your point source must output:

* Topic: `action` and `param`
* Data: string (for both)
* Metadata:

  ```json
  {
    "action": "by_id",     // or "list" or "daily"
    "param": "700_de"      // required for 'by_id', ignored for others
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                                  |
| ----------- | ------ | ----------------------------------------------------------- |
| user_input  | Any    | (Optional) Auxiliary input for future extensibility         |
| action      | str    | One of: 'by_id', 'list', or 'daily'                         |
| param       | str    | For 'by_id', provides the species code (e.g., '700_de'); ignored otherwise |

### Output Topics

| Topic      | Type         | Description                                |
| ---------- | ------------ | ------------------------------------------ |
| bird_data  | dict (JSON)  | Response from Swiss bird API or error info |


## License

Released under the MIT License.
