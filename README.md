python-cron
===========
定时任务执行

功能：
1. 能够定时执行某个命令行，以秒为单位
1. 暂时没想到。。。。总之就是定时执行

使用方法：
1. 配置json，详细配置方法请参考config/config.json
1. python cron.py -all start
   python cron.py -某个任务名称 start
1. 成功执行
1. 如果执行的命令有返回值，就会产生日志在log下，命名的方式为`/log/任务名称/access_log.txt`

注意事项：
1. pid文件是用来记录守护进程的运行状况的，请勿手动删除

其他：
1. 使用了[python-daemon](https://github.com/serverdensity/python-daemon)，感谢。