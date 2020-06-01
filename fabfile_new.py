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
    'ubuntu@10.10.10.54:22',
    'ubuntu@10.10.10.55:22',
    'ubuntu@10.10.10.56:22',
    'ubuntu@10.10.10.57:22',
    'ubuntu@10.10.10.58:22',
    'ubuntu@10.10.10.59:22',
    'ubuntu@10.10.10.60:22',
    'ubuntu@10.10.10.61:22',
    'ubuntu@10.10.10.62:22',
    'ubuntu@10.10.10.63:22',
    'ubuntu@10.10.10.64:22',
    'ubuntu@10.10.10.65:22',
    'ubuntu@10.10.10.66:22',
    'ubuntu@10.10.10.67:22',
    'ubuntu@10.10.10.68:22',
    'ubuntu@10.10.10.69:22',
    'ubuntu@10.10.11.54:22',
    'ubuntu@10.10.11.55:22',
    'ubuntu@10.10.11.56:22',
    'ubuntu@10.10.11.57:22',
    'ubuntu@10.10.11.58:22',
    'ubuntu@10.10.11.59:22',
    'ubuntu@10.10.11.60:22',
    'ubuntu@10.10.11.61:22',
    'ubuntu@10.10.11.62:22',
    'ubuntu@10.10.11.63:22',
    'ubuntu@10.10.11.64:22',
    'ubuntu@10.10.11.65:22',
    'ubuntu@10.10.11.66:22',
    'ubuntu@10.10.11.67:22',
    'ubuntu@10.10.11.68:22',
    'ubuntu@10.10.11.69:22'
}

# 定义需要远程的服务器的密码
env.passwords = {
    'ubuntu@10.10.10.54:22':'123456',
    'ubuntu@10.10.10.55:22':'123456',
    'ubuntu@10.10.10.56:22':'123456',
    'ubuntu@10.10.10.57:22':'123456',
    'ubuntu@10.10.10.58:22':'123456',
    'ubuntu@10.10.10.59:22':'123456',
    'ubuntu@10.10.10.60:22':'123456',
    'ubuntu@10.10.10.61:22':'123456',
    'ubuntu@10.10.10.62:22':'123456',
    'ubuntu@10.10.10.63:22':'123456',
    'ubuntu@10.10.10.64:22':'123456',
    'ubuntu@10.10.10.65:22':'123456',
    'ubuntu@10.10.10.66:22':'123456',
    'ubuntu@10.10.10.67:22':'123456',
    'ubuntu@10.10.10.68:22':'123456',
    'ubuntu@10.10.10.69:22':'123456',
    'ubuntu@10.10.11.54:22':'123456',
    'ubuntu@10.10.11.55:22':'123456',
    'ubuntu@10.10.11.56:22':'123456',
    'ubuntu@10.10.11.57:22':'123456',
    'ubuntu@10.10.11.58:22':'123456',
    'ubuntu@10.10.11.59:22':'123456',
    'ubuntu@10.10.11.60:22':'123456',
    'ubuntu@10.10.11.61:22':'123456',
    'ubuntu@10.10.11.62:22':'123456',
    'ubuntu@10.10.11.63:22':'123456',
    'ubuntu@10.10.11.64:22':'123456',
    'ubuntu@10.10.11.65:22':'123456',
    'ubuntu@10.10.11.66:22':'123456',
    'ubuntu@10.10.11.67:22':'123456',
    'ubuntu@10.10.11.68:22':'123456',
    'ubuntu@10.10.11.69:22':'123456'
}

# 将服务器进行分组
env.roledefs = {
    'prod_master':['ubuntu@10.10.11.54:22','ubuntu@10.10.11.55:22','ubuntu@10.10.11.56:22'],
    'prod_slave':['ubuntu@10.10.11.57:22','ubuntu@10.10.11.58:22','ubuntu@10.10.11.59:22','ubuntu@10.10.11.60:22'],
    'prod_gateway':['ubuntu@10.10.11.61:22','ubuntu@10.10.11.62:22'],
    'prod_service':['ubuntu@10.10.11.63:22','ubuntu@10.10.11.64:22','ubuntu@10.10.11.65:22','ubuntu@10.10.11.66:22','ubuntu@10.10.11.67:22','ubuntu@10.10.11.68:22','ubuntu@10.10.11.69:22'],
    'qa_master':['ubuntu@10.10.10.54:22','ubuntu@10.10.10.55:22','ubuntu@10.10.10.56:22'],
    'qa_slave':['ubuntu@10.10.10.57:22','ubuntu@10.10.10.58:22','ubuntu@10.10.10.59:22','ubuntu@10.10.10.60:22'],
    'qa_gateway':['ubuntu@10.10.10.61:22','ubuntu@10.10.10.62:22'],
    'qa_service':['ubuntu@10.10.10.63:22','ubuntu@10.10.10.64:22','ubuntu@10.10.10.65:22','ubuntu@10.10.10.66:22','ubuntu@10.10.10.67:22','ubuntu@10.10.10.68:22','ubuntu@10.10.10.69:22']
}

# 在指定的分组执行命令
@roles('prod_master','prod_slave','prod_gateway','prod_service','qa_master','qa_slave','qa_gateway','qa_service')
def hostname():
    run('hostname')

@roles('qa_master','qa_slave','qa_gateway','qa_service')
def del_exitdocker():
    sudo("for i in `docker ps -a | grep Exited | awk '{print $1}'`;do docker rm $i;done")

@roles('prod_master','prod_slave','prod_gateway','prod_service')
def echo():
    sudo("for i in `docker ps -a | grep Exited | awk '{print $1}'`;do docker rm $i;done")
