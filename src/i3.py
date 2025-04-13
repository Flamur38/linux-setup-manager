# src/i3.py

import os
from src.utils import run_command, info
from src.dotfiles import clean_and_copy_dotfiles

def install_i3():
    """
    Install i3 and related packages using apt-get.
    """
    info("Installing i3 and related packages...")

    # List of i3-related packages
    packages = [
        "i3", "i3status", "xbacklight",
        "pavucontrol", "pulseaudio-utils"
    ]

    # Install the packages
    run_command(f"sudo apt-get update")
    run_command(f"sudo apt-get install -y {' '.join(packages)}")

    info("i3 and related packages installed successfully.")

def sync_i3_config(project_dotfiles_dir, home_dir):
    """
    Copy i3 and i3status configurations from dotfiles to home directory.
    """
    info("Syncing i3 configuration...")

    src_i3_config = os.path.join(project_dotfiles_dir, 'i3')
    dst_i3_config = os.path.join(home_dir, '.config', 'i3')

    src_i3status_config = os.path.join(project_dotfiles_dir, 'i3status')
    dst_i3status_config = os.path.join(home_dir, '.config', 'i3status')

    # Copy i3 config
    if os.path.exists(src_i3_config):
        clean_and_copy_dotfiles(src_i3_config, dst_i3_config)
        info("i3 configuration copied.")
    else:
        info("No i3 configuration found in dotfiles. Skipping i3 config.")

    # Copy i3status config
    if os.path.exists(src_i3status_config):
        clean_and_copy_dotfiles(src_i3status_config, dst_i3status_config)
        info("i3status configuration copied.")
    else:
        info("No i3status configuration found in dotfiles. Skipping i3status config.")

