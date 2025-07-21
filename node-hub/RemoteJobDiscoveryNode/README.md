# remote_job_discovery

A Dora-rs node for discovering remote jobs via the Jobicy API. This node enables seamless integration of remote job search within Dora workflows, allowing dynamic job queries over industry, tag, region, and more.

## Features
- Real-time remote job search via Jobicy REST API
- Flexible query customization (region, industry, tags, result count)
- Integrates as a modular agent node compatible with Dora/MOFA pipelines

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
  - id: job_finder
    build: pip install -e remote_job_discovery
    path: remote_job_discovery
    inputs:
      user_input: input/user_input
      count: input/count
      geo: input/geo
      industry: input/industry
      tag: input/tag
    outputs:
      - remote_job_results
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
  - id: input_source
    build: pip install your-custom-node
    path: your-custom-node
    outputs:
      - user_input
      - count
      - geo
      - industry
      - tag
  - id: job_finder
    build: pip install -e remote_job_discovery
    path: remote_job_discovery
    inputs:
      user_input: input_source/user_input
      count: input_source/count
      geo: input_source/geo
      industry: input_source/industry
      tag: input_source/tag
    outputs:
      - remote_job_results
```

Your point source must output:

* Topic: `user_input`, `count`, `geo`, `industry`,  `tag`
* Data: scalar (string or int as appropriate)
* Metadata:

  ```json
  {
    "user_input": "String",
    "count": "int (default 20)",
    "geo": "String (default 'usa')",
    "industry": "String (default 'marketing')",
    "tag": "String (default 'seo')"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                             |
| ----------| -------| --------------------------------------- |
| user_input| String | Generic input for chaining node workflows|
| count     | int    | Number of jobs to fetch (default 20)    |
| geo       | String | Geographical filter, e.g., 'usa'        |
| industry  | String | Industry filter, e.g., 'marketing'      |
| tag       | String | Tag filter, e.g., 'seo'                 |

### Output Topics

| Topic               | Type      | Description                            |
|---------------------|-----------|----------------------------------------|
| remote_job_results  | JSON dict | List/dict of jobs from Jobicy API, or error info |


## License

Released under the MIT License.
