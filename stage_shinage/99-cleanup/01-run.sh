#!/bin/bash -e

on_chroot <<EOF
sudo DEBIAN_FRONTEND=noninteractive apt-get -y autoremove
EOF
