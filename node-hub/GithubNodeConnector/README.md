# github_node_connector

A Dora-rs node that interacts with the GitHub API to retrieve user information, repository details, and specific repository file content (e.g., README.md). It can serve as a connector in dataflow pipelines, providing reproducible metadata from GitHub endpoints.

## Features
- Fetches GitHub user information for a specified user
- Retrieves detailed repository information for a given repo
- Obtains file contents (e.g., README) from GitHub repositories

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
  - id: github_connector
    build: pip install -e .
    path: github_node_connector
    inputs:
      user_input: input/user_input  # Placeholder for dataflow (optional)
    outputs:
      - user_info
      - repo_info
      - repo_content
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
  - id: my_custom_input
    build: pip install my-custom-input
    path: my_custom_input
    outputs:
      - user_input
  - id: github_connector
    build: pip install -e github_node_connector
    path: github_node_connector
    inputs:
      user_input: my_custom_input/user_input
    outputs:
      - user_info
      - repo_info
      - repo_content
```

Your point source must output:

* Topic: `user_input`
* Data: Any type (placeholder to allow upflow)
* Metadata:

  ```json
  {
    "description": "Placeholder for upflow data to satisfy the Dora data model. No required schema."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type    | Description                                    |
| ----------- | ------- | ---------------------------------------------- |
| user_input  | any     | Placeholder input to allow node chaining/dataflow |

### Output Topics

| Topic        | Type    | Description                                              |
| ------------ | ------- | -------------------------------------------------------- |
| user_info    | dict    | GitHub user information (from /users/rails)              |
| repo_info    | dict    | GitHub repository information (from /repos/rails/rails)  |
| repo_content | dict    | Contents of rails/rails/README.md (may be base64-encoded)|


## License

Released under the MIT License.
