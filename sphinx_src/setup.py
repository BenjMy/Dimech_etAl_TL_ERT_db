# -*- coding: utf-8 -*-
# Author: Óscar Nájera
# License: 3-clause BSD
"""
Installer Sphinx extension for gallery generator
"""

# Get the requirements from requirements.txt and environment
with open('requirements.txt', 'r') as fid:
    install_requires = [line.strip() for line in fid if line.strip()] 
