#!/usr/bin/env bash

set -x
set -e

TASK=$1
WORKERS=$2
# if [[ $# -ge 1 ]]; then
#     TASK=$1
#     shift
# fi


python3 -u codes/preprocess.py \
--task "${TASK}" \
--train-path "../data/${TASK}/train.txt" \
--valid-path "../data/${TASK}/valid.txt" \
--test-path "../data/${TASK}/test.txt" \
--workers "${WORKERS}"