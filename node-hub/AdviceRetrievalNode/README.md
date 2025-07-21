# advice_retriever

Fetch advice from a public API (https://kk-advice.koyeb.app/api) as a Dora-rs node. Supports retrieving either all available advice as a list or a single random advice string, configurable via input parameter.

## Features
- Fetch all available advice entries from the API
- Retrieve a random piece of advice
- Robust error handling with retry logic

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
  - id: advice_retriever
    build: pip install -e .
    path: advice_retriever
    inputs:
      mode: input/mode
    outputs:
      - all_advice
      - random_advice
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
  - id: custom_controller
    build: pip install your-custom-controller
    path: your_custom_controller
    outputs:
      - mode     # Outputs: 'all' or 'random'

  - id: advice_retriever
    build: pip install -e .
    path: advice_retriever
    inputs:
      mode: custom_controller/mode
    outputs:
      - all_advice
      - random_advice
```

Your point source must output:

* Topic: `mode`
* Data: String indicating either 'all' or 'random'
* Metadata:

  ```json
  {
    "required": true,
    "type": "string",
    "description": "Request mode for advice retrieval ('all' or 'random')"
  }
  ```

## API Reference

### Input Topics

| Topic | Type   | Description                          |
|-------|--------|--------------------------------------|
| mode  | string | Request mode: 'all' or 'random'      |

### Output Topics

| Topic         | Type             | Description                                        |
|-------------- |------------------|----------------------------------------------------|
| all_advice    | list of objects  | List of all available advice entries (if mode=all) |
| random_advice | object or string | A random advice entry (if mode=random)             |

## License

Released under the MIT License.
