# film_data_node

Dora node to retrieve film camera data from the public FilmAPI (https://filmapi.vercel.app/api/films).

## Features
- Fetches up-to-date film camera data from a public API
- Standard Dora-rs input/output integration for graph compatibility
- Graceful error handling with structured error outputs

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
  - id: film_data_node
    build: pip install -e .
    path: film_data_node
    inputs:
      user_input: upstream/user_input  # Optional dummy for pipeline compatibility
    outputs:
      - film_api_output
      - film_api_error
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
  - id: external_source
    build: pip install my-upstream-node
    path: my-upstream-node
    outputs:
      - user_input
  - id: film_data_node
    build: pip install -e .
    path: film_data_node
    inputs:
      user_input: external_source/user_input
    outputs:
      - film_api_output
      - film_api_error
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy input; can be an int, string, etc.)
* Metadata:

  ```json
  {
    "description": "Dummy input for pipeline consistency",
    "type": "string or any JSON-serializable object"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| user_input | any    | Dummy parameter to satisfy graph integration |

### Output Topics

| Topic            | Type          | Description                                          |
| ---------------- | ------------- | ---------------------------------------------------- |
| film_api_output  | dict or list  | Film data fetched from the API                       |
| film_api_error   | dict          | Error message if fetching data fails                 |

## License

Released under the MIT License.
