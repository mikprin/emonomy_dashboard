

# Deploy with docker compose
How to deploy with docker compose:
```bash
mkdir -p grafana-storage grafana-volume
Userid=${UID} Groupid=${GID} docker-compose up -d
```
or in deploy script:
`./deploy.sh`

## Dependencies

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)


## Configuration

* [grafana](https://grafana.com/docs/grafana/latest/installation/configuration/)

# How to add data to database:

Use `test_tools/create_example_data.py` to push artifitial data to database.