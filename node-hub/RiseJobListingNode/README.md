# rise_job_node

A Dora-rs node for retrieving remote and hybrid job listings from the Rise public API. This node allows flexible parameterized job searches, including pagination and sorting, and provides JSON job data suitable for use in distributed processing pipelines.

## Features
- Fetches job listings from the Rise public API
- Supports pagination, sorting, and location-based filtering via parameters
- Robust error handling for API and parameter issues

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
  - id: rise_job_node
    build: pip install -e .
    path: rise_job_node
    inputs: { parameters: input/parameters }
    outputs: [ job_listings ]
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
    build: pip install -e your_input_node
    path: your_input_node
    outputs: [ parameters ]

  - id: rise_job_node
    build: pip install -e .
    path: rise_job_node
    inputs: { parameters: your_input_node/parameters }
    outputs: [ job_listings ]
```

Your point source must output:

* Topic: `parameters`
* Data: Dictionary with any subset of: `page`, `limit`, `sort`, `sortedBy`, `jobLoc`
* Metadata:

  ```json
  {
    "page": "int, optional (default: 1)",
    "limit": "int, optional (default: 20)",
    "sort": "string, optional (default: desc)",
    "sortedBy": "string, optional (default: createdAt)",
    "jobLoc": "string, optional (default: '')"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type                | Description                                  |
| ---------- | ------------------- | -------------------------------------------- |
| parameters | Dict[str, Any]      | Search/call parameters for job API (see below) |

### Output Topics

| Topic         | Type                       | Description                                 |
| ------------- | -------------------------- | ------------------------------------------- |
| job_listings  | Dict (JSON, or error dict) | Response from Rise API with job listings or error |


## License

Released under the MIT License.
