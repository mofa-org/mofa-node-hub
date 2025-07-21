# heat_stress_warning_node

Real-time Heat Stress Warning Fetcher for Hong Kong Observatory

## Features
- Retrieves Heat Stress at Work Warnings from Hong Kong Observatory
- Supports multiple languages: English, Traditional Chinese, Simplified Chinese
- Robust error handling with simple API integration

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
  - id: heat_stress_warning_node
    build: pip install -e .
    path: heat_stress_warning_node
    inputs:
      lang: input/lang
    outputs:
      - warning_data
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
  - id: lang_source
    build: pip install your-lang-source
    path: your-lang-source
    outputs:
      - lang

  - id: heat_stress_warning_node
    build: pip install -e .
    path: heat_stress_warning_node
    inputs:
      lang: lang_source/lang
    outputs:
      - warning_data
```

Your point source must output:

* Topic: `lang`
* Data: String value ('en', 'tc', or 'sc')
* Metadata:

  ```json
  {
    "description": "Language code for warning (en, tc, sc)",
    "type": "string",
    "required": true
  }
  ```

## API Reference

### Input Topics

| Topic | Type | Description |
| ----- | ---- | ----------- |
| lang  | str  | Language code: 'en', 'tc', or 'sc' |

### Output Topics

| Topic        | Type          | Description                                         |
| ------------ | -------------| --------------------------------------------------- |
| warning_data | dict or str   | JSON or plaintext with Heat Stress Warning/results  |


## License

Released under the MIT License.
