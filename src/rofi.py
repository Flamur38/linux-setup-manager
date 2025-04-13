# src/rofi.py

from src.utils import run_command, info

def install_rofi():
    """
    Install rofi using apt-get.
    """
    info("Installing rofi...")

    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y rofi")

    info("Rofi installed successfully.")

