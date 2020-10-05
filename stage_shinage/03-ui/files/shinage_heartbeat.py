#!/usr/bin/env python3

import json
import os
import requests
import subprocess
import sys

def command_noop(arguments):
    print("NOOP")

def command_restart_browser(arguments):
    os.system("/usr/bin/killall /usr/lib/chromium-browser/chromium-browser-v7")

def command_reboot(arguments):
    os.system("/usr/sbin/reboot")

def command_upgrade_remote_control(arguments):
    scriptPath = os.path.realpath(__file__)
    if 'url' in arguments:
        # Backup
        os.system(f"cp '{scriptPath}' /tmp/remote_script_backup.py")
        # Download new script to tmpdir and copy it to actual correct path
        os.system(f"wget --quiet '{arguments['url']}' -O /tmp/remote_script.py && mv /tmp/remote_script.py '{scriptPath}' && chmod +x '{scriptPath}'")
        # Now do the self-test
        p = subprocess.Popen(['/usr/bin/python3', scriptPath, "--self-test"], stdout=subprocess.PIPE)
        output = p.stdout.readline()
        if output == b'SHINAGE_OK\n':
            print("Script successfully updated.")
        else:
            print("Self-test after upgrade failed. Rolling back...")
            os.system(f"cp /tmp/remote_script_backup.py '{scriptPath}'")
    else:
        print('Argument `url` to fetch script from is missing.')


def map_and_execute_command(command, arguments):
    func = getattr(sys.modules[__name__], "command_%s" % command)
    func(arguments)



# Test run?
testRun = os.getenv('SHINAGE_REMOTE_TEST_RUN', None)
if len(sys.argv) > 1 and sys.argv[1] == '--self-test':
    print('SHINAGE_OK')
    exit(0)

# Version?
testRun = os.getenv('SHINAGE_REMOTE_TEST_RUN', None)
if len(sys.argv) > 1 and sys.argv[1] == '--version':
    print('1.0')
    exit(0)


baseUrl = os.getenv('SHINAGE_SERVER_BASE_URL', None)
if baseUrl == None:
    print('SHINAGE_SERVER_BASE_URL is not set. Cancel.')
    exit(1)

uuid = os.getenv('SHINAGE_SCREEN_UUID', None)
if uuid == None:
    print('SHINAGE_SCREEN_UUID is not set. Cancel.')
    exit(1)

r = requests.get(f"{baseUrl}/screen-remote/heartbeat/{uuid}", verify=False)

if r.status_code == 200:
    # command was returned, try to parse
    parsed = json.loads(r.text)
    if 'command' in parsed:
        map_and_execute_command(parsed["command"]["command"], parsed["command"]["arguments"])
    else:
        print("'command' field missing in response. Using the wrong api?")
        exit(2)
