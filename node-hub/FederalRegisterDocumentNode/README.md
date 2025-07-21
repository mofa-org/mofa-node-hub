# federal_register_node

Access the Federal Register API to fetch U.S. government documents by document_id or list all recent documents. Provides convenient integration for Dora-rs pipelines.

## Features
- Retrieve a single Federal Register document by ID
- List all available Federal Register documents
- Simple integration as a Dora-rs node

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
  - id: federalregister
    build: pip install -e .
    path: federal_register_node
    inputs:
      parameters: input/parameters
    outputs:
      - single_document
      - all_documents
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
  - id: my_input_node
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - parameters

  - id: federalregister
    build: pip install -e .
    path: federal_register_node
    inputs:
      parameters: my_input_node/parameters
    outputs:
      - single_document
      - all_documents
```

Your point source must output:

* Topic: `parameters`
* Data: Dictionary with one or both of the following keys: `document_id`, `publication_date` (both as strings, `publication_date` optional)
* Metadata:

  ```json
  {
    "fields": ["document_id", "publication_date"],
    "types": ["string", "string"]
  }
  ```

## API Reference

### Input Topics

| Topic            | Type                              | Description                                   |
| ---------------- | --------------------------------- | --------------------------------------------- |
| parameters       | dict (document_id + publication_date) | Input document query parameters (see below)   |

### Output Topics

| Topic            | Type   | Description                                                        |
| ---------------- | ------ | ------------------------------------------------------------------ |
| single_document  | dict   | The matching Federal Register document (if document_id is given)    |
| all_documents    | dict   | All available Federal Register documents (if document_id omitted)   |
| error            | dict   | Error message if request or processing fails                       |


## License

Released under the MIT License.
