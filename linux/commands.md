# date

格式化对照表

| 参数 |               作用               |
| :--: | :------------------------------: |
|  %S  |           秒（00～59）           |
|  %M  |           分钟（00～59           |
|  %H  |          小时（00～23）          |
|  %I  |          小时（00～12）          |
|  %m  |           月份（1~12）           |
|  %p  |           显示出AM或PM           |
|  %a  |  缩写的工作日名称（例如：Sun）   |
|  %A  | 完整的工作日名称（例如：Sunday） |
|  %b  |   缩写的月份名称（例如：Jan）    |
|  %B  | 完整的月份名称（例如：January）  |
|  %q  |           季度（1~4）            |
|  %y  |       简写年份（例如：20）       |
|  %Y  |      完整年份（例如：2020）      |
|  %d  |          本月中的第几天          |
|  %j  |          今年中的第几天          |
|  %n  |    换行符（相当于按下回车键）    |
|  %t  |     跳格（相当于按下Tab键）      |

```shell
date "+%Y-%m-%d %H:%M:%S"
```



# lsof

> ls open files

```shell
# 查看pid所属进程打开文件的信息
# 查看文件使用情况
lsof /file/path

# 递归查看目录下文件的使用信息
lsof +D /dir/path

# 查看某个用户打开的文件信息
lsof -u username
lsof -u username -c command

# 查看某个命令（应用程序）所打开的文件信息
lsof -c command
lsof -c command1 -c command2

# 查看pid所属进程打开文件的信息
lsof -p pid

# 查找使用端口的进程
lsof -i:3366

# ...
lsof -i tcp:3366

# ...
lsof -i udp:3366

# 显示端口号
lsof -i -P

# 列出所有文件描述符为fdnumber的信息
lsof -d fdnumber

# -R 列出父进程标识符-PPID
lsof -R

# list uer is not kaige
lsof -u "^kaige"
```



**参考链接**

https://man.linuxde.net/lsof



# grep 

> global search regular expression(RE) and print out the line


```shell

```

