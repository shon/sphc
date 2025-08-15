# Building and Distributing `sphc`

This document provides instructions for building the `sphc` package from source and distributing it to the Python Package Index (PyPI).

## Prerequisites

Before you can build and distribute `sphc`, you will need to have the following tools installed:

*   **Python 3:** Make sure you have a modern version of Python 3 installed.
*   **build:** This is the standard tool for building Python packages.
*   **twine:** This is the recommended tool for securely uploading your package to PyPI.

You can install `build` and `twine` using pip:

```bash
pip install build twine
```

## Building the Package

Once you have the prerequisites installed, you can build the package by running the following command in the root directory of the project:

```bash
python -m build
```

This command will create a `dist` directory containing two files:

*   `sphc-1.0a.tar.gz`: This is a source distribution of the package.
*   `sphc-1.0a-py3-none-any.whl`: This is a wheel distribution of the package.

## Uploading to PyPI

Once you have built the package, you can use `twine` to upload the distributions from the `dist` directory. `twine` will securely prompt for your PyPI username and password.

```bash
twine upload dist/*
```

For more information on distributing Python packages, please see the [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
