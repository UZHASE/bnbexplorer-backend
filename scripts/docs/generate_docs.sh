#!/usr/bin/env bash

echo "Sphinx - generating auto doc"
cd /bnbexplorer-backend/docs
sphinx-apidoc -o . ../ -f # Generate apidoc with output in current folder. Root folder ../
make html
echo "Done"


