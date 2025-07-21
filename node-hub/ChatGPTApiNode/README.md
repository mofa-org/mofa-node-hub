# chatgpt_api_node

A Dora-rs node for real-time inference with OpenAI's GPT-4 via the APItools proxy. Translates string input to ChatGPT-4 completion output on demand using HTTP. Suitable for chatbot integration, prompt pipelines, and conversational system back-ends.

## Features
- Stateless relay to the OpenAI ChatGPT-4 API (no local model needed)
- Simple string input/output interface (JSON-ready)
- Handles errors robustly with descriptive response

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
  - id: chatgpt-api
    build: pip install -e chatgpt_api_node
    path: chatgpt_api_node
    inputs:
      user_input: input/user_input
    outputs:
      - chatgpt4_response
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
  - id: user_prompt
    build: pip install your-input-node
    path: your_input_node
    outputs:
      - user_input

  - id: chatgpt-api
    build: pip install -e chatgpt_api_node
    path: chatgpt_api_node
    inputs:
      user_input: user_prompt/user_input
    outputs:
      - chatgpt4_response

  - id: result_display
    build: pip install your-display-node
    path: your_display_node
    inputs:
      chatgpt4_response: chatgpt-api/chatgpt4_response
```

Your point source must output:

* Topic: `user_input`
* Data: String (prompt for GPT-4)
* Metadata:

  ```json
  {
    "dtype": "str",
    "description": "Prompt or message to send to ChatGPT-4"
  }
  ```

## API Reference

### Input Topics

| Topic       | Type | Description                      |
| ----------- | ---- | -------------------------------- |
| user_input  | str  | Prompt or input string for GPT-4 |

### Output Topics

| Topic             | Type         | Description                             |
| ----------------- | ------------ | --------------------------------------- |
| chatgpt4_response | dict / str   | Model response (JSON or reply string), or error report |

## License

Released under the MIT License.
