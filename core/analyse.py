#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys,os,time,datetime,json,commands
from daemon import Daemon
import tools

"""Pantalaimon
守护进程实现类
"""
class Pantalaimon(Daemon):
    """run
	定时执行任务的函数
    """
    def run(self):
    	while True:
    		result = commands.getoutput(self.com)
    		tools.write_access_log(self.name,result)
    		interval = int(self.interval)
    		time.sleep(interval)

    def set_interval(self,interval):
    	"""设置时间间隔"""
    	self.interval = int(interval)

    def set_command(self,com):
    	"""设置命令"""
    	self.com = com

"""run_cron
运行命令
Args:
	name str 这项任务的名称
	com  str 需要执行的命令
	interval int 执行命令需要间隔的时间，单位为秒
	action str 需要执行的动作
"""
def run_cron(name,com,interval,action):
	pan = Pantalaimon(name)
	pan.set_command(com)
	pan.set_interval(interval)

	if action == "start":
		pan.start()
	elif action == "stop":
		pan.stop()
	elif action == "restart":
		pan.restart()
	elif action == "status":
		pan.status

"""get_config
获取配置
"""
def get_config():
	f = open(tools.cur_file_dir()+"config/config.json")
	file_content = f.read()
	f.close()
	try:
		config = json.loads(file_content)
	except Exception:
		print "config isn't a standard Json."
		print "Please rewrite."
		return False
	return config

"""run
分析入口
Args:
	cron_name str 需要执行的任务名称
	action str 需要执行的动作
"""
def run(cron_name="all",action="start"):
	config = get_config()

	for com_type in config.keys():
		for k in config[com_type].keys():
			if cron_name != "all" and cron_name.lower() != k.lower():
				continue
			name 	= k
			com 	= com_type + " " + config[com_type][k]['path'] + " " + config[com_type][k]['param']
			interval= config[com_type][k]['interval']
			run_cron(name,com,interval,action.lower())

"""get_all_cron_name
获得所有的任务名称
Return:
	list 所有配置的名称
"""
def get_all_cron_name():
	config = get_config()
	config_name = []
	for com_type in config.keys():
		config_name.extend(config[com_type].keys())
	return config_name
