#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass 1-deploy-vm.yaml