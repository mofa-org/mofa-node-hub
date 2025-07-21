# color_api_node

A Dora-rs node for bridging to [TheColorAPI](https://www.thecolorapi.com/) for RGB/HEX color lookups and color scheme queries using REST. Supports flexible parameterization (RGB, HEX, and color scheme modes), and emits structured color info as output.

## Features
- Query color information by HEX or RGB values via TheColorAPI
- Generate color schemes (triad, palette) from HEX or RGB inputs
- Outputs structured color data or error details as Dora messages

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
  - id: color_api_node
    build: pip install -e .
    path: color_api_node
    inputs:
      parameters: input/parameters  # Parameters delivered as Dora message
    outputs:
      - color_api_output
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
    build: pip install -e your_source
    path: your_source
    outputs:
      - parameters # Must output in required format
  - id: color_api_node
    build: pip install -e color_api_node
    path: color_api_node
    inputs:
      parameters: your_point_source/parameters
    outputs:
      - color_api_output
```

Your point source must output:

* Topic: `parameters`
* Data: Dict with at least `query_type` and `value` fields (see below)
* Metadata:

  ```json
  {
    "fields": ["query_type", "value"],
    "query_type": "One of 'hex', 'rgb', 'scheme_hex', 'scheme_rgb'",
    "value": "Color value string: e.g. 'ffda32' or 'rgb(53,12,32)'"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type       | Description                                            |
| ---------- | ---------- | ----------------------------------------------------- |
| parameters | dict       | Parameters: `{"query_type": <mode>, "value": <val>}` |

### Output Topics

| Topic             | Type | Description                                                   |
| ----------------- | ---- | ------------------------------------------------------------- |
| color_api_output  | dict | Color or scheme info (as received from TheColorAPI, or error) |


## License

Released under the MIT License.
