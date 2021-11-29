# syntax=docker/dockerfile:1
FROM tiangolo/uvicorn-gunicorn:python3.8-slim

ENV HOME="/root"
WORKDIR /root

# install apt dependencies
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# install poetry
ARG PYPI_MIRROR
RUN if [ -n "$PYPI_MIRROR" ]; then pip config set global.index-url $PYPI_MIRROR; fi
RUN --mount=type=cache,target=/root/.cache pip install poetry

# create virtualenv
ENV VIRTUAL_ENV=/root/.venv
RUN python3 -m virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# install dependencies
COPY pyproject.toml poetry.lock README.md /root/
COPY brick_server/minimal/__init__.py /root/brick_server/minimal/
COPY brick_server/playground/__init__.py  /root/brick_server/playground/
RUN --mount=type=cache,target=/root/.cache poetry install --no-dev
COPY . /root
RUN --mount=type=cache,target=/root/.cache poetry install --no-dev

EXPOSE $PORT

CMD python3 -m brick_server.playground
