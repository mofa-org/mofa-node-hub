# jikan_top_content

JikanTopContentNode: Dora-rs node for fetching real-time top anime, manga, recommendations, and personalities from the Jikan API (MAL) for data-driven workflows.

## Features
- Fetches top manga, anime, and anime recommendations from the Jikan API
- Retrieves top personalities in the anime/manga industry
- Outputs results on dedicated ports for easy pipeline integration

## Getting Started

### Installation
Install via cargo:
```bash
pip install requests
pip install -e .
```

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: jikan_top_content
    build: pip install -e .
    path: jikan_top_content
    inputs:
      user_input: input/user_input
    outputs:
      - top_manga
      - top_anime
      - anime_recommendations
      - top_people
      - status
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
  - id: jikan_top_content
    build: pip install -e .
    path: jikan_top_content
    inputs:
      user_input: my_node/my_output
    outputs:
      - top_manga
      - top_anime
      - anime_recommendations
      - top_people
      - status
```

Your point source must output:

* Topic: `user_input`
* Data: Any scalar or dummy value (for triggering)
* Metadata:

  ```json
  {
    "type": "string",
    "description": "User parameter or trigger input (not required, placeholder only)"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                       |
| -------------|--------|-----------------------------------|
| user_input    | any    | Input parameter (placeholder only) |

### Output Topics

| Topic                | Type     | Description                                      |
| -------------------- | -------- | ------------------------------------------------ |
| top_manga            | dict     | Top manga data from Jikan API                    |
| top_anime            | dict     | Top anime data from Jikan API                    |
| anime_recommendations| dict     | Recommended anime data from Jikan API            |
| top_people           | dict     | Top anime/manga personalities from Jikan API     |
| status               | dict     | Status of each output (OK, ERROR, EXCEPTION)     |


## License

Released under the MIT License.
