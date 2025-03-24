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
```
