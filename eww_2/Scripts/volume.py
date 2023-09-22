#!/usr/bin/python

import subprocess
import re

# Run the amixer command to get the current volume information
try:
    output = subprocess.check_output(["amixer", "get", "Master"]).decode("utf-8")
except subprocess.CalledProcessError:
    print("Error: Unable to retrieve volume information")
    exit(1)

# Use regular expressions to extract the volume percentage
volume_pattern = r'(\d+)%'
matches = re.search(volume_pattern, output)

if matches:
    volume = matches.group(1)
    print(f"󰕾 {volume}%")
else:
    print("Volume information not found")