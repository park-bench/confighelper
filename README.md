# ConfigHelper

ConfigHelper is a library to help parse Parkbench configuration files. 
Configuration files are assumed to be in the format defined by the 
ConfigParser Python module. This library is **not** a general purpose library
and is only intended for use by the Parkbench project.

ConfigHelper is licensed under the GNU GPLv3.

Bug fixes are welcome.

This software is currently only supported on Ubuntu 14.04 and may not be ready
for use in a production environment.

The only current method of installation for our software is building and
installing your own package. We make the following assumptions:
* You are already familiar with using a Linux terminal.
* You already know how to use GnuPG.
* You are already somewhat familiar with using debuild.

Clone the latest *release tag*, not the `master` branch, as `master` may not be
stable.  Build the package with `debuild` from the project directory and
install with `dpkg -i`. Resolve any missing dependencies with `apt-get -f
install`.
