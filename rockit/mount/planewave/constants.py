#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by lmountd"""

from rockit.common import TFmt


class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2

    InvalidControlIP = 5

    # Command-specific codes
    MountControlNotRunning = 9
    MountNotInitialized = 10
    MountNotHomed = 11
    MountNotDisabled = 14
    UnknownParkPosition = 15

    OutsideHALimits = 20
    OutsideDecLimits = 21

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        5: 'error: command not accepted from this IP',

        # Command-specific codes
        9: 'error: PWI4 software is not running',
        10: 'error: mount has not been initialized',
        11: 'error: mount has not been homed',
        14: 'error: mount has already been initialized',
        15: 'error: unknown park position',

        20: 'error: requested coordinates outside HA limits',
        21: 'error: requested coordinates outside Dec limits',

        # tel specific codes
        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with telescope daemon',
        -102: 'error: command not available for this telescope'
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return f'error: Unknown error code {error_code}'


class MountState:
    """Represents the current mount state"""
    Disabled, Parked, Stopped, Slewing, Tracking = range(5)

    _labels = {
        0: 'DISABLED',
        1: 'PARKED',
        2: 'STOPPED',
        3: 'SLEWING',
        4: 'TRACKING',
    }

    _formats = {
        0: TFmt.Red + TFmt.Bold,
        1: TFmt.Yellow + TFmt.Bold,
        2: TFmt.Red + TFmt.Bold,
        3: TFmt.Yellow + TFmt.Bold,
        4: TFmt.Green + TFmt.Bold,
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
