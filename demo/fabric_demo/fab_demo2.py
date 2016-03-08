#!/usr/bin/env python
# encoding: utf-8

from fabric.api import local, lcd

def lsfab():
    with lcd('~/Coding/py/autoops_tools_demo'):
        local('ls')
