# src/dotfiles.py

import os
import shutil
from src.utils import info, error

def clean_and_copy_dotfiles(dotfiles_dir, home_dir):
    """
    Remove old dotfiles and copy new ones from dotfiles_dir to home_dir.
    
    Args:
        dotfiles_dir (str): Path to the local dotfiles folder in project.
        home_dir (str): Path to the user's home directory.
    """
    # List all files and folders inside dotfiles/
    for item in os.listdir(dotfiles_dir):
        src = os.path.join(dotfiles_dir, item)          # Source file (in project)
        dst = os.path.join(home_dir, f".{item}")         # Destination file (in home directory, with . prefix)

        # If destination already exists, remove it
        if os.path.exists(dst):
            if os.path.isfile(dst) or os.path.islink(dst):
                info(f"Removing old file {dst}")
                os.remove(dst)
            elif os.path.isdir(dst):
                info(f"Removing old directory {dst}")
                shutil.rmtree(dst)

        # Now copy the new file or folder
        if os.path.isfile(src):
            info(f"Copying file {src} to {dst}")
            shutil.copy2(src, dst)
        elif os.path.isdir(src):
            info(f"Copying directory {src} to {dst}")
            shutil.copytree(src, dst)

