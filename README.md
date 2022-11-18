

# Deploy with docker compose

```bash
mkdir -p grafana-storage grafana-volume
Userid=${UID} Groupid=${GID} docker-compose up -d
```

or in deploy script:
`./deploy.sh`