# Python

## 介绍

python is good

## 安装

### CentOS

CentOS 默认的源只更新到 3.6 版本，安装最新需要手动编译

```shell
# 下载源码包
wget  https://registry.npmmirror.com/-/binary/python/3.10.2/Python-3.10.2.tgz
tar zxvf Python-3.10.2.tgz
cd Python-3.10.2/

# 依赖
yum -y groupinstall "Development Tools"
yum install -y epel-release
yum -y install bzip2-devel libffi-devel
yum install -y openssl11-devel
# gcc 参考 https://www.cnblogs.com/jixiaohua/p/11732225.html

# 编译安装
./configure --enable-optimizations --with-ensurepip=install
make -j 8

```

