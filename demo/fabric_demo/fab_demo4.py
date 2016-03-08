#!/usr/bin/env python
# encoding: utf-8

from fabric.api import local,cd,run,env

env.hosts = ['user@ip:port',]
env.password = 'pwd'

def setting_ci():
	local('echo "add and commit settings in local"')
	with lcd('/Users/milo/Coding/py/autoops_tools_demo/'):
		local('git add .')
		local('git commit -m "auto module test."')
		local('git push -u origin master')

def update_setting_remote():
	print "remote update"
	with cd('~/temp'):
		run('ls -l | wc -l')

def update():
	setting_ci()
	update_seeting_remote()