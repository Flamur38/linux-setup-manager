# mul1x-python

**mul1x-python** is a complete Debian-based setup manager to automatically configure a fresh Ubuntu, Kali, or Parrot OS system.

It installs essential tools, copies dotfiles, configures Neovim, window managers like i3 and Polybar, sets up Zsh and Oh-My-Zsh, and installs security tools.

---

##  Features

- Install essential development tools (`git`, `curl`, `htop`, etc.)
- Install general and security tools (e.g., `nmap`, `wireshark`, `gobuster`, `hydra`)
- Install and configure:
  - [i3](https://i3wm.org/) (Window Manager)
  - [Polybar](https://polybar.github.io/)
  - [Rofi](https://github.com/davatorium/rofi)
  - [Terminator](https://gnometerminator.blogspot.com/p/introduction.html)
  - [Tmux](https://github.com/tmux/tmux)
  - [Neovim](https://neovim.io/)
  - [Zsh](https://www.zsh.org/) + [Oh-My-Zsh](https://ohmyz.sh/)
- Copy and manage dotfiles automatically
- Install additional helper scripts like `tree.sh`
- Configure npm and install Pyright globally
- Install Google Chrome browser
- Clean and modular Python code

---

##  Project Structure

```plaintext
mul1x-python/
├── dotfiles/          # Your configuration files
├── src/               # Python scripts to automate the setup
├── README.md          # This file
├── requirements.txt   # Python requirements (empty for now)
