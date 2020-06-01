# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.utils import abort
from fabric.colors import *

# env.hosts = ['127.0.0.1']
# env.port = 22
# env.user = 'ubuntu'
# env.password = 'Aa123456!'

# 定义需要远程的服务器和端口
env.hosts = {
    'root@192.168.201.160:22',
    'root@192.168.201.161:22',
    'root@192.168.201.162:22',
    'root@192.168.201.163:22'
}

# 定义需要远程的服务器的密码
env.passwords = {
    'root@192.168.201.160:22':'1qaz2wsx#EDC',
    'root@192.168.201.161:22':'1qaz2wsx#EDC',
    'root@192.168.201.162:22':'1qaz2wsx#EDC',
    'root@192.168.201.163:22':'1qaz2wsx#EDC'
}

# 将服务器进行分组
env.roledefs = {
    'cmq_before':['root@192.168.201.163:22'],
    'cmq_rear':['root@192.168.201.160:22','root@192.168.201.161:22','root@192.168.201.162:22']
}

# 在指定的分组执行命令
@roles('cmq_before')
def hostname():
    run('hostname')

@roles('cmq_rear')
def netstat():
    run('netstat -anpt')
