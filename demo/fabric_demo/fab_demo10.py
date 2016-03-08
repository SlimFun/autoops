#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['192.168.99.101','192.168.99.102']
env.password = 'linux'

@task
@runs_once
def tar_task():
    with lcd('/Users/milo'):
        local('tar -zcf tmp-will-drop.tgz TMP-will-drop')

@task
def put_task():
    run("mkdir -p /tmp/data")
    with cd('/tmp/data'):
        with settings(warn_only=True):
            result = put('/Users/milo/tmp-will-drop.tgz','/tmp/data/tmp-will-drop.tgz')
        if result.failed and not confirm('Put file failed, continue[Y/N]?'):
            abort('Aborting file put task!')

@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local('md5 /Users/milo/tmp-will-drop.tgz',capture=True).split(' ')[3] # mac os x 系统
        rmd5 = run('md5sum /tmp/data/tmp-will-drop.tgz').split(' ')[0]
    if lmd5 == rmd5:
        print 'OK'
    else:
        print 'ERROR'

