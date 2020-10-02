#!/usr/bin/env bash

set -o allexport; source /boot/shinage.conf; set +o allexport

URL=$(printf $SHINAGE_PLAYER_FULL_URL_FORMAT $SHINAGE_SCREEN_UUID)

if [ -z "$SHINAGE_CHROMIUMPARAMETERS" ]; then
    SHINAGE_CHROMIUMPARAMETERS=""
fi

sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium/Default/Preferences

unclutter &

xset s off
xset -dpms
xset s noblank

/usr/bin/chromium-browser --noerrdialogs --incognito --disable-translate \
    --disable-translate-new-ux --disk-cache-size=0 \
    --no-first-run --force-device-scale-factor=1 \
    --user-data-dir=/tmp/chromium/ --disk-cache-dir=/tmp/chromium/ \
    --disk-cache-size=$((1024 * 1024)) --disable-java --disable-plugins $SHINAGE_CHROMIUMPARAMETERS \
    --kiosk $URL
