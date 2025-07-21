# audio_track_retriever

Fast, pluggable node for retrieving audio track data from the public TheAudioDB API for use in Dora-rs dataflows.

## Features
- Fetches track data on demand from TheAudioDB
- Error handling and safe, typed outputs
- Ready-to-integrate with other Dora-rs/MofaAgent pipelines

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
  - id: audio_track_retriever
    build: pip install -e audio_track_retriever
    path: audio_track_retriever
    inputs:
      user_input: upstream_node/user_input  # Optional; can leave blank or wire as needed
    outputs:
      - audio_tracks
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
  - id: upstream_node
    build: pip install -e your-upstream-node
    path: your-upstream-node
    outputs:
      - user_input
  - id: audio_track_retriever
    build: pip install -e audio_track_retriever
    path: audio_track_retriever
    inputs:
      user_input: upstream_node/user_input
    outputs:
      - audio_tracks
```

Your point source must output:

* Topic: `user_input`
* Data: (Any serializable payload required to keep the DAG alive or send input, even if unused)
* Metadata:

  ```json
  {
    "type": "string | dict | any",
    "required": false,
    "description": "Optional user parameter triggering downstream workflow. May remain unused."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type             | Description                                      |
| ---------- | ---------------- | ------------------------------------------------ |
| user_input | any              | Optional parameter, can be any serializable type |

### Output Topics

| Topic        | Type       | Description                                |
| ------------ | ---------- | ------------------------------------------ |
| audio_tracks | dict/list  | Raw result from TheAudioDB, or error object |


## License

Released under the MIT License.
