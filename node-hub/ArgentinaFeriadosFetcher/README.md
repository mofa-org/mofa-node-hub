# argentina_feriados

Fetch Argentina's Public Holidays (Feriados) via Dora-compatible Node

## Features
- Retrieves the full list of official Argentina feriados (public holidays) for the current year
- Compatible with Dora-rs and MofaAgent node pipelines
- Simple integration with downstream ML/data workflows

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
  - id: feriados_fetcher
    build: pip install -e argentina_feriados
    path: argentina_feriados
    outputs:
      - feriados_output
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
  - id: feriados_fetcher
    build: pip install -e argentina_feriados
    path: argentina_feriados
    outputs:
      - feriados_output
  - id: downstream_node
    build: pip install your-processing-node
    path: your_processing_node
    inputs:
      feriados: feriados_fetcher/feriados_output
```

Your point source must output:

* Topic: `feriados_output`
* Data: List of public holidays as JSON/dict structure
* Metadata:

  ```json
  {
    "source": "https://api.argentinadatos.com/v1/feriados/",
    "country": "Argentina",
    "format": "list/dict of feriados"
  }
  ```

## API Reference

### Input Topics

| Topic        | Type    | Description                                              |
| ------------| ------- | ------------------------------------------------------- |
| user_input   | any     | (Optional) For compatibility; not used in logic flow    |

### Output Topics

| Topic            | Type           | Description                                        |
| ----------------| -------------- | -------------------------------------------------- |
| feriados_output  | dict/list      | List of Argentina public holidays or error message  |


## License

Released under the MIT License.
