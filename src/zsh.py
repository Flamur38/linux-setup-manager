# src/zsh.py

from src.utils import run_command, info

import os

def install_zsh():
    """
    Install Zsh and Oh-My-Zsh.
    """

    info("Installing Zsh and Oh-My-Zsh...")

    # Install zsh and curl
    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y zsh curl")

    # Change default shell to zsh if not already
    shell = os.environ.get("SHELL", "")
    zsh_path = run_command("which zsh")[1]

    if shell != zsh_path:
        info("Changing default shell to zsh...")
        user = os.environ.get("USER", "")
        run_command(f"sudo chsh -s {zsh_path} {user}")
    else:
        info("Default shell is already zsh. Skipping.")

    # Install Oh-My-Zsh if not installed
    home_dir = os.path.expanduser("~")
    oh_my_zsh_dir = os.path.join(home_dir, ".oh-my-zsh")

    if not os.path.exists(oh_my_zsh_dir):
        info("Installing Oh-My-Zsh...")
        run_command('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
    else:
        info("Oh-My-Zsh already installed. Skipping.")

    info("Zsh and Oh-My-Zsh setup completed successfully.")

