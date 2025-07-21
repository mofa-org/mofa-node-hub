# website_carbon_node

Estimate Website Carbon Emissions via Dora Node

## Features
- Estimates carbon emissions for any website using the WebsiteCarbon API
- Simple input: provide a website URL and get environmental impact data
- Handles API response errors and general request issues gracefully

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
  - id: websitecarbon
    build: pip install -e .
    path: website_carbon_node
    inputs:
      url: input/url
    outputs:
      - carbon_results
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
  - id: url_source
    # This node should output the URL you want to analyze
    build: pip install your-url-source
    path: your-url-source
    outputs:
      - url

  - id: websitecarbon
    build: pip install -e website_carbon_node
    path: website_carbon_node
    inputs:
      url: url_source/url
    outputs:
      - carbon_results
      - error
```

Your point source must output:

* Topic: `url`
* Data: website URL as a string
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Website URL to analyze (must be non-empty string)"
  }
  ```

## API Reference

### Input Topics

| Topic | Type | Description |
|-------|------|-------------|
| url   | string | Website URL to analyze (non-empty string) |

### Output Topics

| Topic          | Type   | Description                                 |
|--------------- |--------|---------------------------------------------|
| carbon_results | dict   | Carbon emission results from the API        |
| error          | dict   | Error info (if any problems are encountered)|

## License

Released under the MIT License.
