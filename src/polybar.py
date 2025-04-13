# src/polybar.py

import os
from src.utils import run_command, info
from src.dotfiles import clean_and_copy_dotfiles

def install_polybar():
    """
    Install Polybar using apt-get.
    """
    info("Installing Polybar...")

    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y polybar")

    info("Polybar installed successfully.")

def sync_polybar_config(project_dotfiles_dir, home_dir):
    """
    Copy Polybar configuration from dotfiles to home directory.
    Also create launch_polybar.sh script.
    """
    src_polybar_config = os.path.join(project_dotfiles_dir, 'polybar')
    dst_polybar_config = os.path.join(home_dir, '.config', 'polybar')

    if os.path.exists(src_polybar_config):
        info("Syncing Polybar configuration...")

        # Copy the config
        clean_and_copy_dotfiles(src_polybar_config, dst_polybar_config)
    else:
        info("No Polybar configuration found in dotfiles. Skipping config sync.")

    # Make sure the destination directory exists
    os.makedirs(dst_polybar_config, exist_ok=True)

    # Create the launch_polybar.sh script
    launch_script_path = os.path.join(dst_polybar_config, 'launch_polybar.sh')
    
    info("Creating launch_polybar.sh script...")

    launch_script_content = '''#!/usr/bin/env bash

if type "xrandr" > /dev/null; then
    for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
        MONITOR=$m polybar --reload toph &
    done
else
    polybar --reload toph &
fi
'''

    with open(launch_script_path, 'w') as file:
        file.write(launch_script_content)

    # Make the script executable
    run_command(f"chmod +x {launch_script_path}")

    info("Polybar configuration and launch script created successfully.")

