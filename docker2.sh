#!/bin/sh

docker run \
    --network=host \
    -p 9090:9090 \
    -v ./prometheus.yml:/etc/prometheus/prometheus.yml:Z \
    prom/prometheus
