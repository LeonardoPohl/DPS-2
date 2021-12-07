#!/bin/bash

set -e

cd server/benchmarks
python3 test.py
cd -
