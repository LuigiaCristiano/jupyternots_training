#!/bin/bash
# Install curl
conda update -n base conda
conda install curl
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -
poetry install --no-dev
poetry shell
python -m ipykernel install --user --name=rdm-training

# jupyter kernelspec remove testenv
