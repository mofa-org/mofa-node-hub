# music_data_node

A Dora-rs node that retrieves and aggregates music intelligence data for a given recording using MusicBrainz and AcousticBrainz APIs. Focus example: fetches all available data for "Billie Jean" by Michael Jackson, including both low-level and high-level audio analysis.

## Features
- Fetches MusicBrainz Recording ID (MBID) for the specified song
- Aggregates AcousticBrainz high-level and low-level musical features
- Returns structured data suitable for downstream Dora dataflow integration

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
  - id: music_data_fetcher
    build: pip install -e .
    path: music_data_node
    inputs:
      user_input: input/user_input  # Optional, present for integration
    outputs:
      - music_data
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
  - id: input_node
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - user_input
  - id: music_data_fetcher
    build: pip install -e .
    path: music_data_node
    inputs:
      user_input: input_node/user_input
    outputs:
      - music_data
      - error
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable object or string representing the input query (optional for this node)
* Metadata:

  ```json
  {
    "usage": "optional; not directly consumed by music_data_node, but available for integration compatibility"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type    | Description                                           |
| ---------- | ------- | ----------------------------------------------------- |
| user_input | object  | (Optional) Input query for future expansion/integration |

### Output Topics

| Topic      | Type    | Description                                                  |
| ---------- | ------- | ------------------------------------------------------------ |
| music_data | object  | Music intelligence: MusicBrainz + AcousticBrainz metadata    |
| error      | string/object | Error information if retrieval fails                      |


## License

Released under the MIT License.
