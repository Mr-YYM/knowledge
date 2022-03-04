# StackStorm

StackStorm 是一个开源自动化平台。能实现以下功能


```shell
root@6ac9f2a09ab9:/opt/stackstorm# st2 action list --pack=core
+---------------------+------+--------------------------------------------------------------------------------+
| ref                 | pack | description                                                                    |
+---------------------+------+--------------------------------------------------------------------------------+
| core.announcement   | core | Action that broadcasts the announcement to all stream consumers.               |
| core.ask            | core | Action for initiating an Inquiry (usually in a workflow)                       |
| core.echo           | core | Action that executes the Linux echo command on the localhost.                  |
| core.error          | core | Action that executes the Linux echo command (to stderr) on the localhost.      |
| core.http           | core | Action that performs an http request.                                          |
| core.inject_trigger | core | Action which injects a new trigger in the system.                              |
| core.local          | core | Action that executes an arbitrary Linux command on the localhost.              |
| core.local_sudo     | core | Action that executes an arbitrary Linux command on the localhost.              |
| core.noop           | core | Action that does nothing                                                       |
| core.pause          | core | Action to pause current thread of workflow/sub-workflow.                       |
| core.remote         | core | Action to execute arbitrary linux command remotely.                            |
| core.remote_sudo    | core | Action to execute arbitrary linux command remotely.                            |
| core.sendmail       | core | This sends an email                                                            |
| core.uuid           | core | Generate a new UUID (default uuid4)                                            |
| core.winrm_cmd      | core | Action to execute arbitrary Windows Command Prompt command remotely via WinRM. |
| core.winrm_ps_cmd   | core | Action to execute arbitrary Windows PowerShell command remotely via WinRM.     |
+---------------------+------+--------------------------------------------------------------------------------+
```

## 安装

使用 docker 安装最方便

https://docs.stackstorm.com/install/docker.html

```shell
git clone https://github.com/stackstorm/st2-docker
cd st2-docker
echo 'export ST2_EXPOSE_HTTP=0.0.0.0:80' > .env
docker-compose up -d
```

## 使用

https://docs.stackstorm.com/start.html


```shell
# st2 命令需要进入到 st2client 容器中才能用
docker-compose exec st2client bash

# 批量执行命令
st2 run --tail core.remote hosts='192.168.1.231,192.168.1.232' username='root' password='xxx' -- gluster pool list
```
