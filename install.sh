#!/bin/bash

# Install Titandork
echo "Installing Titandork..."

# Create the directory structure if not already existing
sudo mkdir -p /usr/local/bin

# Copy the Python script to the appropriate directory
sudo cp usr/local/bin/titandork.py /usr/local/bin/titandork

# Give execution permissions to the script
sudo chmod +x /usr/local/bin/titandork

echo "Titandork installed successfully!"

