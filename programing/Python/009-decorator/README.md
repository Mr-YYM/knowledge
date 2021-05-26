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

    为什么会报错，因为 Python 默认会把在函数内定义的变量当作「局部变量」，因此，当 `print(b)` 下面出现了 `b = 9`，Python 编译器就会把 b 当作函数 f3 的一个局部变量处理， `print(b)` 的 b 在之前没有声明（assignment）任何值，所有就报错了。解决办法就是在函数最前面加一句 `global b`

## 闭包


## 参考

1. 《流畅的Python》
