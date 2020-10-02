#!/usr/bin/env bash

set -e

# Preparations
rm -f ./pi-gen/stage2/EXPORT_*
touch ./stage_shinage/EXPORT_IMAGE

cd ./pi-gen

# Copy stage_shinage to build directory
rm -rf ./stage_shinage
cp -r ../stage_shinage ./stage_shinage

# Patch: Use i386 because of https://github.com/RPi-Distro/pi-gen/issues/271
sed -i -E "s#^FROM.*#FROM i386/debian:buster#g" ./Dockerfile

#CLEAN=1 ./build.sh -c ../config
CLEAN=1 ./build-docker.sh -c ../config

cd ..
