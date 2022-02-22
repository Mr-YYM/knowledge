

# GluserFS 实践



## 搭建 GlusterFS 卷

### 01. 创建 LVM 分区

> 32 位系统，一个逻辑卷（Logic Volume）最多只能包含65536个PE（Physical Extent），所以一个 PE 的大小就决定了逻辑卷的最大容量，4 MB 的PE决定了单个逻辑卷最大容量为 256 GB，若希望使用大于256G的逻辑卷，则创建卷组时需要指定更大的PE。在Red Hat Enterprise Linux AS 4中PE大小范围为8 KB 到 16GB，并且必须总是 2 的倍数。 例如，如果希望使用 64 MB 的PE创建卷组，这样逻辑卷最大容量就可以为4 TB，命令如下: 
>
> \# vgcreate － 64MB lvmdisk /dev/sdb1 /dev/sdc1
>
> \-----------------------------------
>
> LVM中的PV、VG、LV、PE、LE的关系及简单LVM配置
>
> https://blog.51cto.com/ponyjia/1680969
>
> 不过，在 CentOS 6.x 以后，由于直接使用lvm2的各项格式功能，以及系统转为 64 位，因此这个限制已经不存在了。

1、创建 lvm 分区，创建逻辑卷，格式化 xfs 格式。

```shell
fdisk /dev/sdb

# 创建 Physical Volume
pvcreate /dev/sdb1

lvmdiskscan # List devices that may be used as physical volumes

# 创建 Volume Group
vgcreate gfsdata /dev/sdb1

# 创建 Logic Volume
# -L ：后面接容量，容量的单位可以是M,G,T 等，
# -l ：后面可以接PE 的『个数』
lvcreate --name gfslv -l 100%FREE gfsdata

# 格式化分区
mkfs.xfs /dev/gfsdata/gfslv

# 挂载
mount /dev/gfsdata/gfslv /gfsdata  && echo "/dev/gfsdata/gfslv /gfsdata xfs defaults 0 0" >> /etc/fstab*
mount -a
```



### 02. 安装 Gluster

- 配置源

  > https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/3.6.9/CentOS/epel-7/x86_64/glusterfs-server-3.6.9-1.el7.x86_64.rpm
  
  ```shell
  # 老版本 gluster 源 3.6.9-1
  
  [glusterfs-epel]
  name=GlusterFS is a clustered file-system capable of scaling to several petabytes.
  baseurl=https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/LATEST/EPEL.repo/epel-$releasever/$basearch/
  enabled=1
  skip_if_unavailable=1
  gpgcheck=1
  gpgkey=https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/LATEST/EPEL.repo/rsa.pub
  
  [glusterfs-noarch-epel]
  name=GlusterFS is a clustered file-system capable of scaling to several petabytes.
  baseurl=https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/LATEST/EPEL.repo/epel-$releasever/noarch
  enabled=1
  skip_if_unavailable=1
  gpgcheck=1
  gpgkey=https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/LATEST/EPEL.repo/rsa.pub
  
  [glusterfs-source-epel]
  name=GlusterFS is a clustered file-system capable of scaling to several petabytes. - Source
  baseurl=https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/LATEST/EPEL.repo/epel-$releasever/SRPMS
  enabled=0
  skip_if_unavailable=1
  gpgcheck=1
  gpgkey=https://download.gluster.org/pub/gluster/glusterfs/old-releases/3.6/LATEST/EPEL.repo/rsa.pub
  ```

- 安装

  ```shell
  # 安装，确认版本正确
  yum install glusterfs-server
  # 启动
  systemctl start glusterd && systemctl enable glusterd
  # 确认版本 glusterfs 3.6.9 built on Feb 29 2016 22:38:34
  glusterd --version
  ```

### 03. 配置 Gluster

```shell
# 配置集群机器
gluster peer probe 10.9.68.232
gluster peer probe 10.9.68.233

# 查看集群情况
gluster pool list 

# 创建 volume
gluster volume create yym-volume replica 3 transport tcp 10.9.68.231:/gfsdata/brick2 10.9.68.232:/gfsdata/brick2 10.9.68.233:/gfsdata/brick2

# 启动 volume
gluster volume start yym-volume

# 查看 volume 情况
gluster volume status yym-volume

```



### 04. 设置挂载

```shell
# 设置挂载
mkdir /mnt/gfs_yym
echo "10.9.68.231:yym-volume       /mnt/gfs_yym  glusterfs       defaults        0 0" >> /etc/fstab
mount -a
```





## LVM 扩容

扩容前

- 停止 volume

  ```shell
  gluster volume stop yym-volume
  # Stopping volume will make its data inaccessible. Do you want to continue? (y/n) y
  # volume stop: yym-volume: success
  # 挂载点：ls: cannot open directory .: Transport endpoint is not connected
  ```

- 挂载一个新盘，lsblk 查看

  ```shell
  [root@10 ~]# lsblk
  NAME              MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
  ...
  sdf                 8:32   0   100G  0 disk
  ```

在每台机器上分别执行以下操作

- fdisk 分区

  ```shell
  > fdisk /dev/sdf
  ...
  
  # 1. 查看分区情况
  Command (m for help): p
  
  Disk /dev/sdf: 107.4 GB, 107374182400 bytes, 209715200 sectors
  Units = sectors of 1 * 512 = 512 bytes
  Sector size (logical/physical): 512 bytes / 512 bytes
  I/O size (minimum/optimal): 512 bytes / 512 bytes
  Disk label type: dos
  Disk identifier: 0xca197fb7
  
     Device Boot      Start         End      Blocks   Id  System
  
  # 2. 创建新的分区, n, 然后一路回车即可
  Command (m for help): n
  Partition type:
     p   primary (0 primary, 0 extended, 4 free)
     e   extended
  Select (default p):
  Using default response p
  Partition number (1-4, default 1):
  First sector (2048-209715199, default 2048):
  Using default value 2048
  Last sector, +sectors or +size{K,M,G} (2048-209715199, default 209715199):
  Using default value 209715199
  Partition 1 of type Linux and of size 100 GiB is set
  
  # 3. 查看分区情况
  Command (m for help): p
  ...
     Device Boot      Start         End      Blocks   Id  System
  /dev/sdf1            2048   209715199   104856576   83  Linux
  
  # 4. t 选择 8e 类型
  Command (m for help): t
  Selected partition 1
  Hex code (type L to list all codes): 8e
  Changed type of partition 'Linux' to 'Linux LVM'
  
  # 5. 写入
  Command (m for help): w
  The partition table has been altered!
  
  Calling ioctl() to re-read partition table.
  Syncing disks.
  
  # 再次查看
  [root@10 ~]# fdisk -l /dev/sdf
  ...
     Device Boot      Start         End      Blocks   Id  System
  /dev/sdf1            2048   209715199   104856576   8e  Linux LVM
  ```

- 扩展 lv

  ```shell
  pvcreate /dev/sdf1
  vgextend gfsdata /dev/sdf1
  
  #  --resizefs 或者再执行一句 xfs_growfs /dev/gfsdata/gfslv
  lvextend --extents +100%FREE --resizefs /dev/gfsdata/gfslv
  ```



扩容完成后

- 启动 volume

  ```shell
  gluster volume start yym-volume
  ```

  