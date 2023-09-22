#!/usr/bin/python

import subprocess

icons = ["󰤨  Online", "󰤭  Offline"]

# Check network connectivity using nmcli
try:
    subprocess.check_output(["nmcli", "networking", "connectivity", "check"])
    print(icons[0])  # Network is reachable
except subprocess.CalledProcessError:
    print(icons[1])  # Network is unreachable
