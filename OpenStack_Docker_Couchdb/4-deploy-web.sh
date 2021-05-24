#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass 4-deploy-web.yaml -i inventory/application_hosts.ini