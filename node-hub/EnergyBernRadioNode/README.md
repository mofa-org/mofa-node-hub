# energy_bern_radio

A Dora-rs node that fetches the radio playlist from Energy Bern, exposing the playlist via a simple REST call integration. This node can be used to retrieve the latest playouts (songs played) from the Energy Bern radio channel and share the result with other Dora nodes in your pipeline.

## Features
- Retrieves live playlist data from the Energy Bern API
- Provides structured error handling for HTTP and serialization failures
- Compatible as a plug-and-play Dora-rs node for information integration

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
  - id: energy_bern_radio
    build: pip install -e .
    path: energy_bern_radio
    inputs:
      user_input: input/user_input  # Dummy input for dataflow consistency
    outputs:
      - radio_playlist_response
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
  - id: point_source
    build: pip install your-node
    path: your-point-source-node
    outputs:
      - user_input

  - id: energy_bern_radio
    build: pip install -e .
    path: energy_bern_radio
    inputs:
      user_input: point_source/user_input
    outputs:
      - radio_playlist_response
```

Your point source must output:

* Topic: `user_input`
* Data: (any type, not used by this node)
* Metadata:

  ```json
  {
    "description": "Dummy input; value is ignored; required only for dataflow consistency."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | any    | Dummy parameter for triggering data retrieval |

### Output Topics

| Topic                  | Type           | Description                          |
| ---------------------- | -------------- | ------------------------------------ |
| radio_playlist_response| dict or string | Playlist data or error information   |

## License

Released under the MIT License.
