# yugioh_limit_regulation

Fetch real-time Yu-Gi-Oh! Forbidden & Limited Lists across all major formats via an easy Dora/Mofa agent node.

## Features
- Retrieves the current Forbidden & Limited Lists for various Yu-Gi-Oh! formats (TCG, OCG, Rush, Master Duel, and more)
- Handles region selection dynamically through input messaging
- Returns results or error info in JSON format for downstream processing

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
  - id: yugioh-limit
    build: pip install -e yugioh_limit_regulation
    path: yugioh_limit_regulation
    inputs:
      region: input/region  # string: 'tcg', 'rush', 'ocg', 'ocg_ae', 'master_duel', or 'ocg_cn'
    outputs:
      - forbidden_list
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
  - id: region-provider
    build: pip install your-region-node
    path: your-region-path
    outputs:
      - region

  - id: yugioh-limit
    build: pip install -e yugioh_limit_regulation
    path: yugioh_limit_regulation
    inputs:
      region: region-provider/region
    outputs:
      - forbidden_list
```

Your point source must output:

* Topic: `region`
* Data: String (e.g., "tcg", "ocg", etc.)
* Metadata:

  ```json
  {
    "type": "string",
    "allowed": ["tcg", "rush", "ocg", "ocg_ae", "master_duel", "ocg_cn"]
  }
  ```

## API Reference

### Input Topics

| Topic   | Type   | Description                              |
| ------- | ------ | ---------------------------------------- |
| region  | string | Region specifier for list (tcg, ocg, etc) |

### Output Topics

| Topic          | Type  | Description                                 |
| -------------- | ----- | ------------------------------------------- |
| forbidden_list | json  | Yu-Gi-Oh! list for the given region or error |


## License

Released under the MIT License.
