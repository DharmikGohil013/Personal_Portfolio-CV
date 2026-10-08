#!/usr/bin/env python3
"""Rebuild everything: blog pages + hubs + index, then patch the homepage and main pages."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
for script in ('build.py', 'patch_index.py', 'patch_pages.py', 'patch_misc.py', 'audit.py'):
    print(f'\n==> {script}')
    r = subprocess.run([sys.executable, os.path.join(HERE, script)])
    if r.returncode and script != 'audit.py':
        sys.exit(r.returncode)
