# shikimori_anime_manga

Anime & Manga Search Node for Dora-rs via the Shikimori API.

## Features
- Fetches lists of anime or manga from the Shikimori public API
- Simple selection via the `content_type` parameter: choose 'anime' or 'manga'
- Outputs results as JSON for seamless downstream integration

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
  - id: shikimori_node
    build: pip install -e shikimori_anime_manga
    path: shikimori_anime_manga
    inputs:
      content_type: input/content_type
    outputs:
      - shikimori_result
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
  - id: your_input_node
    build: pip install your-node
    path: your-node
    outputs:
      - content_type

  - id: shikimori_node
    build: pip install -e shikimori_anime_manga
    path: shikimori_anime_manga
    inputs:
      content_type: your_input_node/content_type
    outputs:
      - shikimori_result
      - error
```

Your point source must output:

* Topic: `content_type`
* Data: String of either `anime` or `manga`
* Metadata:

  ```json
  {
    "description": "Content type for search: 'anime' or 'manga'",
    "type": "string"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                        |
| -------------| ------ | -----------------------------------|
| content_type  | string | 'anime' or 'manga' to select type  |

### Output Topics

| Topic            | Type         | Description                                           |
| ----------------| ------------ | ----------------------------------------------------- |
| shikimori_result| list/object  | List of anime/manga results from Shikimori API        |
| error           | string       | Error message if something went wrong                 |


## License

Released under the MIT License.
