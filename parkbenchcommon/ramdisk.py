# Copyright 2018 Joel Allen Luellwitz and Emily Frost
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

"""Provides a class for managing ramdisks."""

__all__ = ['Ramdisk', 'RamdiskMountError']

import logging
import os
import subprocess

class RamdiskMountError(Exception):
    """Raised when a ramdisk mount operation fails."""


class Ramdisk:
    """A class for managing ramdisks."""

    def __init__(self, path, size, uid, gid, mode):
        """Stores mountpoint and options.

        path: A string indicating the path where the ramdisk will be mounted.
        size: The size of the ramdisk to be mounted. This should be a string representing a
          number of bytes, and may include the single-character suffixes k, m, g, or % for
          kibibytes, mebibytes, gibibytes, or percentage of physical RAM, respectively.
        uid: The system user ID that should own the mount directory.
        gid: The system group ID that should be associated with the mount directory.
        mode: The mode of the mount directory access permissions. This should be a decimal
          integer. ex: 511, not 777.
          Note: This integer is most easily obtained by ORing the appropriate permission
          flags from the stat module.
        """
        self.logger = logging.getLogger(__name__)

        # The mount command outputs the canonical path of all mountpoints, so it will need
        #   to know the absolute path with any links resolved. Python calls this realpath.
        self.path = os.path.realpath(path)
        # TODO #16: On Python 3 migration, oct() will break this code.
        self.mount_options = 'size=%s,uid=%s,gid=%s,mode=%s' % (size, uid, gid, oct(mode))

    def mount(self):
        """Mounts the ramdisk. Raises an exception on failure, and does nothing if the disk
        is already mounted.
        """
        if not self.is_mounted():
            if os.path.isfile(self.path):
                raise RamdiskMountError(
                    'Could not mount ramdisk on %s. Specified path is a file.' % self.path)

            if not os.path.isdir(self.path):
                os.makedirs(self.path)

            if not os.listdir(self.path) == []:
                self.logger.warning('Ramdisk mountpoint %s is not empty.', self.path)

            return_code = subprocess.call(
                ['mount', '-t', 'tmpfs', '-o', self.mount_options, 'none',
                 self.path])

            if not self.is_mounted():
                # TODO #16: Implement exception chaining when we move to Python 3.
                raise RamdiskMountError(
                    'Could not mount ramdisk on %s. Mount return code was %s.' %
                    (self.path, return_code))

    def is_mounted(self):
        """Checks whether the ramdisk is mounted.
        
        Returns True if is mounted, returns False otherwise.
        """
        return 'none on %s type tmpfs' % self.path in str(subprocess.check_output('mount'))
