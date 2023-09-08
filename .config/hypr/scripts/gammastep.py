import os
import subprocess

# Define the file name
file_name = "exists.txt"
#should exist at pc startup and only when gamma is off
# Check if the file exists
if os.path.exists(file_name):
    # Execute gammastep command in the background
    subprocess.Popen(["gammastep", "-l", "0:0", "-t", "3500:3500", "&"])
    os.system("notify-send 'Info' 'Night light is being activated..'")
    # Delete the file
    os.remove(file_name)
else:
    # Kill gammastep process
    subprocess.run(["pkill", "gammastep"])
    os.system("notify-send 'Info' 'Night Light Off'")
    
    # Create the file
    open(file_name, 'a').close()
