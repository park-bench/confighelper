# confighelper

_confighelper_ is a library to help parse Parkbench configuration files. Configuration files
are assumed to be in the format defined by the ConfigParser Python module. This library is
**not** a general purpose library and is only intended for use by the Parkbench project.

_confighelper_ is licensed under the GNU GPLv3.

This is software is still in _beta_ and may not be ready for use in a production environment.

Bug fixes are welcome!

## Prerequisites
This software is currently only supported in Ubuntu 18.04.

Currently, the only supported method for installation of this project is building and
installing a Debian package. The rest of these instructions make the following assumptions:

*   `debhelper`, `dh-python`, `python-all`, and `python-setuptools` are installed on your build
    server.
*   You are familiar with using a Linux terminal.
*   You are somewhat familiar with using `debuild`.

## Steps to Build and Install

1.  Clone the repository and checkout the latest release tag. (Do not build against the
    `master` branch. The `master` branch might not be stable.)
2.  Use `debuild` in the project root directory to build the package.
3.  Use `dpkg -i` to install the package.
4.  Run `apt-get -f install` to resolve any missing dependencies.

The library should now be available for other Parkbench projects to use.
