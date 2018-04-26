#!/usr/bin/env bash

docker exec -i alted_postgres_1 dropdb -h postgres -U alted postgres
docker exec -i alted_postgres_1 createdb -h postgres -U alted postgres -O postgres
