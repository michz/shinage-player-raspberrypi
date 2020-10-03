#!/bin/bash -e

install -m 755 files/shinage-uuid-generator.sh      "${ROOTFS_DIR}/usr/local/sbin"
install -m 644 files/shinage-uuid-generator.service "${ROOTFS_DIR}/etc/systemd/system"

on_chroot <<EOF
systemctl daemon-reload
systemctl enable shinage-uuid-generator.service
EOF
