# bored_api_node

Event discovery and suggestion Dora node using the Bored API.

## Features
- Event lookup via price range constraints (minprice, maxprice)
- Event suggestions for a fixed number of participants
- Fetches a fully random event effortlessly

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
  - id: event_finder
    build: pip install -e .
    path: bored_api_node
    inputs:
      mode: input/mode
      minprice: input/minprice
      maxprice: input/maxprice
      participants: input/participants
      user_input: input/user_input
    outputs:
      - api_event
      - error
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
    build: pip install your-node
    path: your-node
    outputs:
      - minprice
      - maxprice
      - participants
      - mode
      - user_input
  - id: event_finder
    build: pip install -e .
    path: bored_api_node
    inputs:
      minprice: your_input_node/minprice
      maxprice: your_input_node/maxprice
      participants: your_input_node/participants
      mode: your_input_node/mode
      user_input: your_input_node/user_input
    outputs:
      - api_event
      - error
```

Your point source must output:

* Topic: `minprice`, `maxprice`, `participants`, `mode`, `user_input`
* Data: strings, floats, or integers depending on field
* Metadata:

  ```json
  {
    "minprice": "string | float (optional)",
    "maxprice": "string | float (optional)",
    "participants": "string | int (optional)",
    "mode": "string: 'price', 'participants', or 'random'",
    "user_input": "string (optional)"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                                    |
| -------------|--------|----------------------------------------------------------------|
| minprice     | string/float | Minimum price filter (optional, for 'price' mode)             |
| maxprice     | string/float | Maximum price filter (optional, for 'price' mode)             |
| participants | string/int   | Number of participants (optional, for 'participants' mode)    |
| mode         | string      | Query mode: 'price', 'participants', or 'random'              |
| user_input   | string      | Optional free-form user input for context or chaining         |

### Output Topics

| Topic      | Type               | Description                              |
| ----------|--------------------|------------------------------------------|
| api_event | dict (JSON object) | Event result as returned by Bored API    |
| error     | dict (JSON object) | Error information (any failure message)  |


## License

Released under the MIT License.
