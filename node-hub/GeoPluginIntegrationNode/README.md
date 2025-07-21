# geoplugin_node

Integrates with the GeoPlugin.net public API to provide currency conversion rates or IP geolocation data, via easily configurable Dora-rs node inputs for use in dataflows.

## Features
- Seamless integration with the GeoPlugin.net public web API
- Supports both currency conversion (custom base currency) and IP geolocation lookup modes
- Returns deserialized, ready-to-use dictionary/JSON responses for downstream processing

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
  - id: geoplugin
    build: pip install -e geoplugin_node
    path: geoplugin_node
    inputs:
      mode: input/mode
      base_currency: input/base_currency
    outputs:
      - result
    env: {}
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
  - id: your_point_source_node
    build: pip install -e your_point_source_node
    path: your_point_source_node
    outputs:
      - mode
      - base_currency
  - id: geoplugin
    build: pip install -e geoplugin_node
    path: geoplugin_node
    inputs:
      mode: your_point_source_node/mode
      base_currency: your_point_source_node/base_currency
    outputs:
      - result
```

Your point source must output:

* Topic: `mode`
* Data: 'currency_converter' or 'ip_geolocation' (string)
* Topic: `base_currency` (optional)
* Data: Base currency code (e.g., 'EUR', 'USD') as string
* Metadata:

  ```json
  { "dtype": "str", "description": "Request mode or base currency for geoplugin" }
  ```

## API Reference

### Input Topics

| Topic         | Type   | Description                                             |
| -------------|--------|--------------------------------------------------------|
| mode         | str    | 'currency_converter' or 'ip_geolocation'               |
| base_currency| str    | Base currency (e.g., 'EUR', 'USD'); optional, default 'EUR' |

### Output Topics

| Topic  | Type | Description                       |
|--------|------|----------------------------------|
| result | dict | GeoPlugin API response (JSON/dict)|

## License

Released under the MIT License.
