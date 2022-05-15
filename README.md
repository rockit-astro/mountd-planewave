## Planewave L mount daemon

`lmountd` interfaces with the PWI4 http api and exposes a
coherent telescope control interface via Pyro.

`lmount` is a commandline utility for controlling the telescope.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the software architecture and instructions for developing and deploying the code.

### Configuration

Configuration is read from json files that are installed by default to `/etc/lmountd`.
A configuration file is specified when launching the server, and the `lmount` frontend will search this location when launched.

```python
{
  "daemon": "clasp_telescope", # Run the server as this daemon. Daemon types are registered in `warwick.observatory.common.daemons`.
  "log_name": "lmountd@clasp", # The name to use when writing messages to the observatory log.
  "control_machines": ["CLASPTCS"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `warwick.observatory.common.IP`.
  "pwi_host": "localhost", # Host name of the PWI4 server. This should generally stay as localhost.
  "pwi_port": 8220, # Port of the PWI server.
  "pwi_timeout": 0.5, # Communication timeout with the PWI server (in seconds).
  "slew_poll_interval": 0.5, # Interval to poll the mount for slew completion (in seconds)
  "slew_timeout": 60, # Maximum time to slew from any position to any other position (in seconds)
  "home_poll_interval": 5, # Interval to poll the mount for homing completion (in seconds)
  "home_timeout": 60, # Maximum time to find home position (in seconds)
  "ha_soft_limits": [-90, 90], # Allowed hour angle range in degrees
  "dec_soft_limits": [-45, 90], # Allowed declination range in degrees
  "park_positions": {
    "stow": { # Positions that can be used with 'tel park'.
      "desc": "general purpose park position", # Description reported by 'tel park'.
      "alt": 50, # Altitude in degrees.
      "az": 0 # Azimuth in degrees.
    }
  }
}
```

### Initial Installation

The automated packaging scripts will push 3 RPM packages to the observatory package repository:

| Package           | Description |
| ----------------- | ------ |
| clasp-lmount-server | Contains the `lmountd` server and configuration for the CLASP telescope. |
| observatory-lmount-client | Contains the `lmount` commandline utility for controlling the telescope server. |
| python3-warwick-observatory-lmount | Contains the python module with shared code. |

`clasp-lmount-server` and `observatory-lmount-client` should be installed on the `clasp-tcs` machine.

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable lmountd@<config>
sudo systemctl start lmountd@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `warwick.observatory.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl stop lmountd@<config>
sudo systemctl start lmountd@<config>
```

### Testing Locally

The server and client can be run directly from a git clone:
```
./lmountd onemetre.json
LMOUNTD_CONFIG_PATH=./clasp.json ./lmount status
```
