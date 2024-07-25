#!/bin/bash

set -e
cd "${0%/*}" || exit 1;   # Go to the script location

if test ! -f popcorn.sif
then
    echo "Compiling popcorn."
    cd src
    apptainer build ../popcorn.sif Singularity
else
    echo "popcorn already compiled."
fi
