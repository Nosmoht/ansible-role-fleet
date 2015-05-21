ansible-role-fleet
=========

# Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Role variables](#role variables)
- [Dependencies](#dependencies)
- [License](#license)
- [Author information](#author information)

# Description

The roles can be used to do the following tasks
- Checkout and build Fleet binaries (fleetd and fleetctl)
- Install Fleet binary files

# Requirements

- Ansible >= 1.2
- Git and Go must be installed

# Role Variables

## Build variables

| Name | Description | Default value |
|:-----  | :----- | :----- |
| fleet_build | Boolean to define if binaries should be build | false |
| fleet_build_repo_url | String to define the Git repo URL | https://github.com/coreos/fleet.git |
| fleet_build_repo_update | Boolean to define if update should be checked out | false |
| fleet_build_version_default | String which equals the Git tag to checkout by default | v0.10.1 |
| fleet_build_path | String to define a directory where the Git repository will be cloned into | $HOME/fleet |
| fleet_build_bin_path | String to define the directory where binary files are stored | $HOME/fleet/bin'

## Install variables

| Name | Description | Default value |
|:-----  | :----- | :----- |
| fleet_install | Boolean to define if the installation should be done | false |
| fleet_install_path | String to define where binaries will be installed | /usr/local/bin |
| fleet_install_binary_owner | String to define the binary owner | root |
| fleet_install_binary_group | String to define the binary group | root |
| fleet_install_binary_mode | String to define the binary mode | '0755' |

## Fleet variables

The following variables must be set using the role to submit, start, stop or destroy unit files

| Name | Description | Default value |
| :----- | :----- | :----- |
| fleet_protocol | String to define if http or https should be used | http |
| fleet_endpoint | String to define the Fleet node to connect to | 127.0.0.1 |
| fleet_port | Number to define the port to be used to connect to | 4001 |
| fleet_bin_path | Path to fleetctl and fleetd binary | '{{ fleet_install_path}}' |

# Dependencies

None

# Example Playbook

Checkout Fleet into $HOME/fleet and build binaries.
```yaml
- hosts: 127.0.0.1
  roles:
  - role: fleet
    fleet_build: true
```

Install the binaries builded above into /usr/local/bin
```yaml
- hosts: 127.0.0.1
  sudo: true
  roles:
  - role: fleet
    fleet_install: true
```

# License

Copyright 2015 [Thomas Krahn]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# Author Information

[Thomas Krahn]

[Thomas Krahn]: emailto:ntbc@gmx.net
