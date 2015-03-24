ansible-role-fleet
=========

# Description

The roles can be used to do the following tasks
- Checkout and build Fleet binaries (fleetd and fleetctl) on local or remote system
- Install Fleet binary files

The process of checking out and building Fleet binaries can be delegated to a remote system called _build host_.

# Requirements
- Ansible >= 1.2
- Git and Go must be installed on _build host_

# Role Variables
## Build variables

| Name | Description | Default value |
|:-----  | :----- | :----- |
| fleet_build | Boolean to define if binaries should be build | false |
| fleet_build_repo_url | String to define the Git repo URL | https://github.com/coreos/fleet.git |
| fleet_build_repo_update | Boolean to define if update should be checked out | false |
| fleet_build_version_default | String which equals the Git tag to checkout by default | v0.9.1 |
| fleet_build_host | String to define the host where build tasks will be delegated to | '{{ inventory_hostname }}' |
| fleet_build_path | String to define a directory where the Git repository will be cloned into | '{{ lookup(''env'', ''HOME'') }}/fleet' |
| fleet_build_bin_path | String to define the directory where binary files are stored | '{{ fleet_build_path}}/bin'

## Install variables
| Name | Description | Default value |
|:-----  | :----- | :----- |
| fleet_install | Boolean to define if the installation should be done | false |
| fleet_install_path | String to define where binaries will be installed | /usr/local/bin |
| fleet_install_binary_owner | String to define the binary owner | root |
| fleet_install_binary_group | String to define the binary group | root |
| fleet_install_binary_mode | String to define the binary mode | '0755' |
| fleet_install_sudo | Boolean to define if binary installation has to be done with sudo. Set to true if installing binaries into a directory which is owned by root (like /usr/bin) | false |

# Dependencies
None

# Example Playbook

Checkout, build and install Fleet binaries and local system using default values.

    - hosts: 127.0.0.1
      roles:
      - role: fleet
        fleet_build: true
        fleet_install: true

Checkout, build Fleet binaries on remote system build-host.example.com and install binaries on local system into /usr/bin.

    - hosts: 127.0.0.1
      roles:
      - role: fleet
        fleet_build: true
        fleet_build_host: build-host.example.com
        fleet_install: true
        fleet_install_path: /usr/bin
        fleet_install_sudo: true

License
-------

BSD

Author Information
------------------
[Thomas Krahn]

[Thomas Krahn]: emailto:ntbc@gmx.net
