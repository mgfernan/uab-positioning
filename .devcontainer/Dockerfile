FROM ubuntu:24.04

ARG QUARTO_VERSION=1.10.18

# ------------------------------------------------------------
# System packages
# ------------------------------------------------------------
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        ca-certificates \
        curl \
        git \
        iproute2 \
        latexmk \
        pandoc \
        python3 \
        python3-dev \
        python3-full \
        python3-pip \
        python3-venv \
        sudo \
        wget \
        texlive-fonts-recommended \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-science \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# Quarto
# ------------------------------------------------------------
RUN wget -q \
        "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb" \
        -O /tmp/quarto.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends /tmp/quarto.deb \
    && rm -f /tmp/quarto.deb \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# Temporary directory
# ------------------------------------------------------------
RUN chmod 1777 /tmp

# ------------------------------------------------------------
# Workspace
# ------------------------------------------------------------
WORKDIR /workspaces/uab_ami

# Ubuntu 24.04 provides:
#   ubuntu:x:1000:1000
#
# This matches the host user and therefore allows the
# ubuntu user to write to the bind-mounted workspace.
USER ubuntu