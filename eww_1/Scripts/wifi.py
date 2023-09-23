#!/usr/bin/python

import subprocess

icons = ["󰤨  Online", "󰤭  Offline"]

# Check network connectivity using nmcli
try:
    check = subprocess.check_output(["nmcli", "networking", "connectivity", "check"]).decode("utf-8")
    if 'none' in check:
        print(icons[1])  # Network is reachable
    if 'full' in check: 
        print(icons[0])  # Netwrok is not reachable
except subprocess.CalledProcessError:
    print(icons[1])  # Network is unreachable
