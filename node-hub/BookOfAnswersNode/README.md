# book_of_answers_node

A Dora-rs node that delivers wisdom from the online Book of Answers API. When triggered, it fetches and outputs a cryptic response, making it easy to integrate with conversational or interactive pipelines.

## Features
- Integrates with the Book of Answers online API to get random advice
- Minimal dependencies and stateless operation
- Seamless Dora-rs MofaAgent compatibility

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
  - id: book_of_answers
    build: pip install -e .
    path: book_of_answers_node
    inputs:
      user_input: input/user_input
    outputs:
      - book_of_answers_response
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
  - id: my_input
    build: pip install my-input-node
    path: my-input-node
    outputs:
      - user_input

  - id: book_of_answers
    build: pip install -e .
    path: book_of_answers_node
    inputs:
      user_input: my_input/user_input
    outputs:
      - book_of_answers_response
```

Your point source must output:

* Topic: `user_input`
* Data: Any (acts as trigger; can be string or dummy value)
* Metadata:

  ```json
  {
    "description": "Acts as a trigger or user message for BookOfAnswers call. Contents are ignored; any type is accepted."
  }
  ```

## API Reference

### Input Topics

| Topic       | Type   | Description                                     |
| ----------- | ------ | ----------------------------------------------- |
| user_input  | Any    | Trigger signal; required for dataflow integrity |

### Output Topics

| Topic                    | Type   | Description                       |
| ------------------------ | ------ | --------------------------------- |
| book_of_answers_response | String | Response from Book of Answers API |


## License

Released under the MIT License.

````