# 包管理

## 常见操作

- pip 改源

    修改文件 `.pip/pip.conf`

    ```ini
    [global]
    index-url = https://mirrors.aliyun.com/pypi/simple/
    ```

- conda 改源

https://zhuanlan.zhihu.com/p/87123943

    修改文件 `~/.condarc`

    ```yaml
    channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
    ssl_verify: true
    ```
