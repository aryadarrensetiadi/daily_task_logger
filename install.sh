#!/bin/bash
# install.sh — Dependency installer for daily_task_logger
#
# This script installs required dependencies:
# - Python 3
# - pip3
# - Telethon (Python library)
#
# Usage: bash install.sh
# Note: Run with bash, or ensure this file is executable: chmod +x install.sh

echo "🚀 Starting installation of required dependencies..."

# Update package repository
sudo apt update

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "⚠️  Python3 is not installed on this system."

    read -p "Would you like to install Python3 now? (y/n): " choice
    if [[ "$choice" == [Yy] ]]; then
        echo "📦 Installing Python3..."
        sudo apt install -y python3 python3-pip
    else
        echo "❌ Installation aborted: Python3 is required."
        exit 1
    fi
else
    echo "✅ Python3 found: $(python3 --version)"
fi

# Ensure pip3 is installed
if ! command -v pip3 &>/dev/null; then
    echo "📦 Installing pip3..."
    sudo apt install -y python3-pip
fi

# Install Telethon if it's not already installed
if ! python3 -c "import telethon" &>/dev/null; then
    echo "📦 Installing Telethon via pip3..."
    pip3 install telethon
else
    echo "✅ Telethon already installed."
fi

# Show Telethon package information
echo "📦 Telethon version:"
pip3 show telethon | grep -E 'Name|Version|Location'

echo "🎉 Installation complete!"
