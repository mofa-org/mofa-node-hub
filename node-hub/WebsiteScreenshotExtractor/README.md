# WebsiteScreenshotExtractor

Fetch website screenshots and metadata via screenshotof.com API

## Features
- Capture instant screenshots of public websites
- Fetch historical screenshots by date
- Returns full response with metadata and error reporting

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
  - id: website_screenshoter
    build: pip install -e website_screenshot
    path: website_screenshot
    inputs:
      user_input: input/user_input
      target_url: input/target_url
      mode: input/mode
      date: input/date
    outputs:
      - screenshot_data
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
  - id: my_input_source
    build: pip install my-input-node
    path: input_node
    outputs:
      - target_url
      - mode
      - date

  - id: website_screenshoter
    build: pip install -e website_screenshot
    path: website_screenshot
    inputs:
      target_url: my_input_source/target_url
      mode: my_input_source/mode
      date: my_input_source/date
      user_input: input/user_input
    outputs:
      - screenshot_data
```

Your point source must output:

* Topic: `target_url`, `mode`, `date` (if using historical mode)
* Data: string (URL), string ('current' or 'historical'), string (YYYY-MM)
* Metadata:

  ```json
  {
    "target_url": "(string, required)",
    "mode": "current | historical",
    "date": "YYYY-MM (optional, for historical mode)"
  }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                         |
| -------------|--------|-------------------------------------|
| user_input    | any    | Input for dataflow consistency      |
| target_url   | str    | Website URL to screenshot           |
| mode         | str    | 'current' or 'historical' selection |
| date         | str    | YYYY-MM if mode='historical'        |

### Output Topics

| Topic            | Type        | Description |
|------------------|-------------|-------------|
| screenshot_data  | dict        | Screenshot response or error data |


## License

Released under the MIT License.
