#!/usr/bin/env bash
mkdir -p grafana-storage grafana-volume
Userid=${UID} Groupid=${GID} docker-compose up -d