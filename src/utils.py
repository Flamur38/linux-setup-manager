# src/utils.py

import subprocess  # Allows us to run shell commands from Python
from colorama import Fore, Style, init  # Colorama for colored terminal output

# Initialize colorama
init(autoreset=True)

def info(message):
    """
    Print a normal information message in green.
    """
    print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} {message}")

def error(message):
    """
    Print an error message in red.
    """
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")

def run_command(command):
    """
    Run a shell command safely and show real-time output.
    
    Args:
        command (str): The shell command to run (like 'ls', 'which git')

    Returns:
        (bool, str): 
            - True and last line of output if the command succeeded.
            - False and error output if the command failed.
    """
    try:
        # Open the process
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True  # Return output as string, not bytes
        )

        last_line = ""
        # Stream output live
        for line in process.stdout:
            print(line.strip())  # Print each line immediately
            last_line = line.strip()

        # Wait for the command to finish
        process.wait()

        if process.returncode == 0:
            return True, last_line
        else:
            return False, last_line

    except Exception as e:
        # If the process fails completely
        return False, str(e)
