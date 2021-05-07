#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass remove_configuration_instances.yaml