#!/usr/bin/python

# -*- coding: utf-8 -*-

import os

FLEETCTL_BIN = '/usr/bin/fleetctl'

def fleetctl(module, action, unit):
    command = "%s %s %s" % (FLEETCTL_BIN, action, unit)
    rc, out, err = module.run_command(command)
    if rc != 0:
        module.fail_json(msg="Error while %s unit file %s: %s" % (action, unit, out), rc=rc, err=err)
    return True

def submit_unit(module, name, path):
    return fleetctl(module, 'submit', path + '/' + name)

def load_unit(module, name):
    return fleetctl(module, 'load', name)
    
def start_unit(module, name):
    return fleetctl(module, 'start', name)
    
def stop_unit(module, name):
    return fleetctl(module, 'stop', name)
    
def unload_unit(module, name):
    return fleetctl(module, 'unload', name)
    
def destroy_unit(module, name):
    return fleetctl(module, 'destroy', name)
    
def get_unit_files(module):
    command = "%s list-unit-files" % (FLEETCTL_BIN)
    rc, out, err = module.run_command(command)
    if rc != 0:
        module.fail_json(msg="Error while listing unit files: %s" % (out), rc=rc, err=err)
        
    result = [re.sub(r'(\t+?)\1', r'\1', line).split('\t') for line in out.split('\n') if line]        
    return result[1:]

def is_unit_submitted(unit, unit_files):
    for line in unit_files:
        if line[0] == unit:
            return True
    return False

def ensure(module):
    changed = False
    unit_files = None
    unit_file_exists = False
    instance_unit = False
    # Set parameters
    name = module.params['name']
    path = module.params['path']
    state = module.params['state']
    # Determine if unit is an instance unit (http://0pointer.de/blog/projects/instances.html)
    instance_unit = name.find('@') != -1
    unit_files = get_unit_files(module)
    if not instance_unit:
        unit_submitted = is_unit_submitted(name, unit_files)
    if state != 'destroyed' and not unit_submitted:        
        changed = submit_unit(module, name, path)
#    if state == 'loaded' 
    return changed

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, Type='String'),
            path=dict(required=False, Type='String'),
            state=dict(Default='started', choices=['submitted', 'loaded', 'started', 'stopped', 'unloaded', 'destroyed']),
        ),
    )
    
    changed = ensure(module)
    module.exit_json(changed=changed, name=module.params['name'])

# import module snippets
from ansible.module_utils.basic import *
main()
