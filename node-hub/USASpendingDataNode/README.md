# usaspending_data_node

A Dora-rs node that fetches top-tier US Federal agency spending data from the USAspending.gov public API and streams it to downstream nodes for further analysis or visualization.

## Features
- Retrieves up-to-date top-level agency spending from USAspending.gov
- Exposes the entire JSON API response on an output topic
- Graceful error handling and reporting in output stream

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
  - id: usaspending_data_node
    build: pip install -e .
    path: usaspending_data_node
    inputs:
      user_input: input/user_input
    outputs:
      - usaspending_data
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
  - id: your_input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input

  - id: usaspending_data_node
    build: pip install -e .
    path: usaspending_data_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - usaspending_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (this input is just a trigger)
* Metadata:

  ```json
  {
    "description": "Any value; serves as a trigger for API call."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type        | Description                                                   |
| ---------- | ----------- | ------------------------------------------------------------- |
| user_input | Any         | Dummy trigger value to initiate the data fetch process        |

### Output Topics

| Topic             | Type  | Description                                                                |
| ----------------- | ----- | -------------------------------------------------------------------------- |
| usaspending_data  | JSON  | JSON response from the USAspending API, or error string in case of failure |


## License

Released under the MIT License.
