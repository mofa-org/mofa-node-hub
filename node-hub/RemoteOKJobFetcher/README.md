# remoteok_job_fetcher

Fetch jobs from the RemoteOK API and emit them as outputs in a Dora-rs/MOFA workflow. This node provides a simple wrapper over the RemoteOK jobs API, delivering job postings as structured outputs and error handling for integration into declarative pipelines.

## Features
- Fetches the latest remote jobs from [RemoteOK](https://remoteok.com/)
- Filters and parses API output, handling malformed JSON gracefully
- Emits both job lists and fetch error notifications for downstream nodes

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
  - id: job_fetcher
    build: pip install -e .
    path: remoteok_job_fetcher
    inputs:
      user_input: input/user_input  # Required by framework (can be empty)
    outputs:
      - remoteok_jobs
      - job_fetch_error
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
  - id: your_node
    build: pip install your-node
    path: your-node
    outputs:
      - user_input

  - id: job_fetcher
    build: pip install -e .
    path: remoteok_job_fetcher
    inputs:
      user_input: your_node/user_input
    outputs:
      - remoteok_jobs
      - job_fetch_error
```

Your point source must output:

* Topic: `user_input`
* Data: Can be any placeholder (not actually used)
* Metadata:

  ```json
  {
    "description": "Placeholder for agent dataflow compatibility. Value can be empty or null."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type  | Description                                     |
| ----------- | ----- | ----------------------------------------------- |
| user_input  | any   | Required parameter to trigger the agent action. |

### Output Topics

| Topic           | Type   | Description                           |
| --------------- | ------ | ------------------------------------- |
| remoteok_jobs   | array  | Array of job objects from RemoteOK.   |
| job_fetch_error | object | Error info if fetch/parse fails.      |


## License

Released under the MIT License.
