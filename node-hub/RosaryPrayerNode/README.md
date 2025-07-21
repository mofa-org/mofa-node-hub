# rosary_prayer_node

A Dora-rs node for fetching Rosary prayers (text or audio) from public API endpoints. The node retrieves prayer data based on an input parameter and outputs structured JSON or text, suitable for devotional applications or integration with audio/visual prayer workflows.

## Features
- Fetches Rosary prayer text for Mondays
- Retrieves Rosary audio for today’s date
- Graceful error handling with clear error messages

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
  - id: rosary_prayer
    build: pip install -e .
    path: rosary_prayer_node
    inputs:
      prayer_type: input/prayer_type
    outputs:
      - monday_text
      - today_audio
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
  - id: input
    build: pip install -e .
    path: my-input-node
    outputs:
      - prayer_type

  - id: rosary_prayer
    build: pip install -e .
    path: rosary_prayer_node
    inputs:
      prayer_type: input/prayer_type
    outputs:
      - monday_text
      - today_audio
      - error
```

Your point source must output:

* Topic: `prayer_type`
* Data: string, either 'monday_text' or 'today_audio'
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Indicates which prayer to fetch: 'monday_text' for Monday prayers, or 'today_audio' for today's audio."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                    |
| ------------|--------|------------------------------------------------|
| prayer_type  | string | Specify which Rosary prayer to fetch. Supported values: 'monday_text', 'today_audio' |

### Output Topics

| Topic        | Type   | Description                                    |
| ------------ | ------ | -----------------------------------------------|
| monday_text  | json/text | Monday Rosary prayer (JSON or text from API)   |
| today_audio  | json/text | Today's Rosary audio (JSON or text from API)   |
| error        | json     | Error output (if an exception occurred)        |

## License

Released under the MIT License.
