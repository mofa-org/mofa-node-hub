# liturgical_calendar_node

Access the daily liturgical calendar entry and available calendar lists from the inadiutorium.cz public API.

## Features
- Retrieve today’s liturgical calendar including feast, celebration, and associated metadata
- List all available liturgical calendar types via simple HTTP API integration
- Easy Dora-rs node integration: stateless, chaining friendly, and no authentication required

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
  - id: liturgical_calendar
    build: pip install -e .
    path: liturgical_calendar_node
    inputs:
      user_input: input/user_input
    outputs:
      - calendar_result
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
  - id: your_node
    build: pip install your-node
    path: your-node
    outputs:
      - user_input

  - id: liturgical_calendar
    build: pip install -e .
    path: liturgical_calendar_node
    inputs:
      user_input: your_node/user_input
    outputs:
      - calendar_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any value to trigger the integration
* Metadata:

  ```json
  {
    "description": "Arbitrary stateless parameter, always required by this node for chaining. Ignored by logic."
  }
  ```

## API Reference

### Input Topics

| Topic        | Type     | Description                                                               |
| ------------|----------|---------------------------------------------------------------------------|
| user_input   | Any      | Stateless parameter used in Dora-rs pipelines. Value is ignored in logic.  |

### Output Topics

| Topic            | Type     | Description                                                                                         |
|------------------|----------|-----------------------------------------------------------------------------------------------------|
| calendar_result  | dict     | Dict containing today’s liturgical calendar entry, list of calendars, and any API error messages.    |

## License

Released under the MIT License.
