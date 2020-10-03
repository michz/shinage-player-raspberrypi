#!/bin/bash -e

# Disable swapping
on_chroot <<EOF
sudo dphys-swapfile swapoff
sudo systemctl disable dphys-swapfile
sudo DEBIAN_FRONTEND=noninteractive apt-get -y purge dphys-swapfile
EOF

# Disable syslog writing
install -m 644 files/rsyslog.conf "${ROOTFS_DIR}/etc"
