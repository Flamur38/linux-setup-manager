# src/terminator.py

import os
from src.utils import run_command, info
from src.dotfiles import clean_and_copy_dotfiles

import shutil

def install_terminator(dotfiles_dir, home_dir):
    """
    Install Terminator and copy its configuration.
    """
    info("Installing Terminator...")

    run_command("sudo apt-get update")
    run_command("sudo DEBIAN_FRONTEND=noninteractive apt-get install -y terminator")

    # Ensure terminator config directory exists
    terminator_config_dir = os.path.join(home_dir, ".config", "terminator")
    os.makedirs(terminator_config_dir, exist_ok=True)

    # Define source (dotfiles/terminator_config) and destination (~/.config/terminator/config)
    src_terminator_config = os.path.join(dotfiles_dir, "terminator_config")
    dst_terminator_config = os.path.join(terminator_config_dir, "config")

    # Copy terminator config (file, not folder)
    info("Copying Terminator configuration...")

    # If destination config exists, remove it
    if os.path.exists(dst_terminator_config):
        os.remove(dst_terminator_config)

    # Copy the file
    shutil.copy2(src_terminator_config, dst_terminator_config)

    info("Terminator configuration copied successfully.")

    # Install tree.sh script
    src_tree_script = os.path.join(dotfiles_dir, "tree.sh")
    dst_tree_script = "/usr/local/bin/tree.sh"

    info("Installing tree.sh helper script...")
    run_command(f"sudo cp {src_tree_script} {dst_tree_script}")
    run_command(f"sudo chmod +x {dst_tree_script}")

    info("Terminator and tree.sh setup completed successfully.")
