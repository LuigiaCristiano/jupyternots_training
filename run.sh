#!/bin/bash
# Install curl
#conda update -n base conda
conda install curl
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/jovyan/.local/bin:$PATH"
poetry install --no-dev
poetry run ipython kernel install --user --name=rdm-training
