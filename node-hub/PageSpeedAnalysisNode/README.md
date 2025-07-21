# pagespeed_analysis

Dora-rs node for PageSpeed Insights API analysis

## Features
- Analyze web page performance scores in real-time using the Google PageSpeed Insights API
- Configurable via environment variables (locale, strategy, timeout)
- Robust error handling with structured outputs

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
  - id: pagespeed
    build: pip install -e .
    path: pagespeed_analysis
    inputs:
      user_input: input/user_input
      target_url: input/target_url
    outputs:
      - pagespeed_data
    env:
      PAGESPEED_API_KEY: "<your_pagespeed_api_key>"
      PAGESPEED_LOCALE: "en_US"
      PAGESPEED_STRATEGY: "mobile"
      PAGESPEED_TIMEOUT: "30"
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
  - id: url_provider
    build: pip install my-url-node
    path: url_provider
    outputs:
      - target_url

  - id: pagespeed
    build: pip install -e .
    path: pagespeed_analysis
    inputs:
      target_url: url_provider/target_url
      user_input: input/user_input
    outputs:
      - pagespeed_data
```

Your point source must output:

* Topic: `target_url`
* Data: String (target page URL)
* Metadata:

  ```json
  {
    "type": "string",
    "required": true,
    "description": "URL to analyze via PageSpeed Insights API"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                          |
| ----------- | ------ | ------------------------------------ |
| user_input  | Any    | Placeholder for port chaining         |
| target_url  | string | The URL of the page to be analyzed   |

### Output Topics

| Topic           | Type | Description                                 |
| --------------- | ---- | ------------------------------------------- |
| pagespeed_data  | dict | PageSpeed Insights API results or error info |

## License

Released under the MIT License.
