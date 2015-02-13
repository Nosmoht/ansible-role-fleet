Role Name
=========

Setup and manage Fleet services used in CoreOS.

Features:
- Setup a directory where unit files will be stored
- Deployment of Fleet unit files based on templates

Not yet implemented:
- Library to manage (start, stop, submit, unload, ... ) unit files with fleetctl.

Requirements
------------

Ansible

Role Variables
--------------

| Name | Description | Default |
| ------- | ---------------- | --------- |
| fleet_unit_file_owner | OS user owning unit files| core |
| fleet_unit_file_group | OS group owing unit files | core |
| fleet_unit_file_directory_path | Directory where unit files will be stored | /home/core/services |
| fleet_unit_file_directory_mode | Mode of unit files | '0750' |
| fleet_unit_file_template | Template used to generate unit files| unit.service.j2 |
| fleet_docker_cmd | Docker executable file. Will be used inside the default template. | /usr/bin/docker |
| fleet_default_required_services | Default services required for a service. Used inside template file | ['etcd.service','docker.service'] |
| fleet_unit_files | Array of Unit file definitions to deploy. Must be set by Playbook or group/host vars | See following description|

Unit file variables
------------
| Name | Description | Type |
| -------- | -------------- | ------- |
| name | Unit file filename | String
| image_owner | Name of image owner in Registry | String |
| image_name | Name of image in Registry | String |
| container_name | Name of the container when started by Docker | String |
| registry_hostname | Hostname of registry where to pull the image from. If empty image will be put from public Docker registry | String |
| registry_port | Port of registry where to pull image from | Integer |
| requires | List of services that must be started as a requirement | Array of Strings |
| before | List of services that must be started before the service can be started | Array of String |
| bindsto | List of services the service binds to | Array of Strings |
| conflicts | List of services which do conflict with this services. If specified Fleet will start the service on another CoreOS node | Array of String |
| run_options | Options passed to docker run | String |
| run_args | Arguments passed to the container | String |

Dependencies
------------

None. CoreOS must be prepared with a Python interpreter.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: coreos
      vars:
        fleet_units:
        - name: myapp.service
          image_owner: user
          image_name: myapp
          registry_hostname: registry.example.com
          registry_port: 5000
          container_name: myappcontainer
          requires:
          - docker.service
          after:
          - docker.service
          conflicts:
          - my2app.service
      roles:
         - { role: fleet }

License
-------



Author Information
------------------

email: thomas.krahn@esailors.de
