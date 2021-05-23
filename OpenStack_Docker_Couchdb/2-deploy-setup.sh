#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass 2-deploy-setup.yaml -i inventory/application_hosts.ini