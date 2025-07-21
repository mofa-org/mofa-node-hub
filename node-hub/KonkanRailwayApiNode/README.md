# konkan_railway_api_node

A Dora-rs node for real-time Konkan Railway data aggregation and relay. Fetches live station and train data from the public Konkan Railway API and makes it available inside a Dora graph for downstream consumption or relay.

## Features
- Fetches live list of Konkan Railway stations
- Retrieves up-to-date train status/details
- Dora integration via MofaAgent for parameter input and output relay

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: konkan_railway_api_node
    build: pip install -e .
    path: konkan_railway_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - konkan_railway_data
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
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input

  - id: konkan_railway_api_node
    build: pip install -e .
    path: konkan_railway_api_node
    inputs:
      user_input: my_input_node/user_input
    outputs:
      - konkan_railway_data
```

Your point source must output:

* Topic: `user_input`
* Data: string (can be any string as trigger)
* Metadata:

  ```json
  {
    "name": "user_input",
    "dtype": "string"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                           |
| ----------- | ------ | ------------------------------------- |
| user_input  | string | Trigger to fetch latest railway data  |

### Output Topics

| Topic                | Type    | Description                                              |
| -------------------- | ------- | ---------------------------------------------------------|
| konkan_railway_data  | object  | Dictionary with 'stations' and 'live_trains' information |

## License

Released under the MIT License.
