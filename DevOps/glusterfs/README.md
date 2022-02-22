# GlusterFS

计算机通过硬盘来存储数据，随着信息数量的增长，单个硬盘的大小增长跟不上人类数据量的增长。因此诞生了分布式存储的概念。

所谓分布式，就是把数据分散存储在多个硬盘上。从宏观角度看，这是一块容量极大的硬盘，实际上由多块硬盘组成。（把多个服务的磁盘融合成一个单一磁盘）

NFS Network File System。是分布式的其中一种实现方式，它通过网络来传输数据。

> GlusterFS is a scalable network filesystem suitable for data-intensive tasks such as cloud storage and media streaming. 

## 介绍

Gluster 是一个开源的分布式文件系统。

> Gluster is a scalable, distributed file system that aggregates disk storage resources from multiple servers into a single global namespace.

### 架构

在 gluster 文件系统中卷 volume 是底层 brick 的集合，几乎所有操作都是在卷层面进行的。

- 分布式GlusterFS卷(Distributed GlusterFS Volume)

  - Discributed GlusterFS Volume就是纯粹的文件打散存储， **没有任何数据冗余** 所以这种分布式卷只提供了规模化和性能提升优点，存储卷中任何一个brick故障都会导致数据丢失。

  - ```shell
    gluster volume create test-volume server1:/exp1 server2:/exp2 server3:/exp3 server4:/exp4
    gluster volume info
    Volume Name: test-volume
    Type: Distribute
    Status: Created
    Number of Bricks: 4
    Transport-type: tcp
    Bricks:
    Brick1: server1:/exp1
    Brick2: server2:/exp2
    Brick3: server3:/exp3
    Brick4: server4:/exp4
    ```

  <img src="https://cloud-atlas.readthedocs.io/zh_CN/latest/_images/distributed_gluster_volume.png" style="zoom: 67%;" />

- GlusterFS复制卷(Replicated GlusterFS Volume)

  - GlusterFS复制卷解决了纯分布式卷的数据丢失风险。在所有的bricks上，明确指定了数据需要维护的副本数量W。在存储卷的副本数量可以在创建卷的时候由客户端决定。

  - 当创建卷时候，需要确保bricks的数量是集群卷配置的副本数量的整数倍。

  - ```shell
    gluster volume create test-volume replica 3 transport tcp \
          server1:/exp1 server2:/exp2 server3:/exp3
    ```

  <img src="https://cloud-atlas.readthedocs.io/zh_CN/latest/_images/replicated_gluster_volume.png" style="zoom:67%;" />

### 

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
