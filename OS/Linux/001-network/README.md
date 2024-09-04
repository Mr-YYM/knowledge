# Linux 网络

## 虚拟网络

![](https://img2018.cnblogs.com/blog/431521/201903/431521-20190308112809094-593909112.png)

> Linux 虚拟网络的背后都是由一个个的虚拟设备构成的。虚拟化技术没出现之前，计算机网络系统都只包含物理的网卡设备，通过网卡适配器，线缆介质，连接外部网络，构成庞大的 Internet。
>

### veth

Linux 的虚拟以太网设备，通常是一对。

```shell
ip link add <p1-name> type veth peer name <p2-name>
```

> The veth devices are virtual Ethernet devices.  They can act as
> tunnels between network namespaces to create a bridge to a
> physical network device in another namespace, but can also be
> used as standalone network devices.[2]
>
> veth devices are always created in interconnected pairs.
>
> Packets transmitted on one device in the pair are immediately
> received on the other device.  When either device is down, the
> link state of the pair is down.

### network namespace

network namespace 是 Linux 系统实现资源隔离的其中一个 namespace。用户网络资源的隔离。

namespace 之间通过 veth pair 相连。

> A virtual network (veth(4)) device pair provides a pipe-like
> abstraction that can be used to create tunnels between network
> namespaces, and can be used to create a bridge to a physical
> network device in another namespace. 

参考 4，manual 手册，关于 namespace 的介绍，仔细看。

### tap/tun

tap/tun 是一套虚拟的网络设备，负责虚拟网络的 「packet reception」并把「packet」传输到对应的「用户空间」程序。

> TUN/TAP provides packet reception and transmission for user space programs. 
  It can be seen as a simple Point-to-Point or Ethernet device, which,
  instead of receiving packets from physical media, receives them from 
  user space program and instead of sending packets via physical media 
  writes them to the user space program. 

tap 处理二层网络流量，随后 tap 处理第三层的网络流量。

## 参考

1. [一文总结 Linux 虚拟网络设备 eth, tap/tun, veth-pair](https://www.cnblogs.com/bakari/p/10494773.html)
2. https://man7.org/linux/man-pages/man4/veth.4.html
3. [容器技术的基石： namespace 发展历史及细节](https://moelove.info/2021/12/10/%E6%90%9E%E6%87%82%E5%AE%B9%E5%99%A8%E6%8A%80%E6%9C%AF%E7%9A%84%E5%9F%BA%E7%9F%B3-namespace-%E4%B8%8A/)
4. https://man7.org/linux/man-pages/man7/network_namespaces.7.html
