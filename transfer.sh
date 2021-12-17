#!/bin/bash

rm -r server
mv tmp server
cd server
chmod +x install.sh
./install.sh