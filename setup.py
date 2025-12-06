#!/usr/bin/env python
"""Setup configuration for task manager"""
from setuptools import setup, find_packages

setup(
    name="task-manager-cli",
    version="0.1.0",
    description="A Python CLI task manager with intentional ambiguities",
    author="Developer",
    python_requires=">=3.7",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "task-manager=src.cli:main",
        ]
    },
    install_requires=[
        # Standard library only
    ]
)
