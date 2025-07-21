# ChineseMedicineClinicAttendanceNode

A Dora-rs node for fetching the annual attendance data of Chinese Medicine Clinics cum Training and Research Centres in Hong Kong, with language selection support. This node exposes the latest data via a simple Dora-compatible API.

## Features
- Retrieve annual attendance statistics from Hong Kong public endpoints
- Supports multiple languages: English, Simplified Chinese, Traditional Chinese
- Returns ready-to-use JSON for downstream analytics or visualization

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
  - id: clinic_attendance_node
    build: pip install -e .
    path: clinic_attendance_node
    inputs:
      language: input/language
    outputs:
      - attendance_data
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
  - id: language_source
    build: pip install your-lang-source
    path: your-lang-source
    outputs:
      - language

  - id: clinic_attendance_node
    build: pip install -e .
    path: clinic_attendance_node
    inputs:
      language: language_source/language
    outputs:
      - attendance_data
```

Your point source must output:

* Topic: `language`
* Data: String, either 'english', 'simplified-chinese', or 'traditional-chinese'
* Metadata:

  ```json
  {
    "type": "string",
    "description": "Language for which to fetch Chinese Medicine Clinic attendance data. Supported: english, simplified-chinese, traditional-chinese."
  }
  ```

## API Reference

### Input Topics

| Topic    | Type   | Description                                                                              |
| -------- | ------ | ----------------------------------------------------------------------------------------|
| language | string | Language for data (supported: 'english', 'simplified-chinese', 'traditional-chinese')   |

### Output Topics

| Topic           | Type            | Description                              |
| --------------- | --------------- | ---------------------------------------- |
| attendance_data | JSON/dict/list  | Fetched attendance data or error message |

## License

Released under the MIT License.
