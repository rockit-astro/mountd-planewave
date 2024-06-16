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
    Disabled, NotHomed, Parked, Stopped, Slewing, Tracking, Homing = range(7)

    _labels = {
        0: 'DISABLED',
        1: 'NOT HOMED',
        2: 'PARKED',
        3: 'STOPPED',
        4: 'SLEWING',
        5: 'TRACKING',
        6: 'HOMING',
    }

    _colors = {
        0: 'red',
        1: 'red',
        2: 'yellow',
        3: 'red',
        4: 'yellow',
        5: 'green',
        6: 'yellow',
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._labels and status in cls._colors:
                return f'[b][{cls._colors[status]}]{cls._labels[status]}[/{cls._colors[status]}][/b]'
            return '[b][red]UNKNOWN[/red][/b]'

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
