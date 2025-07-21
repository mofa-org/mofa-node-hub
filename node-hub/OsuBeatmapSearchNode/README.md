# osu_beatmap_node

Agent for interfacing with osu.direct's public beatmap search and info API for Dora-rs node pipelines.

## Features
- Search osu! beatmaps by query string using the official API
- Retrieve info for a specific beatmap by its ID
- Retrieve info for a specific beatmap set by its ID

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
  - id: osu_beatmap_search
    build: pip install -e .
    path: osu_beatmap_node
    inputs:
      mode: input/mode
      id: input/id  # only needed for mode 'beatmap' or 'set'
      params: input/params  # only needed for mode 'search'
    outputs:
      - osu_search_result
      - osu_beatmap_result
      - osu_beatmap_set_result
      - osu_error
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
  - id: controller
    build: pip install your-controller
    path: controller_node
    outputs:
      - mode
      - id
      - params

  - id: osu_beatmap_search
    build: pip install -e .
    path: osu_beatmap_node
    inputs:
      mode: controller/mode
      id: controller/id
      params: controller/params
    outputs:
      - osu_search_result
      - osu_beatmap_result
      - osu_beatmap_set_result
      - osu_error
```

Your point source must output:

* Topic: `mode`, `id`, `params` (as required by operation)
* Data: string values suitable for relevant osu!direct API endpoints
* Metadata:

  ```json
  {
    "mode": "search|beatmap|set",
    "id": "beatmap id as string (for mode: beatmap/set)",
    "params": "search string (for mode: search)"
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                                      |
|----------|--------|-------------------------------------------------|
| mode     | string | Operation mode: 'search', 'beatmap', or 'set'   |
| id       | string | Beatmap/set ID (required if mode is 'beatmap' or 'set') |
| params   | string | Search query (required if mode is 'search')     |

### Output Topics

| Topic                 | Type   | Description                                                                |
|-----------------------|--------|----------------------------------------------------------------------------|
| osu_search_result     | dict   | Result from the osu!direct search endpoint (mode: search)                  |
| osu_beatmap_result    | dict   | Result for a specific beatmap (mode: beatmap)                              |
| osu_beatmap_set_result| dict   | Result for a specific beatmap set (mode: set)                              |
| osu_error             | dict   | Error, includes failure details                                            |


## License

Released under the MIT License.
