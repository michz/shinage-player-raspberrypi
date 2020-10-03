#!/usr/bin/env bash

set -o allexport; source /boot/shinage.conf; set +o allexport

if [[ "$SHINAGE_SCREEN_UUID" == "00000000-0000-0000-0000-000000000000" ]]; then
    uuid=$(uuidgen -r)
    sed -i -E "s/SHINAGE_SCREEN_UUID=\"(.*)\"/SHINAGE_SCREEN_UUID=\"${uuid}\"/g" /boot/shinage.conf
fi
