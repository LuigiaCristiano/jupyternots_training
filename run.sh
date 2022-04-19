#!/bin/bash
# Install curl
conda install curl
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -
poetry shell
python -m ipykernel install --user --name=rdm-training
exit

# jupyter kernelspec remove testenv
