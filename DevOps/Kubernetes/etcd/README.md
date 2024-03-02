# ETCD

## etcd 的证书

### 两种证书之间的区别

`ETCD_CERT`（`ETCD_CERT_FILE`）和 `ETCD_PEER_CERT`（`ETCD_PEER_CERT_FILE`）两个证书虽然都是用于TLS/SSL加密通信的，但它们在 `etcd` 集群中扮演着不同的角色，分别用于不同的通信场景：

1. **`ETCD_CERT_FILE`（客户端到服务器证书）**:
   - **用途**：这个证书用于客户端与 `etcd` 服务器之间的加密通信。
   - **场景**：当一个客户端（如 Kubernetes API 服务器、etcdctl 命令行工具等）尝试连接到 `etcd` 服务器时，服务器会提供这个证书以证明其身份。客户端使用这个证书来验证它连接的服务器是合法的。
   - **安全目的**：确保客户端到服务器通信的安全性和数据加密，防止中间人攻击。

2. **`ETCD_PEER_CERT_FILE`（对等节点间证书）**:
   - **用途**：这个证书用于 `etcd` 集群内部节点之间的加密通信。
   - **场景**：`etcd` 集群由多个节点组成，为了保持数据的一致性，这些节点需要相互通信（称为对等通信）。在这种通信中，节点之间使用 `ETCD_PEER_CERT_FILE` 指定的证书来证明各自的身份。
   - **安全目的**：确保集群内节点之间通信的安全性和数据加密，防止未授权访问和数据篡改。

总结来说，`ETCD_CERT_FILE` 主要用于验证客户端与 `etcd` 服务器之间的通信，而 `ETCD_PEER_CERT_FILE` 用于验证集群内部节点之间的通信。这两种证书反映了 `etcd` 安全架构中的两个不同层面：客户端-服务器模型和集群内部对等节点通信模型。

### 举例

当我们使用 etcdctl 访问 etcd server 的时候，需要配置客户端证书（--cert=  --key=）才能访问。这个证书只有是 ca 证书签发的就行，如果找不到专门给 etcdctl 签发的客户端证书，可以自己签一个，或者直接拿系统现有的证书，都是可以的。

像下列配置那样，证书配成下面这两个个都是可以的

node-k8s-master-01.pem
member-k8s-master-01.pem


```shell
# kube-apiserver 启动配置（启动参数）
kube-apiserver
...
# 这里配置了证书的双向认证
--etcd-cafile=/etc/ssl/etcd/ssl/ca.pem # 用于验证服务端证书的 ca
--etcd-certfile=/etc/ssl/etcd/ssl/node-k8s-master-01.pem # 客户端证书
--etcd-keyfile=/etc/ssl/etcd/ssl/node-k8s-master-01-key.pem 
...

# ETCD 启动配置（环境变量）
# 服务端证书配置
ETCD_TRUSTED_CA_FILE=/etc/ssl/etcd/ssl/ca.pem # 用于验证客户端证书的 ca
ETCD_CERT_FILE=/etc/ssl/etcd/ssl/member-k8s-master-01.pem # 服务端证书
ETCD_KEY_FILE=/etc/ssl/etcd/ssl/member-k8s-master-01-key.pem
ETCD_CLIENT_CERT_AUTH=true

# 内部节点通信间证书配置
ETCD_PEER_TRUSTED_CA_FILE=/etc/ssl/etcd/ssl/ca.pem
ETCD_PEER_CERT_FILE=/etc/ssl/etcd/ssl/member-k8s-master-01.pem
ETCD_PEER_KEY_FILE=/etc/ssl/etcd/ssl/member-k8s-master-01-key.pem
ETCD_PEER_CLIENT_CERT_AUTH=True
```

- 自己签发证书

```shell
cd /root/test
# 创建客户端私钥
openssl genrsa -out client-key.pem 2048
# 创建证书签名请求（CSR）
openssl req -new -key client-key.pem -out client.csr -subj "/CN=etcd-client"
# 使用 CA 签发客户端证书
openssl x509 -req -in client.csr -CA /etc/ssl/etcd/ssl/ca.pem -CAkey /etc/ssl/etcd/ssl/ca-key.pem -CAcreateserial -out client-cert.pem -days 365

# 配置 ETCDCTL 使用刚刚签发的客户端证书
export ETCDCTL_CACERT="/etc/ssl/etcd/ssl/ca.pem"
export ETCDCTL_CERT="/root/test/client-cert.pem"
export ETCDCTL_KEY="/root/test/client-key.pem"
```
