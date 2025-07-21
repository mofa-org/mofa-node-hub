# radio_srf_music

Music Playlist Fetcher for SRF 1 Radio

## Features
- Fetches the current playlist (with timestamps) from the SRF 1 Radio channel via their public API
- Outputs structured JSON with song title, artist, start and end time
- Returns error information in output if fetching fails

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
  - id: radio_srf_music
    build: pip install -e .
    path: radio_srf_music
    inputs:
      user_input: input/user_input
    outputs:
      - radio_srf_1_song_list
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
  - id: radio_srf_music
    build: pip install -e .
    path: radio_srf_music
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - radio_srf_1_song_list

  - id: your_input_node
    build: pip install your-node
    path: your-input-node
    outputs:
      - user_input
```

Your point source must output:

* Topic: `user_input`
* Data: Any string (dummy value)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Dummy user input for trigger"
  }
  ```

## API Reference

### Input Topics

| Topic              | Type    | Description                   |
| ------------------ | ------- | ----------------------------- |
| user_input         | string  | Dummy string to allow chaining |

### Output Topics

| Topic                  | Type     | Description                                    |
| ---------------------- | -------- | ---------------------------------------------- |
| radio_srf_1_song_list  | JSON     | List of songs or error info {"error": ...}     |


## License

Released under the MIT License.
