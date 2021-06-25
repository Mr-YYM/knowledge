# Linux namespace

Namespace 是 Linux 内核中用于环境隔离的一种实现，实践中经常用到的「容器技术」的基础就是 Linux 内核提供的 Namespace 技术。

> Linux namespaces comprise some of the fundamental technologies behind most modern-day container implementations. 

Namespace 共分为以下几种类型:

- Mount: 隔离「挂载点」，实现「文件系统」的隔离。
- UTS: 隔离 hostname 和 domain name
- IPC: 隔离信号量、消息队列和共享内存
- PID: 进程号的隔离 => 同一系统内核，不同容器可以有相同的 PID
- Network: 网络接口隔离 => 每个容器都有各自的网络栈，可以理解为拥有各自的 IP 地址
- User: 用户隔离 => 每个容器都占有一套自己的用户体系


> At a high level, they allow for the isolation of global system resources between independent processes. For example, the PID namespace isolates the process ID number space. This means that two processes running on the same host can have the same PID!

## Network Namespace

使用 `ip` 命令可以轻松创建 `Network Namespace`

1. 创建 Namespace

    ```shell
    # 创建两个 Namespace
    ip netns add client
    ip netns add server
    ip netns list
    ```

2. 创建 `veth pair`[1] 连接两个 `Namespace`



## 参考

1. veth - Virtual Ethernet Device. [Linux Programmer's Manual: VETH(4)](https://man7.org/linux/man-pages/man4/veth.4.html)

    veth pair 相当于一条网线把两个设备连接起来

    >  The veth devices are virtual Ethernet devices.  They can act as
       tunnels between network namespaces to create a bridge to a
       physical network device in another namespace, but can also be
       used as standalone network devices.

    >  veth devices are always created in **interconnected pairs**.  A pair
       can be created using the command:
    >   
    >   `ip link add <p1-name> type veth peer name <p2-name>`
