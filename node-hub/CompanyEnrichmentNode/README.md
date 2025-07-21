# company_enrichment_node

Automated company domain enrichment for Dora/Mofa nodes via CompanyEnrich API.

## Features
- Fetches company metadata from a 3rd-party enrichment API.
- Seamless error handling with informative return messages.
- Credential management via environment variable for secure API access.

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
  - id: enrichment_node
    build: pip install -e company_enrichment_node
    path: company_enrichment_node
    inputs:
      domain: input/domain
      user_input: input/user_input
    outputs:
      - company_enrich_response
    env:
      COMPANY_ENRICH_TOKEN: "${COMPANY_ENRICH_TOKEN}"
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
  - id: domain_source
    build: pip install your-node
    path: your-node-directory
    outputs:
      - domain
      - user_input

  - id: enrichment_node
    build: pip install -e company_enrichment_node
    path: company_enrichment_node
    inputs:
      domain: domain_source/domain
      user_input: domain_source/user_input
    outputs:
      - company_enrich_response
```

Your point source must output:

* Topic: `domain`
* Data: string (the domain to enrich)
* Metadata:

  ```json
  {
    "description": "Target company domain (e.g., 'google.com')",
    "type": "string"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                        |
| ----------- | ------ | ---------------------------------- |
| domain      | string | Company domain to lookup/enrich    |
| user_input  | string | Upstream compatibility placeholder |

### Output Topics

| Topic                   | Type        | Description                                             |
| ----------------------- | ----------- | ------------------------------------------------------- |
| company_enrich_response | dict/string | API result (enriched data) or {"error": msg} on failure |
|                         |             |                                                         |


## License

Released under the MIT License.
