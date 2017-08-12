#!/bin/bash

export SURVEY_FILE=$1
export RESPONSE_FILE=$2

docker-compose run --rm parser