#!/bin/bash
pylint $(find -type f -name "*.py" ! -path "**/venv/**" ! -path "**/__pycache__/**")