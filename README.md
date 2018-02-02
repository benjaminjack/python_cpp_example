# python_cpp_example

This repository contains an example Python module which wraps C++ code. The code presented here was designed to meet four requirements:

1. Python bindings for C++ code (using [`pybind11`](http://pybind11.readthedocs.io/en/stable/index.html) and built with [CMake](http://cmake.org))
2. Unit tests for C++ code (using [`catch`](http://catch-lib.net))
3. Unit tests for Python code (using `unittest`)
4. A `setuptools` setup.py script for building, installation, and testing

Please see the [blog post that accompanies this repository](http://www.benjack.io/2018/02/02/python-cpp-revisited.html) for more information.

**NOTE**: If you'd like to see the version of the repository that corresponds to my [original June 2017 blog post](http://www.benjack.io/2017/06/12/python-cpp-tests.html), go to [this release](https://github.com/benjaminjack/python_cpp_example/tree/v0.1). However, I no longer recommend using the repository structure from this old release.

# Installation

To build and install `python_cpp_example`, clone or download this repository and then, from within the repository, run:

```bash
python3 ./setup.py install
```

or

```bash
pip3 install .
```

# Tests

To execute all unit tests, run the following command:

```bash
python3 ./setup.py test
```

# Requirements

- Python 2 or 3
- CMake 2.8.12 or higher
- A modern compiler with C++11 support

# Acknowledgements

Much of the code in this repository was adapted from the [`pybind11` tutorial](http://pybind11.readthedocs.io/en/stable/basics.html) and the [`pybind11` example CMake repository](https://github.com/pybind/cmake_example).