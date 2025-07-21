# bonequest_episode

A Dora-rs node that fetches a specific episode from the BoneQuest webcomic API (episode 420). The node performs an HTTP GET request, serializes the API response, and delivers it downstream as an output. Designed for integration into machine orchestrated pipelines (Mofa/Dora).

## Features
- Fetches BoneQuest episode data from the public API
- Serializes HTTP and error responses into structured output
- Simple integration into Dora/Mofa pipelines

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
  - id: bonequest_fetcher
    build: pip install -e .
    path: bonequest_episode
    inputs:
      user_input: input/user_input
    outputs:
      - bonequest_episode
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
  - id: my_node
    build: pip install my-node
    path: path/to/my-node
    outputs:
      - user_input
  - id: bonequest_fetcher
    build: pip install -e .
    path: bonequest_episode
    inputs:
      user_input: my_node/user_input
    outputs:
      - bonequest_episode
```

Your point source must output:

* Topic: `user_input`
* Data: Any (dummy input)
* Metadata:

  ```json
  {
    "description": "Dummy parameter to facilitate triggering of the fetch operation."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                        |
| ---------- | ------ | ------------------------------------------------------------------ |
| user_input | Any    | Dummy parameter required to trigger API fetch. Value is ignored.    |

### Output Topics

| Topic            | Type   | Description                                                                           |
| ---------------- | ------ | ------------------------------------------------------------------------------------- |
| bonequest_episode| JSON   | Episode data if successful, or error object with 'error' and 'message' if fetch fails. |


## License

Released under the MIT License.
