#!/bin/bash
# Install curl
conda install curl
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -
poetry install --no-dev
poetry shell
python -m ipykernel install --user --name=rdm-training
exit 0

# jupyter kernelspec remove testenv
