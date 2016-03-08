#!/usr/bin/env python
# encoding: utf-8

from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.99.101','192.168.99.102']
env.password = 'linux'

@runs_once
def input_raw():
    return prompt("Please input directory name: ", default = "/root")

def worktask(dirname):
    run('ls -l ' + dirname)

@task    # 限定只有go函数对外可见
def go():
    getdirname = input_raw()
    worktask(getdirname)
