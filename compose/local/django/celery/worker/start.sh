    t#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

export C_FORCE_ROOT=true

celery -A alted.taskapp worker -l INFO
