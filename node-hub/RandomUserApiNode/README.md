# random_user_api_node

Fetch random user data from an external API and expose it as a Dora node output, suitable for dataflow pipelines and integration with other Dora-rs nodes.

## Features
- Retrieves random user data from https://randomuser.me API
- Accepts parameterized requests via `user_input`
- Outputs data in JSON serializable format for seamless downstream consumption

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
  - id: randomuser
    build: pip install -e .
    path: random_user_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - random_user_data
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
  - id: randomuser
    build: pip install -e .
    path: random_user_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - random_user_data

  - id: consumer
    build: pip install your-consumer-package
    path: your_consumer_node
    inputs:
      random_user_data: randomuser/random_user_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable trigger (e.g., string)
* Metadata:

  ```json
  {
    "description": "Parameter to trigger fetching new user data. Can be empty or arbitrary trigger."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                               |
| ----------| ------ | ------------------------------------------ |
| user_input | Any    | Triggers the request to fetch user data   |

### Output Topics

| Topic            | Type  | Description                                  |
| ---------------- | ----- | -------------------------------------------- |
| random_user_data | dict  | Random user data returned from API (JSON)    |

## License

Released under the MIT License.
