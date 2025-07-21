# nasa_asteroid_node

A Dora node for accessing NASA's Near Earth Object (NEO) data APIs. This node exposes configurable endpoints to retrieve asteroid feeds by date or browse the NASA NEO database in real time, making it easy to plug live asteroid data into your workflow.

## Features
- Access NASA's live Near Earth Object asteroid feed by date range.
- Browse the NEO small bodies catalog through REST API.
- Flexible downstream integration and error reporting via Dora messaging system.

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
  - id: nasa_asteroid_node
    build: pip install -e .
    path: nasa_asteroid_node
    env:
      NASA_API_KEY: "<your-nasa-api-key>"
    inputs:
      service_type: input/service_type
      user_input: input/user_input
      start_date: input/start_date
      end_date: input/end_date
    outputs:
      - feed_output
      - browse_output
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
  - id: your_point_source_node
    build: pip install -e your-point-source
    path: your-point-source
    outputs:
      - service_type
      - user_input
      - start_date
      - end_date
  - id: nasa_asteroid_node
    build: pip install -e .
    path: nasa_asteroid_node
    inputs:
      service_type: your_point_source_node/service_type
      user_input: your_point_source_node/user_input
      start_date: your_point_source_node/start_date
      end_date: your_point_source_node/end_date
    outputs:
      - feed_output
      - browse_output
      - error
```

Your point source must output:

* Topic: `service_type`, `user_input`, `start_date`, `end_date`
* Data: Service selection string and parameters for the NASA API
* Metadata:

  ```json
  {
    "service_type": "feed | browse",
    "user_input": "<any string input> (optional)",
    "start_date": "YYYY-MM-DD (feed mode)",
    "end_date": "YYYY-MM-DD (feed mode)"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type   | Description                                                               |
| ------------| ------ | ------------------------------------------------------------------------- |
| service_type | str    | Which NASA NEO endpoint to call: "feed" for date search, "browse" to list |
| user_input   | str    | User text input (for downstream API compatibility; optional)              |
| start_date   | str    | Start date in YYYY-MM-DD (use with service_type: feed)                    |
| end_date     | str    | End date in YYYY-MM-DD (use with service_type: feed)                      |

### Output Topics

| Topic         | Type         | Description                                           |
| ------------- | ------------| ----------------------------------------------------- |
| feed_output   | dict         | Response from /feed endpoint (neo feed by date)       |
| browse_output | dict         | Response from /neo/browse endpoint                    |
| error         | str or dict  | Error messages and diagnostics                        |

## License

Released under the MIT License.
