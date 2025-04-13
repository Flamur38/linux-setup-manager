#!/bin/bash

# Color definitions
COLOR_FILE="\033[0;36m"    # Cyan for file path
COLOR_RESET="\033[0m"      # Reset color

# Function to show tree and file contents
function tree_with_content {
  # If no directory argument is passed, use the current directory
  DIRECTORY="${1:-.}"

  # Ensure the directory exists
  if [[ ! -d "$DIRECTORY" ]]; then
    echo "Error: $DIRECTORY is not a valid directory."
    exit 1
  fi

  # Use `find` to list files and then show content
  find "$DIRECTORY" -type f | while IFS= read -r line; do
    # Print file path in cyan color
    echo -e "${COLOR_FILE}$line${COLOR_RESET}"  # Show the file path in cyan
    cat "$line"                                # Show the file content directly
  done
}

# Call the function with the directory you want to scan
tree_with_content "$1"

#sudo cp tree.sh /usr/local/bin/tree.sh

