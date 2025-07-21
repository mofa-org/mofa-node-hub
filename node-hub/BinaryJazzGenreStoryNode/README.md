# binaryjazz_genre_story

Generate Random Genres and Stories using BinaryJazz API

## Features
- Fetches random genres from the BinaryJazz Genrenator API
- Retrieves quirky short stories from the BinaryJazz Story API
- Provides error outputs for reliable orchestration

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
  - id: genre_story
    build: pip install -e binaryjazz_genre_story
    path: binaryjazz_genre_story
    inputs:
      user_input: input/user_input
    outputs:
      - genre_result
      - story_result
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
  - id: my_input
    build: pip install -e my-input-node
    path: my-input-node
    outputs:
      - user_input

  - id: genre_story
    build: pip install -e binaryjazz_genre_story
    path: binaryjazz_genre_story
    inputs:
      user_input: my_input/user_input
    outputs:
      - genre_result
      - story_result
```

Your point source must output:

* Topic: `user_input`
* Data: Any payload (used for orchestration convenience)
* Metadata:

  ```json
  {
    "description": "Any data; not used but serves as a trigger."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                        |
| ----------- | ------- | ---------------------------------- |
| user_input  | Any     | Input payload to trigger API calls |

### Output Topics

| Topic         | Type        | Description                       |
| ------------- | ----------- | --------------------------------- |
| genre_result  | JSON/dict   | List of random genres or error    |
| story_result  | JSON/dict   | List of random stories or error   |


## License

Released under the MIT License.
