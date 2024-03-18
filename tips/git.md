# Git

Centos 安装 git 请使用源：https://packages.endpointdev.com/

## git 查看被删除的文件

要查看 Git 中被删除文件的内容，你可以使用 `git show` 命令。`git show` 命令允许你查看对象（比如提交、树、标签等）的信息，也可以用来查看被删除文件的最后状态。

首先，你需要找到包含该文件最后更改的提交的哈希值。可以使用下面的命令来查找该文件相关的最近的提交：

```bash
git log -n 1 -- vhost/servers/xxxx.conf
```

这个命令会显示出影响`vhost/servers/xxxx.conf`文件的最近一次提交的详细信息，包括提交哈希值。

找到提交哈希值后，使用以下命令查看被删除文件的内容：

```bash
git show <提交哈希值>:vhost/servers/xxxx.conf
```

请将`<提交哈希值>`替换为实际的哈希值。

这样，你就能看到在那次提交中`vhost/servers/xxxx.conf`文件的内容了。如果你只是想查看文件在被删除前的最后状态，而不关心是在哪次提交中被删除的，可以尝试使用下面的命令：

```bash
git show HEAD:vhost/servers/xxxx.conf
```

这个命令会显示出在最后一次提交时`vhost/servers/xxxx.conf`文件的内容，即在文件被删除之前的最后状态。不过，这种方法仅在文件最近一次提交之后未发生其他变更时有效。
