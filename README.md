

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