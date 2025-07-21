# advice_slip_node

A Dora-rs node that fetches advice from the Advice Slip public API and outputs the response for downstream consumption. The node demonstrates external API integration and robust error handling, returning JSON results for integration with other Dora nodes.

## Features
- Fetches advice from https://api.adviceslip.com
- Simple Dora-rs node integration pattern
- Graceful error handling with structured output

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
  - id: advice_slip_node
    build: pip install -e .
    path: advice_slip_node
    inputs:
      user_input: input/user_input
    outputs:
      - advice_slip_response
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
  - id: your_input_source
    build: pip install your-input-source
    path: your_input_source
    outputs:
      - user_input

  - id: advice_slip_node
    build: pip install -e .
    path: advice_slip_node
    inputs:
      user_input: your_input_source/user_input
    outputs:
      - advice_slip_response
```

Your point source must output:

* Topic: `user_input`
* Data: Arbitrary data (not used, may be left empty)
* Metadata:

  ```json
  {
    "description": "User request or trigger for AdviceSlipNode. Any type, not utilized by the node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                              |
| ----------| ------ | --------------------------------------------------------|
| user_input | any    | Input trigger or parameter for execution (not required) |

### Output Topics

| Topic                | Type   | Description                                                            |
| -------------------- | ------ | ---------------------------------------------------------------------- |
| advice_slip_response | dict   | JSON advice slip data or error details if API call fails                |


## License

Released under the MIT License.
