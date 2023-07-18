#!/bin/bash -e

# **ATTENTION** This is also hardcoded in getty@tty1.service
KIOSK_USER_NAME="kiosk"

on_chroot <<EOF
adduser --disabled-password --gecos "" ${KIOSK_USER_NAME}

for GRP in audio video input tty; do
  adduser $KIOSK_USER_NAME \$GRP
done
EOF

install -m 755 files/.profile           "${ROOTFS_DIR}/home/${KIOSK_USER_NAME}/"
install -m 755 files/.xsession          "${ROOTFS_DIR}/home/${KIOSK_USER_NAME}/"

# Autologin
install -m 755 -d="${ROOTFS_DIR}/etc/systemd/system/getty@tty1.service.d"
install -m 644 files/getty-override.conf "${ROOTFS_DIR}/etc/systemd/system/getty@tty1.service.d/override.conf"

on_chroot <<EOF
# Enable automatic login shell
systemctl daemon-reload
systemctl enable getty@tty1.service

# No root login by ssh
sed -i -E "s/^\s*#?\s*PermitRootLogin.*$/PermitRootLogin no/g" /etc/ssh/sshd_config
EOF
