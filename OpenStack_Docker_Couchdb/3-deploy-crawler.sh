#!/bin/bash

. ./openrc.sh; ansible-playbook --ask-become-pass 3-deploy-crawler.yaml -i inventory/application_hosts.ini