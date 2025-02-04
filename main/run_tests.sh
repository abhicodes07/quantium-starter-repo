#!/bin/zsh

source .venv/bin/activate

python -m pytest quantium-starter-repo/main/test_app_callbacks.py

PYTEST_EXIT_CODE = $?

if [PYTEST_EXIT_CODE -eq 0]
then
  exit 0
else
  exit 1
fi
