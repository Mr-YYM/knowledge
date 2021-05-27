# ssh

## 常见配置

- 允许某个用户使用密码登录，其他禁止密码登录 `/etc/ssh/ssd_config`

```ini
Match User root
    PasswordAuthentication no
Match User test
    PasswordAuthentication yes
Match all
```
