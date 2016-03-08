#!/usr/bin/env python
# encoding: utf-8

from fabric.api import local, lcd

def github():
    with lcd('/Users/milo/Coding/py/autoops_tools_demo/'):
        local('git add .')
        local('git commit -m "auto module test."')
        local('git push -u origin master')

