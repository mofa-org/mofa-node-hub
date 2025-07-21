# runescape_group_hiscores

Query RuneScape Group HiScores via Dora-compatible MOFA agent node.

## Features
- Query group hiscores from the official RuneScape API
- Flexible filtering: group size, result size, boss ID, and page
- Outputs results as easily consumable structured data

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
  - id: runescape_group_hiscores
    build: pip install -e .
    path: runescape_group_hiscores
    inputs:
      parameters: dora/parameters  # (Optional - parameter input node)
    outputs:
      - group_hiscores
    env: {}
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
  - id: your_parameter_source
    build: pip install your-param-node
    path: your-param-node
    outputs:
      - parameters

  - id: runescape_group_hiscores
    build: pip install -e .
    path: runescape_group_hiscores
    inputs:
      parameters: your_parameter_source/parameters
    outputs:
      - group_hiscores
```

Your point source must output:

* Topic: `parameters`
* Data: JSON-serialized dictionary of parameters, e.g.:
* Metadata:

  ```json
  {
    "groupSize": "2",
    "size": "1",
    "bossId": "1",
    "page": "0"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                  |
| ----------|--------|-------------------------------------------------------------|
| parameters | dict   | Dictionary with keys: groupSize, size, bossId, page (str)   |

### Output Topics

| Topic          | Type   | Description                                                 |
|----------------|--------|------------------------------------------------------------|
| group_hiscores | dict   | RuneScape group hiscores query result (see API docs), or error |


## License

Released under the MIT License.
