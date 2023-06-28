# keepalived

## 简介

keepalived 是一款能帮助你实现高可用服务的开源工具。它主要通过创建一个虚拟 IP（VIP）来工作。可以这样理解：你有两台或更多的服务器，它们都运行着相同的服务。为了实现这些服务的高可用，你可以使用 keepalived 在其中一台服务器上创建一个 VIP，这台服务器我们称之为主服务器。所有的客户端连接都会到这个 VIP，实际上也就是连接到了主服务器。

keepalived 的聪明之处在于，它会不断检查主服务器的状态。如果主服务器出现故障，keepalived 就会把 VIP 快速迁移到另一台备用服务器上。这样，客户端就能无缝地继续他们的工作，他们甚至可能都没有察觉到后台服务器已经切换。

要实现这种高效的切换，keepalived 使用了一种名为 VRRP (Virtual Router Redundancy Protocol) 的协议。同时，它还利用了 ARP (Address Resolution Protocol) 协议来使得网络设备知道 VIP 已经迁移到了新的主机上。这种机制允许 keepalived 在故障发生时迅速切换服务器，使得服务保持高可用性。

## VRRP 协议

VRRP (Virtual Router Redundancy Protocol) 是一种用于实现网络路径冗余的协议，它能够保证在主路由器出现问题时，备用路由器能够立即接管，保证网络的连续性。在 keepalived 中，通过 VRRP 协议，可以实现一个虚拟路由器实例，这个实例的 IP 地址是由一个或者多个 keepalived 节点共享的。其中一个 keepalived 节点作为 MASTER，其他的节点作为 BACKUP。当 MASTER 节点出现故障时，BACKUP 节点会接管虚拟路由器的 IP，保证服务的可用性。

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