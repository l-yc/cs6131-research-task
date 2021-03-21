#!/bin/sh

docker run \
    -p 9090:9090 \
    -v ./config:/etc/prometheus \
    prom/prometheus
