# cvedatabase_node

Vulnerability DB Query Node for Dora-rs

## Features
- Receive and handle user input parameters for vulnerability queries
- Query the Shodan CVE database API for vulnerability details
- Return vulnerability information or error details to output channels

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
  - id: cve_query
    build: pip install -e cvedatabase_node
    path: cvedatabase_node
    inputs:
      user_input: input/user_input
    outputs:
      - vuln_info
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
  - id: cve_query
    build: pip install -e cvedatabase_node
    path: cvedatabase_node
    inputs:
      user_input: your_input_node/user_input
    outputs:
      - vuln_info
```

Your point source must output:

* Topic: `user_input`
* Data: User query string or object (e.g., a CVE ID)
* Metadata:

  ```json
  {
    "parameter_name": "user_input",
    "description": "CVE ID or vulnerability search term",
    "example": "CVE-2016-10087"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type     | Description                       |
| ----------- | -------- | --------------------------------- |
| user_input  | String   | CVE ID or vulnerability query     |

### Output Topics

| Topic      | Type      | Description                               |
| ---------- | --------- | ----------------------------------------- |
| vuln_info  | Object    | Vulnerability details or error information |


## License

Released under the Apache-2.0 License.
