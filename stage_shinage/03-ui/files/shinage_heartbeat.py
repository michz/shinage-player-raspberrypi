#!/usr/bin/env python3

import json
import os
import requests

def command_noop():
    print("NOOP")

def command_restart_browser():
    os.system("/usr/bin/killall /usr/lib/chromium-browser/chromium-browser-v7")

def command_reboot():
    os.system("/usr/sbin/reboot")

def map_and_execute_command(argument):
    commands = {
        'noop': command_noop,
        'restart_browser': command_restart_browser,
        'reboot': command_reboot,
    }
    func = commands.get(argument, lambda: print("Invalid command given."))
    func()


baseUrl = os.getenv('SHINAGE_SERVER_BASE_URL', None)
if baseUrl == None:
    print('SHINAGE_SERVER_BASE_URL is not set. Cancel.')
    exit(1)

uuid = os.getenv('SHINAGE_SCREEN_UUID', None)
if uuid == None:
    print('SHINAGE_SCREEN_UUID is not set. Cancel.')
    exit(1)

r = requests.get(f"{baseUrl}/screen-remote/heartbeat/{uuid}")

if r.status_code == 200:
    # command was returned, try to parse
    parsed = json.loads(r.text)
    if 'command' in parsed:
        map_and_execute_command(parsed["command"]["command"])
    else:
        print("'command' field missing in response. Using the wrong api?")
        exit(2)
