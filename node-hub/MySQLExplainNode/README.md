# mysql_explain_node

Easily integrate MySQL query plan visualization and API analysis via mysqlexplain.com using Dora/MoFa. This node exposes EXPLAIN submission and iframe oEmbed retrieval as simple endpoints.

## Features
- Retrieve oEmbed iframe code for EXPLAIN plans
- Submit raw EXPLAIN plans or MySQL queries for API analysis
- Flexible configurable inputs and robust error handling

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
  - id: explain
    build: pip install -e mysql_explain_node
    path: mysql_explain_node
    inputs:
      user_input: dora/timer/millis/1000
    outputs:
      - result
    parameters:
      action: oembed
      url: https://mysqlexplain.com/plan/1234
      showFullscreenButton: 'true'
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
  - id: explain
    build: pip install -e mysql_explain_node
    path: mysql_explain_node
    inputs:
      user_input: your_trigger_node/trigger
    outputs:
      - result
    parameters:
      action: submit_explain
      query: "SELECT * FROM users WHERE id=42"
      version: "8.0.32"
      bindings: '[{"id":42}]'
      explain_json: "{}"
      explain_tree: "{}"
```

Your point source must output:

* Topic: `user_input`
* Data: Any value to trigger evaluation
* Metadata:

  ```json
  {
    "description": "Trigger input for explain actions, triggers parameter readout and API call"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type       | Description                                                       |
| ------------| ---------- | ----------------------------------------------------------------- |
| user_input   | any        | Triggers evaluation of the parameters and submission to the API    |
| action      | str        | "oembed" or "submit_explain"                                     |
| url         | str        | Required for oembed: URL of an EXPLAIN plan                       |
| showFullscreenButton | str ("true"/"false") | oembed: Show fullscreen button (default: 'true')             |
| query       | str        | submit_explain: MySQL query (default: 'SELECT 1')                 |
| version     | str        | submit_explain: MySQL version (optional)                          |
| bindings    | json str   | submit_explain: Bindings list as JSON string (default: [])         |
| explain_json| json str   | submit_explain: JSON EXPLAIN output (default: {})                  |
| explain_tree| json str   | submit_explain: Structured tree (default: {})                      |

### Output Topics

| Topic   | Type         | Description                     |
| ------- | ------------ | ------------------------------- |
| result  | dict or str  | API result or error message     |

## License

Released under the MIT License.
