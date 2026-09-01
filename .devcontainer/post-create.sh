#!/usr/bin/env bash

set -euo pipefail

sudo mkdir -p /home/vscode/.cache /home/vscode/.local/share/quarto/logs
sudo chown -R vscode:vscode /home/vscode/.cache /home/vscode/.local
chmod -R u+rwX /home/vscode/.cache /home/vscode/.local

VENV_DIR="/workspaces/uab_ami/.venv"

if [[ ! -d "${VENV_DIR}" ]]; then
  python3 -m venv "${VENV_DIR}"
fi

"${VENV_DIR}/bin/python" -m pip install --upgrade pip
"${VENV_DIR}/bin/pip" install -r /workspaces/uab_ami/requirements.txt
"${VENV_DIR}/bin/pip" install jupyter numpy

quarto --version
"${VENV_DIR}/bin/python" --version
"${VENV_DIR}/bin/jupyter" --version