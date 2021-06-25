# Linux 网络

## 虚拟网络

![](https://img2018.cnblogs.com/blog/431521/201903/431521-20190308112809094-593909112.png)

> Linux 虚拟网络的背后都是由一个个的虚拟设备构成的。虚拟化技术没出现之前，计算机网络系统都只包含物理的网卡设备，通过网卡适配器，线缆介质，连接外部网络，构成庞大的 Internet。

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
