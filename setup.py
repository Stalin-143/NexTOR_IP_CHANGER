#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nextor",
    version="1.1",
    author="Stalin",
    author_email="stalin@example.com",
    description="Automatically rotate Tor exit nodes and display updated IP address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Stalin-143/NexTOR_IP_CHANGER",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests[socks]>=2.22.0",
        "stem>=1.8.0",
    ],
    entry_points={
        "console_scripts": [
            "nextor=Nex_Tor_IP_changer.NexTOR:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
