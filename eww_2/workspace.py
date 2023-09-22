#!/usr/bin/python

import subprocess

# Define the special character for the active workspace
active_char = "󰄯"

# Define the character for inactive workspaces
inactive_char = "󰄰"

# Run the hyprctl command and capture its output
output = subprocess.check_output(["hyprctl", "activewindow"])

# Decode the output to a string
output_str = output.decode("utf-8")

# Split the output by lines and find the line containing "workspace: "
lines = output_str.split("\n")
active_workspace_line = next((line for line in lines if "workspace: " in line), None)

if active_workspace_line:
    # Extract the workspace number
    workspace_number = int(active_workspace_line.split(" ")[1])
    
    # Generate the representation of workspaces
    workspace_representation = [active_char if i == workspace_number - 1 else inactive_char for i in range(5)]
    
    # Print the workspace representation
    # print(" ".join(workspace_representation))
    print("hi")
else:
    # If "workspace: " was not found, print an error message
    print("Error: Unable to determine the active workspace")
