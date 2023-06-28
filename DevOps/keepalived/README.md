# keepalived

keepalived 实现的功能如下:

以下示例以两台主机为例，主机 IP 分别为 192.168.31.10 和 192.168.31.11，我们的目标是在这两台主机上配置 keepalived，以实现虚拟 IP (VIP) 的高可用性。

0. **两台主机之间的关系：**

    ```shell
    +---------------------+   VIP: 192.168.31.100    +--------------------+
    |                     | <----------------------> |                    |
    |  Master             |     VRRP Protocol        |  Backup            |
    |  (Active)           |                          |  (Standby)         |
    | IP: 192.168.31.10   |                          | IP: 192.168.31.11  |
    +---------------------+                          +--------------------+
    ```

    在这个简单的字符图中，"Master" 主机是活动的，它具有虚拟 IP 地址（VIP: 192.168.31.100）。而 "Backup" 主机是备用的，它在等待接管 VIP。当 "Master" 主机发生故障时，"Backup" 主机将立即接管 VIP，保证了服务的高可用性。这两台主机通过 VRRP 协议进行通信，协调 VIP 的所有权。


## 简介

keepalived 是一款能帮助你实现高可用服务的开源工具。它主要通过创建一个虚拟 IP（VIP）来工作。可以这样理解：你有两台或更多的服务器，它们都运行着相同的服务。为了实现这些服务的高可用，你可以使用 keepalived 在其中一台服务器上创建一个 VIP，这台服务器我们称之为主服务器。所有的客户端连接都会到这个 VIP，实际上也就是连接到了主服务器。

keepalived 的聪明之处在于，它会不断检查主服务器的状态。如果主服务器出现故障，keepalived 就会把 VIP 快速迁移到另一台备用服务器上。这样，客户端就能无缝地继续他们的工作，他们甚至可能都没有察觉到后台服务器已经切换。

要实现这种高效的切换，keepalived 使用了一种名为 VRRP (Virtual Router Redundancy Protocol) 的协议。同时，它还利用了 ARP (Address Resolution Protocol) 协议来使得网络设备知道 VIP 已经迁移到了新的主机上。这种机制允许 keepalived 在故障发生时迅速切换服务器，使得服务保持高可用性。

## VRRP 协议

VRRP（Virtual Router Redundancy Protocol）即虚拟路由器冗余协议，是一种网络协议，用于创建一个虚拟的路由器，它由两台或更多的物理路由器组成。这些路由器共享一个虚拟IP地址。VRRP协议可以保证在物理路由器出现故障时，网络中的其他机器仍然可以通过这个虚拟IP地址进行通信。

在一组VRRP路由器中，有一个路由器被选为主路由器，其余的路由器作为备份。主路由器拥有和虚拟路由器相同的IP地址，并负责转发到虚拟路由器IP地址的数据包。如果主路由器出现故障，备份路由器之一将接管IP地址和相应的数据包转发任务。

VRRP协议是一种基于优先级的协议，每台参与的路由器都有一个配置的优先级。主路由器是优先级最高的路由器。如果两台或更多的路由器优先级相同，那么就会根据它们的物理IP地址来选择一个主路由器，IP地址高的成为主路由器。当主路由器出现故障时，优先级次高的路由器将会成为新的主路由器。

VRRP使用定期的广播消息来维持集群的状态，这个消息称为VRRP Advertisement。主路由器定期发送VRRP Advertisement消息，告诉备份路由器它还在正常工作。如果备份路由器在一段时间内没有收到这个消息，它们将开始进行新一轮的主路由器选举。

总的来说，VRRP协议通过虚拟路由器和主/备模式，保证了在物理路由器出现故障时，网络的正常通信不会受到影响。

> 路由器这个词听起来让人困惑，他不是配置在主机 VM 上的吗，怎么叫路由器呢，是不是这个协议设计之初是用在路由器上的。

是的，你的理解是正确的。VRRP（Virtual Router Redundancy Protocol）虽然名字中包含"路由器"，但这并不意味着它只能在物理路由器设备上使用。在计算机网络术语中，"路由器"常常被用来泛指任何执行路由功能的设备或软件，无论它们是物理设备还是虚拟设备。例如，一台运行着路由软件的服务器，也可以被称为路由器。

确实，VRRP在设计之初主要是为了在物理路由器设备上提供冗余。然而，随着虚拟化技术和云计算的发展，VRRP也被广泛用在虚拟环境中，包括虚拟机和容器。例如，Kubernetes中的keepalived插件就使用了VRRP协议，实现了在Kubernetes节点之间的IP地址冗余。

所以，在这里，当我们谈论"VRRP路由器"时，实际上是指执行了路由功能的任何实体，无论是物理设备、虚拟机，还是运行在容器中的软件。

### VRRP Advertisement消息

VRRP Advertisement消息是VRRP协议中最关键的消息类型。它由Master路由器周期性地发送，用于声明其对虚拟路由器的控制权，并告知其他路由器其优先级。它包含以下关键字段：

1. **Version**：VRRP协议的版本号。当前的版本是VRRPv3。

2. **Type**：消息的类型。对于VRRP Advertisement消息，此字段的值是1。

3. **Virtual Router ID (VRID)**：标识虚拟路由器的ID。此字段的值由管理员配置，并且在同一网络中必须是唯一的。

4. **Priority**：发送此消息的路由器的优先级。优先级的范围是0到255。优先级高的路由器更有可能成为Master。如果Master路由器宕机，具有次高优先级的路由器将接管Master的角色。

5. **Advertisement Interval**：发送VRRP Advertisement消息的间隔时间，单位是秒。这是Master路由器通知其活动状态的频率。

6. **Checksum**：消息的校验和，用于检测消息在传输过程中是否被损坏。

以上就是VRRP Advertisement消息的主要字段。这些字段提供了VRRP协议所需的所有信息，以协调多个路由器，并确定哪个路由器应成为Master，从而实现虚拟IP地址的高可用性。

> VRRP Advertisement消息工作在网络协议的第几层

VRRP (Virtual Router Redundancy Protocol) 是一个网络层协议。在网络协议中，VRRP通常在IP协议之上工作，但是它并不是传输层协议，因此，VRRP Advertisement 消息是工作在网络层。

## 简单的使用

以下示例以两台主机为例，主机 IP 分别为 192.168.31.10 和 192.168.31.11，我们的目标是在这两台主机上配置 keepalived，以实现虚拟 IP (VIP) 的高可用性。

0. **两台主机之间的关系：**

    ```shell
    +---------------------+   VIP: 192.168.31.100    +--------------------+
    |                     | <----------------------> |                    |
    |  Master             |     VRRP Protocol        |  Backup            |
    |  (Active)           |                          |  (Standby)         |
    | IP: 192.168.31.10   |                          | IP: 192.168.31.11  |
    +---------------------+                          +--------------------+
    ```

    在这个简单的字符图中，"Master" 主机是活动的，它具有虚拟 IP 地址（VIP: 192.168.31.100）。而 "Backup" 主机是备用的，它在等待接管 VIP。当 "Master" 主机发生故障时，"Backup" 主机将立即接管 VIP，保证了服务的高可用性。这两台主机通过 VRRP 协议进行通信，协调 VIP 的所有权。


1. **在两台主机上安装 keepalived**：

   对于大部分 Linux 发行版，你可以使用包管理器来安装 keepalived：

   在 Ubuntu 上:
   ```shell
   sudo apt-get install keepalived
   ```
   在 CentOS 上:
   ```shell
   sudo yum install keepalived
   ```

2. **在两台主机上配置 keepalived**：

   keepalived 的配置文件通常位于 `/etc/keepalived/keepalived.conf`。以下是两台主机的配置文件示例：

   **在 192.168.31.10 主机上（MASTER）**：

   ```shell
   vrrp_instance VI_1 {
       state MASTER
       interface eth0
       virtual_router_id 51
       priority 101
       advert_int 1
       authentication {
           auth_type PASS
           auth_pass 1111
       }
       virtual_ipaddress {
           192.168.31.100
       }
   }
   ```
   
   **在 192.168.31.11 主机上（BACKUP）**：

   ```shell
   vrrp_instance VI_1 {
       state BACKUP
       interface eth0
       virtual_router_id 51
       priority 100
       advert_int 1
       authentication {
           auth_type PASS
           auth_pass 1111
       }
       virtual_ipaddress {
           192.168.31.100
       }
   }
   ```
   
   在这里，`state` 参数定义了这台主机的角色，MASTER 或 BACKUP；`virtual_router_id` 定义了 VRRP 实例的 ID，同一个 VRRP 实例的这个值需要一致；`priority` 定义了 VRRP 优先级，数值越高优先级越高，MASTER 的优先级应该高于 BACKUP；`auth_type` 和 `auth_pass` 定义了 VRRP 实例的认证方式和密码，同一个 VRRP 实例的这个值也需要一致；`virtual_ipaddress` 定义了 VIP，同一个 VRRP 实例的这个值需要一致。

3. **在两台主机上启动 keepalived 服务**：

   配置完成后，你可以使用如下命令来启动 keepalived 服务：

   ```shell
   sudo systemctl start keepalived
   ```
   
   这样，两台主机就会开始运行 keepalived，并通过 VRRP 协议保持通讯，当 MASTER 主机不可用时，BACKUP 主机会接管 VIP，保证服务的可用性。