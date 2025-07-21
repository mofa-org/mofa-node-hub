# ip_fraud_detector

IP Fraud Score Lookup Dora Node

## Features
- Looks up IP fraud probability using GetIPIntel API
- Accepts IP address as input parameter
- Returns fraud analysis result including risk score and details

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
  - id: ip_fraud_detector
    build: pip install -e .
    path: ip_fraud_detector
    inputs:
      user_input: input/user_input
      ip: input/ip
    outputs:
      - ip_fraud_score
    env:
      GETIPINTEL_CONTACT_EMAIL: "your-contact@email.com"
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
  - id: ip_source
    build: pip install your-node
    path: your-custom-ip-source
    outputs:
      - ip

  - id: ip_fraud_detector
    build: pip install -e .
    path: ip_fraud_detector
    inputs:
      ip: ip_source/ip
    outputs:
      - ip_fraud_score
    env:
      GETIPINTEL_CONTACT_EMAIL: "your-contact@email.com"
```

Your point source must output:

* Topic: `ip`
* Data: IP address as string
* Metadata:

  ```json
  {
    "type": "string",
    "description": "IPv4 or IPv6 address to be checked"
  }
  ```

## API Reference

### Input Topics

| Topic      | Type   | Description                        |
| ---------- | ------ | ---------------------------------- |
| user_input | Any    | Arbitrary user command or context   |
| ip         | String | The IP address to be checked       |

### Output Topics

| Topic          | Type   | Description                               |
| -------------- | ------ | ------------------------------------------|
| ip_fraud_score | JSON   | GetIPIntel risk result or error message   |


## License

Released under the MIT License.
