# ringtone_search_node

Ringtone search node for MOFA/Dora-rs pipelines. This node performs an HTTP GET request to a configurable API endpoint to retrieve ringtone search results for a user-specified or default keyword, and outputs the structured API response.

## Features
- Query customizable ringtone search API endpoints
- Accept user parameter input (with fallback to env default)
- Emits structured JSON response for downstream consumption

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
  - id: ringtone_search
    build: pip install -e ringtone_search_node
    path: ringtone_search_node
    inputs:
      user_input: input/user_input
    outputs:
      - api_response
    env:
      API_ENDPOINT: "https://abhi-api.vercel.app/api/search/ringtone"
      DEFAULT_TEXT: "iPhone"
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
    build: pip install your-point-source
    path: your-point-source
    outputs:
      - user_input
  - id: ringtone_search
    build: pip install -e ringtone_search_node
    path: ringtone_search_node
    inputs:
      user_input: your_point_source/user_input
    outputs:
      - api_response
```

Your point source must output:

* Topic: `user_input`
* Data: String containing the query keyword
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Search string forwarded to the ringtone search node."
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| user_input | string | Search string to forward to the API endpoint |

### Output Topics

| Topic        | Type  | Description                             |
| ------------ | ----- | --------------------------------------- |
| api_response | JSON  | API response (JSON or error dictionary) |


## License

Released under the MIT License.

````
