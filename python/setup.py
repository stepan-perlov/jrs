#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from jrs import __version__

setup(
    name="jrs",
    version=__version__,
    url="https://github.com/stepan-perlov/jrs#python-jrs",
    description="json: [rpc, schema]",
    license='MIT',
    author="Stepan Perlov",
    author_email="stepanperlov@gmail.com",
    packages=["jrs"],
    platforms=["linux"]
)
