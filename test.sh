#!/bin/bash
docker-compose build
docker-compose -f docker-compose-test.yml run --rm parser