# phantomjscloud_node

Easily access the PhantomJSCloud API via a Dora-rs node for headless website rendering and plain text extraction. This node proxies requests to PhantomJSCloud, yielding rendered content or web scraping output as structured JSON.

## Features
- Headless website rendering to plain text via PhantomJSCloud
- Handles input configuration and HTTP error reporting gracefully
- Easily plugs into Dora-rs pipelines for automated web scraping

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
  - id: phantomjscloud
    build: pip install -e .
    path: phantomjscloud_node
    environment:
      PHANTOMJS_CLOUD_KEY: "<your_api_key>"
    inputs:
      user_input: input/user_input
      url: input/url
    outputs:
      - phantomjscloud_response
      - phantomjscloud_error
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
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input
      - url
  - id: phantomjscloud
    build: pip install -e .
    path: phantomjscloud_node
    environment:
      PHANTOMJS_CLOUD_KEY: "<your_api_key>"
    inputs:
      user_input: your_input_node/user_input
      url: your_input_node/url
    outputs:
      - phantomjscloud_response
      - phantomjscloud_error
```

Your point source must output:

* Topic: `user_input`, `url`
* Data: String for `url`, arbitrary for `user_input`
* Metadata:

  ```json
  {
    "description": "user_input can be any value (reserved for future extension); url must be a valid website address as string."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                  |
| ----------- | ------ | -------------------------------------------- |
| user_input  | Any    | Placeholder, reserved for future extensions. |
| url         | String | Target website URL for PhantomJSCloud render |

### Output Topics

| Topic                   | Type  | Description                        |
| ----------------------- | ----  | ---------------------------------- |
| phantomjscloud_response | JSON  | Rendered output from PhantomJSCloud |
| phantomjscloud_error    | JSON  | JSON-formatted error message        |


## License

Released under the MIT License.
