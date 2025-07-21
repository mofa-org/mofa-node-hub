# hackernews_data_node

A Dora node that fetches real-time public data from Hacker News, including stories, jobs, and comments, and outputs the results in a dora-rs-compliant message format.

## Features
- Fetches real-time Hacker News story, job, and comment data
- Provides clean, serialized JSON output for integration
- Drop-in Dora node: input/output fully dora-rs contract compliant

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
  - id: hackernews_data_node
    build: pip install -e .
    path: hackernews_data_node
    inputs:
      user_input: input/user_input
    outputs:
      - hackernews_data
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
  - id: your_point_source
    build: pip install your-source
    path: your_point_source
    outputs:
      - user_input

  - id: hackernews_data_node
    build: pip install -e .
    path: hackernews_data_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - hackernews_data
```

Your point source must output:

* Topic: `user_input`
* Data: Any str or dict (may be ignored by this node)
* Metadata:

  ```json
  {
    "type": "string or dict",
    "optional": true,
    "description": "Input for chaining or triggering."
  }
  ```

## API Reference

### Input Topics

| Topic              | Type   | Description                           |
| ------------------ | ------ | ------------------------------------- |
| user_input         | str or dict | Optional input for node chaining or trigger. |

### Output Topics

| Topic             | Type   | Description                                               |
| ----------------- | ------ | --------------------------------------------------------- |
| hackernews_data   | dict   | Dictionary with 'story', 'job', and 'comment' HN items.   |


## License

Released under the MIT License.
