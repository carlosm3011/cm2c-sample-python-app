#!/bin/bash
# Python wrapper, (c) carlos@xt6.us, 20151201

PYTHON="/usr/bin/python"
export SRCHOME=$(pwd)

####
export PYTHONPATH="$SRCHOME/lib:$SRCHOME/lib/cm2c:$SRCHOME/bin:$PYTHONPATH"

$PYTHON $*
