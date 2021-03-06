#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for solstice-libs-picker
"""

import pytest

from solstice.libs.picker import __version__


def test_version():
    assert __version__.get_version()
