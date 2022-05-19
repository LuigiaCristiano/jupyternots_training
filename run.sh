#!/bin/bash
pip install poetry
poetry install --no-dev
poetry run ipython kernel install --user --name=rdm-training

