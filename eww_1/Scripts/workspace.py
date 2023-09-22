#!/usr/bin/python

import subprocess
import argparse

# Define the special character for the active workspace
active_char = "󰄯"

# Define the character for inactive workspaces
inactive_char = "󰄰"

def generate_workspace_representation(num_workspaces, active_workspace):
    # Generate the representation of workspaces
    workspace_representation = [
        active_char if i == active_workspace - 1 else inactive_char
        for i in range(num_workspaces)
    ]
    return " ".join(workspace_representation)

def main():
    parser = argparse.ArgumentParser(description="Generate workspace representation")
    parser.add_argument(
        "active_workspace",
        type=int,
        choices=range(1, 10),
        help="The active workspace (1 to 9)",
    )
    args = parser.parse_args()

    # Run the hyprctl command and capture its output
    output = subprocess.check_output(["hyprctl", "activeworkspace"])

    # Decode the output to a string
    output_str = output.decode("utf-8")

    # Find the line containing "workspace ID"
    workspace_line = next(
        (line for line in output_str.split("\n") if "workspace ID" in line), None
    )

    if workspace_line:
        # Extract the workspace ID as a string between parentheses
        workspace_id_str = workspace_line.split("(")[1].split(")")[0]

        # Convert the workspace ID to an integer
        workspace_id = int(workspace_id_str)

        # Generate and print the workspace representation
        workspace_representation = generate_workspace_representation(
            args.active_workspace, workspace_id
        )
        print(workspace_representation)
    else:
        # If "workspace ID" was not found, print an error message
        print("Error: Unable to determine the active workspace")

if __name__ == "__main__":
    main()
