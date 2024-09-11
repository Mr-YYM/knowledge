# containerd

最新版本的 k8s 已经不再支持 Docker 作为运行时，containerd 是最常用替代方案


## 常见问题

- 配置 insecure registry

文档：
https://github.com/containerd/containerd/blob/main/docs/hosts.md 

Specifying the Configuration Directory 和 Setup Default Mirror for All Registries 部分


```toml
# /etc/containerd/config.toml
version = 2

[plugins."io.containerd.grpc.v1.cri".registry]
   config_path = "/etc/containerd/certs.d"
```

mkdir /etc/containerd/certs.d/_default

```toml
# /etc/containerd/certs.d/_default/hosts.toml
server = "http://172.31.0.36"

[host."http://172.31.0.36"]
  skip_verify = true
```

sudo systemctl restart containerd


以上适用于 crictl 或者 k8s 拉镜像

对于  ctr 命令

ctr image pull --plain-http <image> 即可
https://stackoverflow.com/questions/65681045/adding-insecure-registry-in-containerd
