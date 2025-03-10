#!/usr/bin/env python

import subprocess
from pathlib import Path


def main() -> None:
    """Initialize the project after generation."""
    # Initialize git repository
    subprocess.run(["git", "init"], check=True)
    
    # Create virtual environment using hatch
    subprocess.run(["hatch", "env", "create"], check=True)
    
    # Install development dependencies using uv
    subprocess.run(["uv", "pip", "install", "-e", "."], check=True)


if __name__ == "__main__":
    main()
