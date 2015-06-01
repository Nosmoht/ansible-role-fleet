ansible-role-fleet
=========

# Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Role variables](#role variables)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [License](#license)
- [Author information](#author information)

# Description

The roles installs Fleet binary files

# Requirements

- Ansible >= 1.9

# Role Variables

| Name | Description | Default value |
|:-----  | :----- | :----- |
| fleet_version | Fleet version to install | v0.10.1 |
| fleet_url | URL where to download package | https://github.com/coreos/fleet/releases/download/ |
| fleet_package_name | Package name to download | fleet-{{ fleet_version }}-linux-amd64 |
| fleet_package_file | Package file to download | '{{ fleet_package_name }}.tar.gz' |
| fleet_download_path | Path where to download package | /tmp |
| fleet_install | Boolean to define if the installation should be done | false |
| fleet_install_path | String to define where binaries will be installed | /usr/local/bin |
| fleet_install_binary_owner | String to define the binary owner | root |
| fleet_install_binary_group | String to define the binary group | root |
| fleet_install_binary_mode | String to define the binary mode | '0755' |

# Dependencies

None

# Examples

Install the binaries into /usr/local/bin
```yaml
- hosts: 127.0.0.1
  become: true
  become_user: root
  become_method: sudo
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
