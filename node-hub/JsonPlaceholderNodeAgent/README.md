# json_placeholder_node

Fetch post details, all posts, and comments for a post from the JSONPlaceholder API in a Dora-rs node.

## Features
- Retrieve details for a single post (post id 1)
- Fetch all posts in bulk
- Get comments related to post id 1

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
  - id: json_api
    build: pip install -e .
    path: json_placeholder_node
    inputs:
      user_input: input/user_input  # Dummy input, can connect to timer or constant
    outputs:
      - post_details
      - all_posts
      - post_comments
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
  - id: json_api
    build: pip install -e .
    path: json_placeholder_node
    inputs:
      user_input: input/user_input
    outputs:
      - post_details
      - all_posts
      - post_comments

  - id: my_consumer
    build: pip install my-consumer-node
    path: my-consumer-node
    inputs:
      post_details: json_api/post_details
      all_posts: json_api/all_posts
      post_comments: json_api/post_comments
```

Your point source must output:

* Topic: `user_input`
* Data: Any value (can be a dummy tick or empty string)
* Metadata:

  ```json
  {
    "description": "Dummy input to trigger fetching from the API. Can be a tick, empty, or string."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                       |
| ----------- | ------ | --------------------------------- |
| user_input  | Any    | Dummy trigger to invoke the node.  |

### Output Topics

| Topic         | Type    | Description                                         |
| ------------- | ------- | --------------------------------------------------- |
| post_details  | object  | Details of post with id 1                            |
| all_posts     | array   | List of all posts                                   |
| post_comments | array   | All comments for post id 1                          |

## License

Released under the MIT License.
