# 实用指南

## 常见问题解决

<img width="524" alt="image" src="https://github.com/user-attachments/assets/7ce69375-bb6b-4330-aec5-77f7703e3fd9" />

遇到上述报错 `error: You must be logged in to the server (Unauthorized)` ，可以查看下是不是过期了 

```shell
# 查看用户
kubectl config get-contexts
# 验证权限
kubectl auth can-i get pod
# <USER_NAME> 替换为用户名
kubectl config view --raw -o jsonpath='{.users[?(@.name == "<USER_NAME>")].user.client-certificate-data}' | base64 -d | openssl x509 -noout -dates

# 如果输出显示到期了，需要替换下
# notBefore=May 16 03:08:51 2023 GMT
# notAfter=May 15 03:08:51 2024 GMT

# 重新签发证书，csr 证书请求，key 密钥可以继续用以前的
openssl x509 -req -in xxx.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out xxx.crt -days 365


# ====== 重新生成生成 dev.kubeconfig ======
export KUBE_APISERVER="https://192.168.167.xx:6443"

kubectl config set-cluster kubernetes \
--certificate-authority=/etc/kubernetes/pki/ca.crt \
--embed-certs=true \
--server=${KUBE_APISERVER} \
--kubeconfig=dev.kubeconfig
 
# 设置客户端认证参数
kubectl config set-credentials xxx \
--client-certificate=xxx.crt \
--client-key=xxx.key \
--embed-certs=true \
--kubeconfig=dev.kubeconfig
 
# 设置上下文参数
kubectl config set-context kubernetes \
--cluster=kubernetes \
--user=xxx \
--namespace=xxx \
--kubeconfig=dev.kubeconfig
 
# 设置默认上下文
kubectl config use-context kubernetes --kubeconfig=dev.kubeconfig

# 覆盖老 config
cp dev.kubeconfig /home/dev/.kube/config
```
