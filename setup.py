# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import bo
version = bo.__version__

setup(
    name='braonly',
    version=version,
    author='',
    author_email='zhe.li@me.com',
    packages=[
        'bo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['bo/manage.py'],
)