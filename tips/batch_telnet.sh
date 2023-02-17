#!/bin/bash

# 批量 telnet 脚本
# 定义变量，存放要连接的 IP 和端口号
hosts=(
   "192.168.1.1:7010"
   "192.168.1.1:7020"
   "192.168.1.1:7050"
)

# 遍历数组中的元素，执行 telnet
for host in "${hosts[@]}"
do
  ip=$(echo $host | cut -d':' -f1)
  port=$(echo $host | cut -d':' -f2)
  # 执行 telnet 操作
  if echo "" | telnet $ip $port | grep "Connected" > /dev/null; then
    echo "Success: ${ip}:${port}"
  else
    echo "Failed: ${ip}:${port}"
  fi
done