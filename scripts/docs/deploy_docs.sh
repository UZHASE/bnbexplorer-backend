#!/usr/bin/env bash

bash ./scripts/docs/generate_docs.sh

echo "Cloning docs repository"
cd /bnbexplorer-backend/docs
git clone https://github.com/UZHASE/UZHASE.github.io.git docs_repo
cd docs_repo
git config user.email "apidoc@bnbexplorer.email"
git config user.name "APIDOC"

echo "Done"

echo "Deploying docs..."
cp ../_build/html/* . -rf
git add .
git commit -m"Updated docs"
git push origin master
cd ..
rm docs_repo -rf
