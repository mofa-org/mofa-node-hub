# url_unshortener

Unshorten URLs in your pipeline using the Unshorten.me API.

## Features
- Automatic URL unshortening with Unshorten.me
- Supports authenticated or anonymous API use via .env file
- Simple Dora node interface with clear input/output

## Getting Started

### Installation
Install via cargo:
```bash
pip install -e .
````

## Basic Usage

Create a YAML config (e.g., `demo.yml`):

```yaml
nodes:
  - id: url_unshortener
    build: pip install -e .
    path: url_unshortener
    inputs:
      shortened_url: input/shortened_url
    outputs:
      - unshortened_result
    env:
      UNSHORTEN_AUTH_HEADER: "Bearer <your_api_token_if_needed>"
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
  - id: my_url_feeder
    build: pip install -e my_url_feeder
    path: my_url_feeder
    outputs:
      - shortened_url

  - id: url_unshortener
    build: pip install -e .
    path: url_unshortener
    inputs:
      shortened_url: my_url_feeder/shortened_url
    outputs:
      - unshortened_result
    env:
      UNSHORTEN_AUTH_HEADER: "Bearer <your_api_token_if_needed>"
```

Your point source must output:

* Topic: `shortened_url`
* Data: Shortened URL as string
* Metadata:

  ```json
  {
    "dtype": "str"
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                  |
|-----------------|--------|------------------------------|
| shortened_url   | str    | Shortened URL to unshorten   |

### Output Topics

| Topic               | Type | Description                   |
|---------------------|------|-------------------------------|
| unshortened_result  | dict | Response from Unshorten.me API |


## License

Released under the MIT License.
