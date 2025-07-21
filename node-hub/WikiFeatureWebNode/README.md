# WikiFeatureWebNode

Fetch Wikipedia page content via MediaWiki API for use in Dora-rs pipelines (Python node).

## Features
- Fetches Wikipedia page revisions/content using the MediaWiki API
- Override target Wikipedia page dynamically via `titles` parameter
- Graceful error handling with error output topic

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
  - id: wiki_node
    build: pip install -e .
    path: wiki_feature_node
    inputs:
      user_input: input/user_input
      titles: input/titles
    outputs:
      - wiki_content
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
  - id: input_node
    build: pip install your-input-node  # Replace as needed
    path: your-input-node
    outputs:
      - titles
  - id: wiki_node
    build: pip install -e .
    path: wiki_feature_node
    inputs:
      titles: input_node/titles
    outputs:
      - wiki_content
      - error
```

Your point source must output:

* Topic: `titles`
* Data: String (Wikipedia page title)
* Metadata:

  ```json
  {
    "dtype": "str",
    "desc": "Target Wikipedia page title (e.g., 'cat', 'dog', etc.)"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                |
| ----------|--------|-----------------------------------------------------------|
| user_input | any    | Placeholder for compliance; not utilized in processing    |
| titles     | str    | (Optional) Wikipedia page title to fetch (e.g. "cat")    |

### Output Topics

| Topic        | Type  | Description                                    |
| ------------|-------|------------------------------------------------|
| wiki_content | dict  | Raw MediaWiki JSON response for given title    |
| error        | str   | Error message encountered during fetch         |


## License

Released under the MIT License.
