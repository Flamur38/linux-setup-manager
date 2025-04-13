# src/main.py

# Import helper functions and module installers
from src.utils import info, error, run_command
from src.dotfiles import clean_and_copy_dotfiles
from src.neovim import install_neovim, sync_nvim_config
from src.i3 import install_i3, sync_i3_config
from src.polybar import install_polybar, sync_polybar_config
from src.rofi import install_rofi
from src.terminator import install_terminator
from src.tmux import install_tmux
from src.tools import install_general_tools
from src.zsh import install_zsh

import os

def is_tool_installed(tool_name):
    """
    Check if a tool is installed using 'which'.
    """
    success, _ = run_command(f"which {tool_name}")
    return success

def install_tool(tool_name):
    """
    Install a tool using apt-get if it's not already installed.
    """
    if is_tool_installed(tool_name):
        info(f"{tool_name} is already installed. Skipping installation.")
    else:
        info(f"{tool_name} is not installed. Installing now...")
        run_command(f"sudo apt-get update")
        run_command(f"sudo apt-get install -y {tool_name}")
        info(f"{tool_name} installation completed.")

def main():
    """
    Main function to set up the system.
    """

    # Set up paths
    dotfiles_dir = os.path.join(os.path.dirname(__file__), '..', 'dotfiles')
    home_dir = os.path.expanduser("~")

    # 1. Install basic tools
    tools = [
        "git",
        "curl",
        "htop"
    ]

    for tool in tools:
        install_tool(tool)

    # 2. Install general and security tools
    install_general_tools()

    # 3. Install i3 and related tools
    install_i3()

    # 4. Install Polybar
    install_polybar()

    # 5. Install Rofi
    install_rofi()

    # 6. Install Zsh and Oh-My-Zsh
    install_zsh()

    # 7. Install Terminator
    install_terminator(dotfiles_dir, home_dir)

    # 8. Install Tmux
    install_tmux(dotfiles_dir, home_dir)

    # 9. Install Neovim
    install_neovim()

    # 10. Copy general dotfiles
    info("Copying dotfiles...")
    clean_and_copy_dotfiles(dotfiles_dir, home_dir)
    info("Dotfiles copied successfully.")

    # 11. Sync i3 configuration
    sync_i3_config(dotfiles_dir, home_dir)

    # 12. Sync Polybar configuration
    sync_polybar_config(dotfiles_dir, home_dir)

    # 13. Sync Neovim configuration
    sync_nvim_config(dotfiles_dir, home_dir)

if __name__ == "__main__":
    main()
