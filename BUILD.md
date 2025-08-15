# Building and Distributing `sphc`

This document provides instructions for building the `sphc` package from source and distributing it to the Python Package Index (PyPI).

## Prerequisites

Before you can build and distribute `sphc`, you will need to have the following tools installed:

*   **Python 3:** Make sure you have a modern version of Python 3 installed.
*   **setuptools:** This is the standard tool for packaging Python projects. It should be installed with Python by default.
*   **wheel:** This tool is used to create wheel distributions, which are a pre-compiled package format for Python.
*   **twine:** This is the recommended tool for securely uploading your package to PyPI.

You can install `wheel` and `twine` using pip:

```bash
pip install wheel twine
```

## Building the Package

Once you have the prerequisites installed, you can build the package by running the following command in the root directory of the project:

```bash
python setup.py sdist bdist_wheel
```

This command will create a `dist` directory containing two files:

*   `sphc-1.0a.tar.gz`: This is a source distribution of the package.
*   `sphc-1.0a-py3-none-any.whl`: This is a wheel distribution of the package.

## Configuring PyPI Credentials

To avoid entering your username and password every time you upload a package, you can create a `.pypirc` file in your home directory.

**On macOS and Linux:** The file path is `~/.pypirc`.
**On Windows:** The file path is `C:\Users\YourUsername\.pypirc`.

Add the following content to the file, replacing `your_pypi_username` and `your_pypi_password` with your PyPI credentials:

```
[distutils]
index-servers =
    pypi
    sphc

[pypi]
repository: https://upload.pypi.org/legacy/
username: your_pypi_username

[sphc]
repository: https://upload.pypi.org/legacy/
username: your_pypi_username
password: your_pypi_password
```

Make sure to set the appropriate permissions for this file to make it readable and writable only by your user.

```bash
chmod 600 ~/.pypirc
```

## Uploading to PyPI

Once you have configured your `.pypirc` file, you can use `twine` to upload the distributions from the `dist` directory:

```bash
twine upload --repository sphc dist/*
```

This command will upload the package to PyPI using the credentials and repository URL defined for `sphc` in your `.pypirc` file.
