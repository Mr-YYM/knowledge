# Linux 包管理

## apt

apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器。

apt 命令提供了查找、安装、升级、删除某一个、一组甚至全部软件包的命令[1]

### 配置说明

- 配置文件位置: `/etc/apt/`

- 安装 unstable 包:

    ```shell
    sed -i '2s/buster/unstable/' sources.list
    apt update
    apt install [something]
    ```

### important tips

- 查看 apt 包信息的官网: https://tracker.debian.org/


## 参考

1. [Linux apt 命令| 菜鸟教程](https://www.runoob.com/linux/linux-comm-apt.htm)
