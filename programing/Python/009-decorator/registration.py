registry = []


def register(func):
    print(f'running register {func}')
    registry.append(func)

    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print(f'registry -> {registry}')
    f1()
    f2()
    f3()


if __name__ == '__main__':
    """
    ========== python3 registration.py 输出结果 ==========
    running register <function f1 at 0x10d12d3a0>
    running register <function f2 at 0x10d12d310>
    running main()
    registry -> [<function f1 at 0x10d12d3a0>, <function f2 at 0x10d12d310>]
    running f1()
    running f2()
    running f3()
    
    ========== 调用模块: import registration 输出结果 ==========
    In [1]: import registration
    running register <function f1 at 0x107393e50>
    running register <function f2 at 0x10808ae50>
    """
    main()
