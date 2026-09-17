#!/usr/bin/env bash

set -euo pipefail

echo "=== AMI Quarto: post-create setup ==="

# ------------------------------------------------------------
# User directories
# ------------------------------------------------------------

mkdir -p \
    "${HOME}/.cache" \
    "${HOME}/.local/share/quarto/logs"

# ------------------------------------------------------------
# Project Python virtual environment
# ------------------------------------------------------------

VENV_DIR="/workspaces/uab_ami/.venv"

if [[ ! -d "${VENV_DIR}" ]]; then
    echo "Creating Python virtual environment..."
    python3 -m venv "${VENV_DIR}"
fi

# ------------------------------------------------------------
# Python dependencies
# ------------------------------------------------------------

echo "Installing Python dependencies..."

"${VENV_DIR}/bin/python" -m pip install \
    -r /workspaces/uab_ami/requirements.txt

# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------

echo
echo "=== Versions ==="

echo "Quarto:"
quarto --version

echo
echo "Python:"
"${VENV_DIR}/bin/python" --version

echo
echo "Jupyter:"
"${VENV_DIR}/bin/jupyter" --version

echo
echo "User:"
id

echo
echo "Home:"
ls -ld "${HOME}"

echo
echo "Quarto logs:"
ls -ld "${HOME}/.local/share/quarto/logs"

echo
echo "=== Setup complete ==="