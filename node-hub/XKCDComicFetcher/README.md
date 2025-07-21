# XKCDComicFetcher

Fetch XKCD comics as JSON data for easy pipeline integration.

## Features
- Retrieves XKCD comic #614
- Fetches the latest XKCD comic
- Handles chained parameter passing for node integration

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
  - id: xkcd_comic_fetcher
    build: pip install -e .
    path: xkcd_comic_fetcher
    inputs:
      user_input: input/user_input
    outputs:
      - xkcd_comics
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
  - id: xkcd_comic_fetcher
    build: pip install -e .
    path: xkcd_comic_fetcher
    inputs:
      user_input: your_node/next_step_trigger
    outputs:
      - xkcd_comics
```

Your point source must output:

* Topic: `user_input`
* Data: Any string or JSON object required for chaining
* Metadata:

  ```json
  {
    "description": "Used to trigger XKCDComicFetcher run from an upstream node; content can be empty or a context string."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                   |
| ----------- | ------ | --------------------------------------------- |
| user_input  | Any    | Triggers a fetch; enables chaining from nodes |

### Output Topics

| Topic        | Type   | Description                                                   |
| ------------ | ------ | ------------------------------------------------------------- |
| xkcd_comics  | JSON   | Dictionary with XKCD #614 and latest comic (errors as needed) |

## License

Released under the MIT License.
