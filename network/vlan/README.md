# VLAN

在一个交换机（或者好几个）内，划分不同的逻辑网段，实现逻辑隔离。用来避免：

- 减少广播域大小，避免过度的广播。

## 知识点

### VLAN 之间的通信

VLAN 直接通信需要路由器，或者三层交换机的路由功能。

> gpt:如果你使用的是 三层交换机，你可以在三层交换机上直接配置 VLAN 间的路由：
> 
> 三层交换机可以在内部根据 IP 地址路由数据包，允许不同 VLAN 的设备直接通信，而不需要借助外部路由器。
> 
> 你只需要在三层交换机上创建 SVI（Switch Virtual Interface，交换虚拟接口） 或 路由接口，这些接口为每个 VLAN 分配一个 IP 地址，并在内部路由 VLAN 之间的流量。

> A VLAN interface, or switched virtual interface **(SVI)**, is a **Layer 3 interface** that is created to provide communication between VLANs.[1]

## 一些问题

### VLAN 是二层网络的事情，但是似乎又跟三层的IP地址有联系

...

### 「access 模式」 vs 「trunk 模式」

与电脑设备直连的端口用access模式，VLAN交换机之间互连，用trunk模式

## 参考

1. https://www.cisco.com/c/en/us/td/docs/switches/datacenter/sw/5_x/nx-os/layer2/configuration/guide/Cisco_Nexus_7000_Series_NX-OS_Layer_2_Switching_Configuration_Guide_Release_5-x_chapter4.html
