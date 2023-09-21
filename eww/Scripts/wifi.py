#!/usr/bin/python

import subprocess

icons = ["󰤨  Online", "󰤭  Offline"]
hostname = "gnu.org"  # Change this to "gnu.org" or any other host you want to ping

# Check network connectivity using ping
try:
    subprocess.check_output(["ping", "-c", "1", hostname])
    print(icons[0])  # Network is reachable
except subprocess.CalledProcessError:
    print(icons[1])  # Network is unreachable
