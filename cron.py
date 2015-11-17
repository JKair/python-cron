#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from core.analyse import run,get_all_cron_name

if __name__ == '__main__':
	arg = sys.argv[1:]
	if len(sys.argv) < 3: #检查参数
		print "arg wrong"
		exit()
	if arg[0][1:].lower() in get_all_cron_name():
		cron_name = "all"
	elif arg[0][1:].lower() == "all":
		cron_name = "all"
	else:
		print "cron name is wrong!"
		exit()

	action_list = ["start","restart","stop","status"]
	if arg[1].lower() in action_list:#检查行为
		run(cron_name,arg[1].lower())
	else:
		print "arg is wrong!"
		exit()