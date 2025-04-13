# src/tmux.py

import os
import shutil
from src.utils import run_command, info

def install_tmux(dotfiles_dir, home_dir):
    """
    Install tmux, copy configuration, and install TPM (Tmux Plugin Manager).
    """
    info("Installing tmux...")

    run_command("sudo apt-get update")
    run_command("sudo DEBIAN_FRONTEND=noninteractive apt-get install -y tmux")

    # Copy .tmux.conf
    src_tmux_conf = os.path.join(dotfiles_dir, ".tmux.conf")
    dst_tmux_conf = os.path.join(home_dir, ".tmux.conf")

    info("Copying tmux configuration...")

    # If old tmux.conf exists, remove it first
    if os.path.exists(dst_tmux_conf):
        os.remove(dst_tmux_conf)

    # Copy the file
    shutil.copy2(src_tmux_conf, dst_tmux_conf)

    info(".tmux.conf copied successfully.")

    # Ensure ~/.local/scripts exists
    local_scripts_dir = os.path.join(home_dir, ".local", "scripts")
    os.makedirs(local_scripts_dir, exist_ok=True)

    # Install TPM (Tmux Plugin Manager)
    tpm_dir = os.path.join(home_dir, ".tmux", "plugins", "tpm")

    if not os.path.exists(tpm_dir):
        info("Cloning TPM (Tmux Plugin Manager)...")
        run_command(f"git clone https://github.com/tmux-plugins/tpm {tpm_dir}")
    else:
        info("TPM already installed. Skipping clone.")

    # Install tmux plugins
    if run_command("command -v tmux")[0]:
        info("Installing tmux plugins...")
        run_command(f"{tpm_dir}/bin/install_plugins")
    else:
        info("tmux command not found, skipping plugin install.")

    info("Tmux setup completed successfully.")
