#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.99.101','192.168.99.102']
env.password = 'linux'

@runs_once
def local_task():
    local('uname -a')

def remote_task():
    with cd('/root/'):
        run('ls -l')
