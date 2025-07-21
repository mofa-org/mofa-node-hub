# UnhcrResettlementNode

Access UNHCR Resettlement API endpoints as a Dora-rs node for easy data integration—fetch regions, categories, and paginated departure data via simple inputs.

## Features
- Fetch UNHCR regions via a dedicated API endpoint
- List available resettlement categories
- Retrieve paginated departures data with query support

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
  - id: unhcr
    build: pip install -e .
    path: unhcr_resettlement_node
    inputs:
      api_action: input/api_action
      user_input: input/user_input  # Optional
      page: input/page             # For departures
      year: input/year             # For departures
      origin: input/origin         # For departures
      asylum: input/asylum         # For departures
      resettlement: input/resettlement  # For departures
    outputs:
      - regions
      - categories
      - departures
      - error
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
  - id: my-query-driver
    build: pip install -e my-query-driver
    path: my_query_driver
    outputs:
      - api_action
      - page
      - year
      - origin
      - asylum
      - resettlement

  - id: unhcr
    build: pip install -e .
    path: unhcr_resettlement_node
    inputs:
      api_action: my-query-driver/api_action
      page: my-query-driver/page
      year: my-query-driver/year
      origin: my-query-driver/origin
      asylum: my-query-driver/asylum
      resettlement: my-query-driver/resettlement
    outputs:
      - regions
      - categories
      - departures
      - error
```

Your point source must output:

* Topic: `api_action` (with string values: "regions", "categories", or "departures")
* Data: String (indicates which API branch to query)
* Metadata:

  ```json
  {
    "type": "str"
  }
  ```

## API Reference

### Input Topics

| Topic           | Type   | Description                                                           |
| --------------- | ------ | --------------------------------------------------------------------- |
| api_action      | str    | Which UNHCR endpoint to fetch: "regions", "categories", or "departures" |
| user_input      | any    | Optional, not required; placeholder for general user controls           |
| page            | str    | (departures only) Page number for pagination                            |
| year            | str    | (departures only) Comma-separated years (e.g., "2016,2017")            |
| origin          | str    | (departures only) Comma-separated ISO country codes (origins)           |
| asylum          | str    | (departures only) Comma-separated ISO country codes (asylum countries)  |
| resettlement    | str    | (departures only) Comma-separated ISO country codes (destinations)      |

### Output Topics

| Topic       | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| regions     | dict   | Full JSON list of regions from UNHCR regions endpoint        |
| categories  | dict   | Full JSON list of categories from UNHCR categories endpoint  |
| departures  | dict   | Departures data (paginated, per provided params)             |
| error       | dict   | Error object if the node fails to contact UNHCR API          |


## License

Released under the MIT License.
