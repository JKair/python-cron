# -*- coding:utf-8 -*-
import os,sys,time

def cur_file_dir():
    """
    获取当前绝对路径
    """
    path = sys.path[0]
    if os.path.isdir(path):
        return path+"/"
    elif os.path.isfile(path):
        return os.path.dirname(path)+"/"

"""write_file
往文件里面写东西
Args:
    name str 这项任务的名称
    log_type  str 日志类别
    content str 需要写进日志的名称
"""
def write_file(name,log_type,content):
    strtime = "[" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + "]"
    content = strtime + " " + content + "\n"
    log_path = cur_file_dir() + "log/" + name + "/"
    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    log_name =  log_path + log_type + "_log.txt"
    f = open(log_name,"a")
    f.write(content)
    f.close()

def write_error_log(name,content):
    """写错误日志"""
    write_file(name,"error",content)

def write_access_log(name,content):
    """写成功运行日志"""
    write_file(name,"access",content)