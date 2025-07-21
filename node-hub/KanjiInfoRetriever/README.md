# kanji_info_retriever

Retrieve information about specific kanji characters from an open API (kanjiapi.dev) and make them available as output for other Dora nodes. This node can be triggered with any user-provided input to perform the query and return kanji data.

## Features
- Fetch detailed kanji metadata from kanjiapi.dev
- Simple trigger via parameter input (`user_input`)
- Robust error handling via JSON output

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
  - id: kanji_info
    build: pip install -e .
    path: kanji_info_retriever
    inputs:
      user_input: input/user_input
    outputs:
      - kanji_info
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
  - id: kanji_info
    build: pip install -e kanji_info_retriever
    path: kanji_info_retriever
    inputs:
      user_input: my_trigger_node/trigger_signal
    outputs:
      - kanji_info

  - id: downstream_consumer
    build: pip install -e .
    path: downstream_consumer
    inputs:
      kanji_info: kanji_info/kanji_info
```

Your point source must output:

* Topic: `user_input`
* Data: Any trigger signal (string or object)
* Metadata:

  ```json
  {
    "description": "Any data to trigger the kanji info retrieval"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                               |
| ----------- | ------ | ----------------------------------------- |
| user_input  | any    | Any input to trigger the kanji lookup     |

### Output Topics

| Topic       | Type    | Description                                     |
| ----------- | ------- | ----------------------------------------------- |
| kanji_info  | object  | Metadata for the fetched kanji character        |


## License

Released under the MIT License.
