

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




## Database example

Connect to database with `psql`:
```bash
psql postgresql://postgres:newpassword@localhost:5432
```

Use also can use Beekeeper Studio to connect to database.


# Test tools

## Installation of sqlalchemy

Sometimes sqlalchemy having issues. What worked for me:
```bash
sudo apt install libpq-dev
sudo pip install psycopg2
sudo pip install sqlalchemy
```


## Artiicial data: 
Use `test_tools/create_example_data.py` to push artifitial data to database.

## Add example data to empty postgres database

There are 2 scripts that can help you with that. `push_data_to_postgres.ipynb` and `test_tools/push_data_to_postgres.py`. Fist one is used as an interactive demo and a second one can be used as external library for future use. Example data is located in `example_data/example_csv`. Make sure to change location when using script.