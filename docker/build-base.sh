#!/usr/bin/env bash


set -o errexit
set -o pipefail
set -o nounset

base_image=lappis/botrequirements:boilerplate

# Build base image
docker build . -f docker/requirements.Dockerfile -t $base_image

# Check if user wants to publish
if [ $# -eq 1 ]; then
    if [ "$1" = "publish" ]; then
        echo; echo; echo "PUBLISHING IMAGES"
        docker push $base_image;
    fi
else
    echo "Execute 'sh build.sh publish' to publish images"
fi
