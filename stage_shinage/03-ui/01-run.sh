#!/bin/bash -e

install -m 644 files/hdparm.conf            "${ROOTFS_DIR}/etc"
install -m 755 files/run-browser.sh         "${ROOTFS_DIR}/usr/local/bin"
install -m 755 files/shinage_heartbeat.py   "${ROOTFS_DIR}/usr/local/sbin"
install -m 644 files/shinage_heartbeat_cron "${ROOTFS_DIR}/etc/cron.d"
