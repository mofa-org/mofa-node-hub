# german_election_node

Query up-to-date German election survey polls and main page with a Dora-compatible MofaAgent node.

## Features
- Fetches the latest German election surveys from dawum.de
- Retrieves both survey JSON and the main page HTML
- Dora-rs compatible node structure for fast integration

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
  - id: german_election_node
    build: pip install -e .
    path: german_election_node
    inputs:
      user_input: input/user_input
    outputs:
      - german_election_api_results
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
  - id: my_input_source
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input
  - id: german_election_node
    build: pip install -e .
    path: german_election_node
    inputs:
      user_input: my_input_source/user_input
    outputs:
      - german_election_api_results
```

Your point source must output:

* Topic: `user_input`
* Data: Any input (string or object) to trigger the query (can be empty string or None for this API, as the actual input isn't used)
* Metadata:

  ```json
  {
    "description": "Placeholder for API query trigger (not actually used in API call)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                     |
| ----------| ------ | ----------------------------------------------- |
| user_input | any    | Placeholder input; triggers poll query          |

### Output Topics

| Topic                       | Type   | Description                                                                           |
| --------------------------- | ------ | ------------------------------------------------------------------------------------- |
| german_election_api_results | object | Dictionary containing newest_surveys (JSON from dawum), main_page (HTML or error)      |

## License

Released under the MIT License.
