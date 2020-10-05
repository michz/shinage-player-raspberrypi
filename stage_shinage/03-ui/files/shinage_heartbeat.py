#!/usr/bin/env python3

import json
import os
import requests

def command_noop(arguments):
    print("NOOP")

def command_restart_browser(arguments):
    os.system("/usr/bin/killall /usr/lib/chromium-browser/chromium-browser-v7")

def command_reboot(arguments):
    os.system("/usr/sbin/reboot")

def map_and_execute_command(command, arguments):
    commands = {
        'noop': command_noop,
        'restart_browser': command_restart_browser,
        'reboot': command_reboot,
    }
    func = commands.get(command, lambda: print("Invalid command given."))
    func(arguments)


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
        map_and_execute_command(parsed["command"]["command"], parsed["command"]["arguments"])
    else:
        print("'command' field missing in response. Using the wrong api?")
        exit(2)
