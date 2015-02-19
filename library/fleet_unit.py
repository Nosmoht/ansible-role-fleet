#!/usr/bin/python

# -*- coding: utf-8 -*-

import os

FLEETCTL_BIN = '/usr/bin/fleetctl'

def get_unit_files(module):
    command = "%s list-unit-files" % (FLEETCTL_BIN)
    rc, out, err = module.run_command(command)
    if rc != 0:
        module.fail_json(msg="Error while listing unit files: %s" % (out), rc=rc, err=err)
    return True, out

def ensure(module):
    changed = False
    # Set parameters
    name = module.params['name']
    state = module.params['state']
    # Execute tasks based on current state
    unit_files = get_unit_files(module)
    return changed

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, Type=String),
            state=dict(Default='started', choices=['submitted', 'loaded', 'started', 'stopped', 'unloaded', 'destroyed']),
        ),
    )
    
    changed = ensure(module)
    module.exit_json(changed=changed, name=module.params['name'])

# this is magic, see lib/ansible/module_common.py
# <<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
