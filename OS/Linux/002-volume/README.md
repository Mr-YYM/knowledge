# Linux 存储


## 常用操作

- LVM 磁盘扩容

    首先挂载一块新磁盘

    ```shell
    # 扫描总线接口，把刚刚在 vcenter 添加的硬盘加载到系统中
    cd /sys/class/scsi_host/
    for h in *; do echo "- - -" > "${h}/scan"; done
    # 给新加的硬盘分区
    fdisk /dev/sdb
    ##### fdisk #####
    # 依次按下如下命令
    # 1. p: 查看分区
    # 2. n: 创建新分区。一路回车即可
    # 3. t: 选择分区类型，输入 8e，代表 Linux LVM
    # 4. p: 查看分区
    # 5. w: 写入操作
    #################
    # 创建 PV
    pvcreate /dev/sdb1
    # 扩充 VG
    vgextend centos /dev/sdb1
    # vgdisplay 查看 free 容量
    # 扩容 LV
    # 233 这个数字，这里填写 vgdisplay 查看到的 free 容量
    lvextend --extents +2333 --resizefs /dev/centos/root
    # 或者可以直接用百分比的方式
    lvextend -l +100%FREE /dev/centos/root --resizefs
    ```
