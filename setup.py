#! /usr/bin/env python3

from __future__ import print_function
from os import sys, path

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

from setuptools import find_packages

setup(
    name='python_cpp_example',
    version='0.3',
    author='Benjamin Jack',
    author_email='benjamin.r.jack@gmail.com',
    description='A hybrid Python/C++ test project',
    long_description='',
    packages=find_packages('src'),
    package_dir={'':'src'},
    test_suite='tests',
    zip_safe=False,
)
