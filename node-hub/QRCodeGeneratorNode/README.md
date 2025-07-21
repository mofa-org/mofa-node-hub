# qr_code_node

A Dora-rs node for QR code generation using an external API. This node takes input parameters to generate a QR code image and outputs the result as a base64-encoded PNG.

## Features
- Generate QR codes from data and size parameters
- Automatically retries request to handle transient API failures
- Returns QR image as base64 string for serialization

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
  - id: qr_code_node
    build: pip install -e ./qr_code_node
    path: qr_code_node
    inputs:
      data: input/data
      size: input/size
    outputs:
      - qr_code_result
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
  - id: input
    build: pip install your-input-node
    path: your-input-node
    outputs:
      - data
      - size

  - id: qr_code_node
    build: pip install -e ./qr_code_node
    path: qr_code_node
    inputs:
      data: input/data
      size: input/size
    outputs:
      - qr_code_result
```

Your point source must output:

* Topic: `data` and `size`
* Data: String input for data to encode and size (pixels, as integer in string form)
* Metadata:

  ```json
  {
    "data": "String (data to encode in QR)",
    "size": "String (integer value for image size in px)"
  }
  ```

## API Reference

### Input Topics

| Topic  | Type   | Description             |
|--------|--------|-------------------------|
| data   | String | Data to encode in QR    |
| size   | String | Output image size (px)  |

### Output Topics

| Topic           | Type   | Description                                              |
|-----------------|--------|----------------------------------------------------------|
| qr_code_result  | Object | Contains `qr_code_base64` (base64 PNG), `content_type`, or error |


## License

Released under the MIT License.
