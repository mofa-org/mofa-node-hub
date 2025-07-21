# red_tide_node

Fetch the Latest Red Tide Situation Updates from the HK AFCD Portal

## Features
- Query up-to-date Hong Kong Red Tide Situation reports in Traditional Chinese, Simplified Chinese, or English
- Language-selective API: Choose your preferred language for the report
- Simple API integration for Dora workflows, outputting structured JSON

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
  - id: red_tide_node
    build: pip install -e .
    path: red_tide_node
    inputs:
      language: input/language
    outputs:
      - red_tide_data
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
  - id: my_language_source
    build: pip install -e my_language_node
    path: my_language_node
    outputs:
      - language
  - id: red_tide_node
    build: pip install -e .
    path: red_tide_node
    inputs:
      language: my_language_source/language
    outputs:
      - red_tide_data
```

Your point source must output:

* Topic: `language`
* Data: String (`traditional`, `simplified`, `english`)
* Metadata:

  ```json
  {
    "type": "string",
    "allowed": ["traditional", "simplified", "english"]
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                                                                  |
|----------|--------|------------------------------------------------------------------------------|
| language | string | Language code. One of 'traditional', 'simplified', or 'english' (case-insensitive). |

### Output Topics

| Topic          | Type   | Description                                        |
|----------------|--------|----------------------------------------------------|
| red_tide_data  | JSON   | Dict with red tide data, source URL, description, or error information. |


## License

Released under the MIT License.
