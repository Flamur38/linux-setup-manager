# src/neovim.py

import os
from src.utils import run_command, info

def install_neovim():
    """
    Install Neovim from the GitHub release tarball.
    Removes old versions and installs the requested version.
    """
    info("Installing Neovim from GitHub release...")

    # Step 1: Install dependencies
    dependencies = [
        "curl", "tar", "gcc", "make", "unzip", "gettext",
        "libtool", "libtool-bin", "autoconf", "automake",
        "cmake", "pkg-config"
    ]
    run_command(f"sudo apt-get update")
    run_command(f"sudo apt-get install -y {' '.join(dependencies)}")

    # Step 2: Define version and download
    version = "v0.10.0"
    url = f"https://github.com/neovim/neovim/releases/download/{version}/nvim-linux64.tar.gz"
    run_command(f"curl -LO {url}")

    # Step 3: Extract the tar.gz file
    run_command(f"tar xzf nvim-linux64.tar.gz")

    # Step 4: Remove old Neovim install if it exists
    run_command(f"sudo rm -rf /opt/nvim")

    # Step 5: Move the new Neovim to /opt
    run_command(f"sudo mv nvim-linux64 /opt/nvim")

    # Step 6: Create a symlink to /usr/local/bin
    run_command(f"sudo ln -sf /opt/nvim/bin/nvim /usr/local/bin/nvim")

    # Step 7: Clean up downloaded tar.gz
    run_command(f"rm nvim-linux64.tar.gz")

    info("Neovim installed successfully.")

def sync_nvim_config(project_dotfiles_dir, home_dir):
    """
    Copy Neovim configuration from project dotfiles to user's home directory.
    """
    from src.dotfiles import clean_and_copy_dotfiles

    src_nvim_config = os.path.join(project_dotfiles_dir, 'nvim')
    dst_nvim_config = os.path.join(home_dir, '.config', 'nvim')

    info("Syncing Neovim configuration...")

    clean_and_copy_dotfiles(src_nvim_config, dst_nvim_config)

    info("Neovim configuration synced successfully.")

