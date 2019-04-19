#!/usr/bin/env bash

NOTEBOOKS_PATH=notebooks/*.ipynb

execute_notebooks () {
  DATASET_FOLDER='datasets/fixtures/' pipenv run jupyter nbconvert --execute --to notebook $NOTEBOOKS_PATH --stdout > /dev/null
}

announce_success () {
  GREEN='\033[0;32m'
  NO_COLOR='\033[0m'
  echo "\n\n${GREEN} All notebooks executed successfully${NO_COLOR}\n\n"
}

execute_notebooks && announce_success
