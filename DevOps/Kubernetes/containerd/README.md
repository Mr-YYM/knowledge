# containerd

最新版本的 k8s 已经不再支持 Docker 作为运行时，containerd 是最常用替代方案


## 常见问题

- 配置「代理镜像」和「insecure registry」

文档：
https://github.com/containerd/containerd/blob/main/docs/hosts.md 

首先在顶层配置文件中，指定 `host configuration files located` 的目录 `/etc/containerd/certs.d`：

```toml
# /etc/containerd/config.toml
version = 2

[plugins."io.containerd.grpc.v1.cri".registry]
   config_path = "/etc/containerd/certs.d"
```

这个配置有一个**十分啃爹**的地方 ctr 命令是不去看的，只有 crictl 才生效。我调了大半天发现不生效，后来换作 crictl 生效了，才意识到这问题。

https://stackoverflow.com/questions/65681045/adding-insecure-registry-in-containerd

<img width="777" alt="Google Chrome 2025-03-09 19 40 00" src="https://github.com/user-attachments/assets/5ed4627e-c456-497f-87fa-8b93c6386a23" />

**registry 代理镜像服务**

对于 ctr 命令，直接像文档那样 `ctr images pull --hosts-dir "/etc/containerd/certs.d"` 就能 pull 了。

对于 crictl 或 k8s.

http://127.0.0.1:5000 是我自己搭建的本地缓存镜像服务（ 能通过梯子代理又能缓存重复的镜像拉取，十分好用， `docker run --name=cache -d --restart=always --network=hub-cache -v hub-cache:/var/lib/registry -p 5000:5000 -e HTTP_PROXY=http://192.168.57.1:7890 -e HTTPS_PROXY=http://192.168.57.1:7890 -e REGISTRY_PROXY_REMOTEURL=https://registry-1.docker.io registry:2` ）

```shell
mkdir -p /etc/containerd/certs.d/docker.io/
tee /etc/containerd/certs.d/docker.io/hosts.toml <<EOF
server = "https://docker.io"

[host."http://127.0.0.1:5000"]
  capabilities = ["pull", "resolve"]
EOF
```

**insecure registry**

看文档 Specifying the Configuration Directory 和 Setup Default Mirror for All Registries 部分

mkdir /etc/containerd/certs.d/_default

```toml
# /etc/containerd/certs.d/_default/hosts.toml
server = "http://172.31.0.36"

[host."http://172.31.0.36"]
  skip_verify = true
```

以上适用于 crictl 或者 k8s 拉镜像

对于  ctr 命令

ctr image pull --plain-http <image> 即可

**最后记得重启**

```shell
sudo systemctl restart containerd
```
