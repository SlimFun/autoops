#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env

env.hosts = ['root@192.168.99.101']
env.password = 'linux'

def host_type():
    '''
    Usage: fab -H <ip_address or hostname>[可以是多台服务器] host_type
    e.g. fab -f fab_demo5.py host_type
    '''
    run('uname -s')
