#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass docker.yaml -i inventory/application_hosts.ini