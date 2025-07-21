# startrek_season_node

Query Star Trek season info from the open stapi API and emit results as a Dora node.

## Features
- Fetch Star Trek season info using the [stapi.co](https://stapi.co) REST API
- Configurable `uid` parameter to target any season
- Outputs entire season metadata or error details in JSON

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
  - id: season_info
    build: pip install -e .
    path: startrek_season_node
    inputs:
      uid: input/uid
    outputs:
      - season_info
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
  - id: my_uid_source
    build: pip install my-uid-source
    path: my-uid-source
    outputs:
      - uid

  - id: season_info
    build: pip install -e .
    path: startrek_season_node
    inputs:
      uid: my_uid_source/uid
    outputs:
      - season_info
```

Your point source must output:

* Topic: `uid`
* Data: Star Trek season UID (string)
* Metadata:

  ```json
  {
    "type": "string",
    "desc": "Star Trek season UID (e.g. \"SAMA0000001633\")"
  }
  ```

## API Reference

### Input Topics

| Topic | Type | Description |
|-------|------|-------------|
| uid   | string | Star Trek season UID (e.g. "SAMA0000001633") |

### Output Topics

| Topic        | Type    | Description                              |
|--------------|---------|------------------------------------------|
| season_info  | object  | JSON object with season info or error    |

## License

Released under the MIT License.
