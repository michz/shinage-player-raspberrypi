#!/bin/bash -e

install -m 644 files/hdparm.conf        "${ROOTFS_DIR}/etc/"
install -m 755 files/run-browser.sh     "${ROOTFS_DIR}/usr/local/bin/"
