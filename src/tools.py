# src/tools.py

import os
from src.utils import run_command, info

def install_general_tools():
    """
    Install general and security tools.
    """

    info("Installing general and security tools...")

    # 1. Install base packages
    base_packages = [
        "build-essential", "nmap", "nikto", "sqlmap",
        "python3", "python3-pip", "wireshark", "tcpdump",
        "htop", "zsh", "bat", "dirb", "gobuster", "hydra",
        "john", "aircrack-ng", "hashcat", "smbclient",
        "whois", "rdesktop", "nodejs", "ripgrep", "fd-find",
        "xclip", "flameshot"
    ]

    run_command("sudo apt-get update")
    run_command(f"sudo DEBIAN_FRONTEND=noninteractive apt-get install -y {' '.join(base_packages)}")

    # 2. Fix missing npm
    success, _ = run_command("command -v npm")
    if not success:
        info("npm not found, installing manually...")
        run_command("sudo apt-get install -y npm")

    # 3. Configure npm for local user and install pyright
    success, _ = run_command("command -v npm")
    if success:
        info("Configuring npm for local user...")
        home_dir = os.path.expanduser("~")
        npm_global_dir = os.path.join(home_dir, ".npm-global")
        os.makedirs(npm_global_dir, exist_ok=True)
        run_command(f"npm config set prefix {npm_global_dir}")
        run_command(f"export PATH={npm_global_dir}/bin:$PATH")

        info("Installing pyright globally...")
        run_command("npm install -g pyright")
    else:
        info("npm is still missing, skipping pyright installation.")

    # 4. Symlink fd if needed
    if not run_command("command -v fd")[0] and run_command("command -v fdfind")[0]:
        info("Creating symlink: fd -> fdfind")
        home_dir = os.path.expanduser("~")
        local_bin = os.path.join(home_dir, ".local", "bin")
        os.makedirs(local_bin, exist_ok=True)
        run_command(f"ln -sf $(which fdfind) {local_bin}/fd")
        run_command(f"export PATH={local_bin}:$PATH")

    # 5. Install fzf if not installed
    home_dir = os.path.expanduser("~")
    fzf_dir = os.path.join(home_dir, ".fzf")
    if not os.path.exists(fzf_dir):
        info("Cloning fzf...")
        run_command(f"git clone --depth 1 https://github.com/junegunn/fzf.git {fzf_dir}")
        run_command(f"{fzf_dir}/install --all")
    else:
        info("fzf already installed, skipping.")

    # 6. Install Snap packages
    if run_command("command -v snap")[0]:
        info("Installing Snap packages...")
        snap_packages = ["enum4linux", "seclists", "searchsploit"]
        for snap_package in snap_packages:
            run_command(f"sudo snap install {snap_package}")
    else:
        info("Snap is not installed, skipping Snap packages.")

    # 7. Install Google Chrome
    if not run_command("command -v google-chrome")[0]:
        info("Installing Google Chrome...")
        run_command("wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        run_command("sudo apt-get install -y /tmp/google-chrome.deb")
        run_command("rm /tmp/google-chrome.deb")
    else:
        info("Google Chrome already installed.")

    info("All general and security tools installed successfully.")

