#!/bin/bash

set -e

cd client && yarn && yarn build && cd -

cd server
python3 -m venv --copies .env
source .env/bin/activate
pip install -r requirements.txt
cd -
