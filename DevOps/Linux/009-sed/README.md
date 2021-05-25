# sed

sed 运行逻辑：

![](https://pic002.cnblogs.com/images/2011/96760/2011111421151143.png)

## 使用说明

![](https://pic4.zhimg.com/80/v2-31f5d953a3cd62eaf71d317fb58dbed3_1440w.jpg)


## 常见操作

```shell
# =========== test.txt ===========
# hello
# find old enable find
# short inside
# =========== 示例文件 ===========

# 替换第二行的【第一个】(每个/g 只替换第一个)匹配到的 find 为 unstable
sed -i '2s/find/search/' test.txt
# 替换第二行的所有的 find 为 search
sed -i '2s/find/search/g' test.txt
```

## 参考

1. https://zhuanlan.zhihu.com/p/66651350
2. https://www.cnblogs.com/fhefh/archive/2011/11/22/2259097.html
3. https://blog.51cto.com/xficc/1621403
4. https://coolshell.cn/articles/9104.html
