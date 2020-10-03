#!/bin/bash -e

install -m 644 files/99-small-footprint.conf "${ROOTFS_DIR}/etc/apt/apt.conf.d"
