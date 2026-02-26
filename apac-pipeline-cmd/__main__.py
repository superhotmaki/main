#!/usr/bin/env python3
"""
APAC Pipeline Command Center
Run with: python -m apac-pipeline-cmd
Or: python __main__.py
"""
import sys
import os

# Ensure we can import from this directory
sys.path.insert(0, os.path.dirname(__file__))

from cli import main

if __name__ == "__main__":
    main()
