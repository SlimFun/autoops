#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['192.168.99.101','192.168.99.102']
env.gateway = '192.168.99.103'
env.passwords = {
    'root@192.168.99.101:22': 'linux',
    'root@192.168.99.102:22': 'linux',
    'root@192.168.99.103:22': 'python'
}

lfile = '/Users/milo/TMP-will-drop/test.sh'
rfile = '/tmp/shell_script'

@task
def put_task():
    run('mkdir -p /tmp/shell_script')
    with settings(warn_only=True):
        result = put(lfile,rfile)
    if result.failed and not confirm('Put file failed, continue[Y/N]?'):
        abort('Aborting file put task!')

@task
def run_task():
    with cd('/tmp/shell_script'):
        run('sh test.sh')
        with cd('/root/'):
            run('ls -l ./')

@task
def go():
    put_task()
    run_task()
