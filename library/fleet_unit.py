#!/usr/bin/python

# -*- coding: utf-8 -*-

import os

FLEETCTL_BIN = 'fleetctl'

def fleetctl(module, action, unit):
    command = "%s %s %s" % (FLEETCTL_BIN, action, unit)
    rc, out, err = module.run_command(command)
    if rc != 0:
        module.fail_json(msg="Error while %s unit file %s: %s" % (action, unit, out), rc=rc, err=err)
    return True

def submit_unit(module, name, path):
    if path:
        return fleetctl(module, 'submit', path + '/' + name)
    else:
        return fleetctl(module, 'submit', name)

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
    unit_file_name = None
    # Determine if unit is an instance unit (http://0pointer.de/blog/projects/instances.html)
    # True: apache@8080.service, False: apache@.service, myapp.service
    if re.search(r'@.+\.', unit):
        unit_file_name = re.sub('(.+@)(.+)(\..+)', r'\1\3', unit)
    else:
        unit_file_name = unit;
    
    for line in unit_files:
        if line[0] == unit_file_name:
            return True
    return False

def get_unit_state(unit):
    if unit:
        return unit[3]
    return None

def unit_is_loaded(unit):
    return get_unit_state(unit) == 'loaded'

def unit_is_started(unit):
    return get_unit_state(unit) == 'running'

def unit_is_stopped(unit):
    return get_unit_state(unit) == 'stop'

def get_units(module):
    command = "%s list-units" % (FLEETCTL_BIN)
    rc, out, err = module.run_command(command)
    if rc != 0:
        module.fail_json(msg="Error while listing units: %s" % (out), rc=rc, err=err)
    result = [re.sub(r'(\t+?)\1', r'\1', line).split('\t') for line in out.split('\n') if line]
    return result[1:]

def get_unit(name, units):
    for unit in units:
        if unit[0] == name:
            return unit;
    return None

def ensure(module):
    changed = False
    unit_files = None
    unit_file_exists = False
    unit = None
    # Set parameters
    name = os.path.basename(module.params['name'])
    path = os.path.dirname(module.params['name'])
    state = module.params['state']

    unit_files = get_unit_files(module)
    unit_submitted = is_unit_submitted(name, unit_files)

    if not unit_submitted:
        if state not in ['destroyed', 'unloaded']: 
            changed = submit_unit(module, name, path)
        else:
            module.fail_json(msg="Unit not submitted: %s" % name)

    unit = get_unit(name, get_units(module))

    if state == 'started' and not unit_is_started(unit):
        changed = start_unit(module, name)
    if state == 'stopped' and unit_is_started(unit):
        changed = stop_unit(module, name)
    if state == 'destroyed' and unit_submitted:
        changed = destroy_unit(module, unit)
    return changed

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, Type='String'),
            state=dict(Default='started', choices=['submitted', 'loaded', 'started', 'stopped', 'unloaded', 'destroyed']),
        ),
    )
    
    changed = ensure(module)
    module.exit_json(changed=changed, name=module.params['name'])

# import module snippets
from ansible.module_utils.basic import *
main()
