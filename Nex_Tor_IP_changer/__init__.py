#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NexTOR IP Changer - Tor Exit Node Rotator
Package initialization module
"""

__version__ = "1.1"
__author__ = "Stalin"
__license__ = "MIT"
__doc__ = """
NexTOR IP Changer: Automatically rotate Tor exit nodes and change IP address.

This package provides tools for rotating Tor exit nodes and dynamically
changing your public IP address, intended for privacy research, OSINT,
and security testing purposes.
"""

from .NexTOR import main, new_tor_identity, ma_ip

__all__ = ['main', 'new_tor_identity', 'ma_ip']
