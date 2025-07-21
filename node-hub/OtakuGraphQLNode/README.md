# otaku_graphql_node

A Dora-rs node for running arbitrary GraphQL queries against the https://api.fussy.fun/graphql endpoint. The node receives GraphQL queries and variables via Dora messaging, executes the request, and returns responses or error info. Ideal for integrating external anime/manga databases or similar GraphQL APIs in agent data flows.

## Features
- Accepts user-provided GraphQL queries and variables at runtime
- Forwards queries to the Fussy GraphQL API and collects responses
- Handles query/results and all error cases (JSON/HTTP parsing, API errors)

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
  - id: otaku_graphql
    build: pip install -e otaku_graphql_node
    path: otaku_graphql_node
    inputs:
      user_input: input/user_input  # any data to trigger query
      graphql_query: input/graphql_query
      variables: input/variables
    outputs:
      - graphql_response
      - graphql_error
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
  - id: your_input
    build: pip install your_input_node
    path: your_input_node
    outputs:
      - user_input
      - graphql_query
      - variables
  - id: otaku_graphql
    build: pip install -e otaku_graphql_node
    path: otaku_graphql_node
    inputs:
      user_input: your_input/user_input
      graphql_query: your_input/graphql_query
      variables: your_input/variables
    outputs:
      - graphql_response
      - graphql_error
```

Your point source must output:

* Topic: `graphql_query`
* Data: GraphQL query string
* Metadata:

  ```json
  {
    "type": "string",
    "desc": "GraphQL query string, e.g. '{ Media(id:1) { title { romaji } } }'"
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                      |
|-----------------|--------|----------------------------------|
| user_input      | any    | Any value, serves as query trigger|
| graphql_query   | string | GraphQL query as a string         |
| variables       | string | JSON-formatted variables or '{}'  |

### Output Topics

| Topic             | Type          | Description                        |
|-------------------|---------------|------------------------------------|
| graphql_response  | dict (JSON)   | Query result as decoded JSON       |
| graphql_error     | string        | Error string from query or parsing |


## License

Released under the MIT License.
