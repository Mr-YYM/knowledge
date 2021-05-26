# 装饰器

```python
def foo():
    def wrap(*args, **kwargs):
        """
        装饰器内部函数
        """
        pass
    return wrap
```

通常，装饰器内部会定义一个内部函数，要了解内部函数，需要首先了解「变量作用域」与「闭包」的概念

## 变量作用域

- sample

    ```python
    b = 6
    def foo(a):
        print(a)
        print(b)  # 报错在这里: UnboundLocalError: local variable 'b' referenced before assignment
        b = 9  # 不加这一句是不会报错的，但是加了就会报错
    
    foo(0)
    ```

## 闭包


## 参考

1. 《流畅的Python》
