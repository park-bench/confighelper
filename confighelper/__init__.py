# Copyright 2015-2018 Joel Allen Luellwitz and Andrew Klapp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# TODO: Rename this package to parkbench-common.
"""confighelper is a support module for Parkbench projects."""

# TODO: This isn't done correctly, but removing it will break other projects right now.
from .confighelper import ConfigHelper
from .confighelper import ValidationException

__all__ = ['beaconbroadcaster', 'beaconreceiver', 'confighelper', 'tmpfs']
__author__ = 'Joel Luellwitz and Andrew Klapp'
__version__ = '0.8'
