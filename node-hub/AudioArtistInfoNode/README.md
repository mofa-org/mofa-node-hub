# audio_artist_node

Provides artist information retrieval from TheAudioDB API for music knowledge workflows.

## Features
- Retrieves detailed musical artist information from TheAudioDB
- Accepts artist names as parameters and falls back to a default if none provided
- Designed for integration in Dora-rs/MOFA dataflow pipelines

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
  - id: audio-artist-info
    build: pip install -e audio_artist_node
    path: audio_artist_node
    inputs:
      user_input: input/user_input
      artist_name: input/artist_name
    outputs:
      - artist_info
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
  - id: custom-input
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - artist_name
      - user_input

  - id: audio-artist-info
    build: pip install -e audio_artist_node
    path: audio_artist_node
    inputs:
      user_input: custom-input/user_input
      artist_name: custom-input/artist_name
    outputs:
      - artist_info
```

Your point source must output:

* Topic: `artist_name`
* Data: String containing the artist's name to look up
* Metadata:

  ```json
  {
    "data_type": "string",
    "description": "Artist name for lookup (defaults to 'coldplay' if not provided)"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                              |
| ------------ | ------ | ---------------------------------------- |
| user_input   | string | Upstream contextual/triggering parameter |
| artist_name  | string | Musical artist to look up (fallback if not provided) |

### Output Topics

| Topic        | Type    | Description                 |
| ------------ | ------- | --------------------------- |
| artist_info  | string (JSON) | TheAudioDB info response or error message (JSON serialized) |


## License

Released under the MIT License.
