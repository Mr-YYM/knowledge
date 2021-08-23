# glusterfs

glusterfs 是一个分布式文件系统，可以把存储的文件，分散在不同的机器上。

> GlusterFS is a scalable network filesystem suitable for data-intensive tasks such as cloud storage and media streaming. 

## 安装指南

### 00. 准备机器

gluster 不建议把直接把数据放在与系统相同的目录下，因此建议每台机器都挂载一块新的硬盘专门用于 gluster 存储使用。

准备三台机器，分别进行分区操作与 `/etc/hosts` 的设置

- 分区

    ```shell
    fdisk /dev/sdb  # 给硬盘分区
    mkfs.xfs /dev/sdb1  # 格式化分区
    echo "/dev/sdb1 /gluster-data xfs defaults 0 0" >> /etc/fstab  # 挂载信息写入 fstab，开机自动挂载
    mount -a  # 启用刚刚的配置
    ```

- 配置 hosts

    ```ini
    node-01 192.168.217.129
    node-02 192.168.217.130
    node-03 192.168.217.131
    ```

### 安装 gluster

三台机器分别执行

```shell
# 安装源信息
yum install -y centos-release-gluster
# 安装
yum install -y glusterfs glusterfs-server glusterfs-fuse
# 启动
systemctl enable glusterd.service
systemctl start glusterd.service
```

### 配置集群

```shell
mkdir /gluster-data/data
# 添加集群机器
gluster peer probe node-01
gluster peer probe node-02
gluster peer probe node-03
# 创建 volume
gluster volume create test node-01:/gluster-data/data node-02:/gluster-data/data node-03:/gluster-data/data
# 挂载
mkdir /test
mount.glusterfs node-01:test /test
```
