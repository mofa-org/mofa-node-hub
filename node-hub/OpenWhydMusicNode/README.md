# openwhyd_music_node

A Dora-rs node for fetching curated music recommendations from the [OpenWhyd](https://openwhyd.org) community API. This node retrieves Adrien's playlist and public YouTube music API data for integration in real-time media pipelines.

## Features
- Fetches the latest 20 tracks from OpenWhyd user Adrien
- Retrieves YouTube Music-related public API metadata via OpenWhyd
- Robust error handling for service outages or malformed responses

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
  - id: music_node
    build: pip install -e .
    path: openwhyd_music_node
    inputs:
      user_input: input/user_input  # For dataflow compliance (can be omitted if stateless)
    outputs:
      - music_api_response
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
  - id: music_node
    build: pip install -e .
    path: openwhyd_music_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - music_api_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any serializable value (the OpenWhydMusicNode ignores the content, but the connection is required for dataflow compliance)
* Metadata:

  ```json
  {
    "type": "any",
    "description": "Optional user input for triggering API call (content ignored)."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                            |
| ----------- | ------ | ------------------------------------------------------|
| user_input  | any    | Optional user input for dataflow compliance           |

### Output Topics

| Topic              | Type          | Description                                                |
| ------------------ | ------------- | ----------------------------------------------------------|
| music_api_response | list[dict]    | List with results or errors for Adrien's tracks and YT API |

## License

Released under the MIT License.
