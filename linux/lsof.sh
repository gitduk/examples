#!/bin/bash
#=============================================================
# File Name: lsof.sh
# Author: dongkai
# email: wdkany@qq.com
# Created Time: Sat 24 Oct 2020 03:33:02 PM CST
#=============================================================
G='[0;32m' # green color
Y='[1;33m' # yellow color
N='[0m' # No Color


# 列出所有打开的文件(万物皆文件)
lsof

# 参数介绍
lsof /file/path         # 查看文件使用情况
lsof +D /dir/path       # 递归查看目录下文件的使用信息
lsof -u username        # 查看某个用户打开的文件 信息                       lsof -u username -c command
lsof -c command         # 查看某个命令（应用程序）所打开的文件信息          lsof -c command1 -c command2
lsof -p pid             # 查看pid所属进程打开文件的信息
lsof -i:3366            # 查找使用端口的进程
lsof -i tcp:3366        # ...
lsof -i udp:3366        # ...
lsof -i -P              # 显示端口号
lsof -d fdnumber        # 列出所有文件描述符为fdnumber的信息
lsof -R                 # -R 列出父进程标识符-PPID

lsof -u "^kaige"        # list uer is not kaige


# 参考链接
# https://man.linuxde.net/lsof




