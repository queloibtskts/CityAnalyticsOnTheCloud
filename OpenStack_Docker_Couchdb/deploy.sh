#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass deploy.yaml -i inventory/application_hosts.ini