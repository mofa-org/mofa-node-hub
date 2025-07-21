# github_repository_node

A Dora-rs node providing access to GitHub repository details and issues via the Ironoc.net public API. Supports querying repository metadata and issues dynamically from other Dora nodes or configurations.

## Features
- Fetches detailed metadata for a GitHub user's repositories
- Retrieves issue lists for a specific repository
- Easy parameterization for integration with wider Dora pipelines

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
  - id: github_repo
    build: pip install -e github_repository_node
    path: github_repository_node
    inputs:
      action: input/action
      username: input/username
      repository: input/repository
    outputs:
      - repo_detail
      - repo_issues
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
  - id: my_input_node
    build: pip install my-input-node  # your own node
    path: my_input_node
    outputs:
      - action
      - username
      - repository

  - id: github_repo
    build: pip install -e github_repository_node
    path: github_repository_node
    inputs:
      action: my_input_node/action
      username: my_input_node/username
      repository: my_input_node/repository
    outputs:
      - repo_detail
      - repo_issues
      - error
```

Your point source must output:

* Topic: `action`, `username`, `repository`
* Data: String (e.g., "repo_detail", "conorheffron", "ironoc")
* Metadata:

  ```json
  {
    "type": "string",
    "input_fields": ["action", "username", "repository"]
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                                  |
| ---------- | ------ | ----------------------------------------------------------- |
| action     | string | API action: either `repo_detail` or `repo_issues`           |
| username   | string | GitHub username (default: "conorheffron")                  |
| repository | string | GitHub repository name (default: "ironoc"); used for issues |

### Output Topics

| Topic       | Type           | Description                                    |
| ----------- | -------------- | ---------------------------------------------- |
| repo_detail | JSON/dict      | Repository detail list (for repo_detail action) |
| repo_issues | JSON/dict      | Repository issue list (for repo_issues action)  |
| error       | JSON/dict      | Error details and documentation link            |


## License

Released under the MIT License.
