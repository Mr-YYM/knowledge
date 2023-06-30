# TIPS

## About _t

在 C 语言中，类型名通常以 `_t` 结尾，这是一种命名约定，用来表示这是一个类型定义（type definition）。所以在 `ssize_t` 这个类型名中，`t` 就是表示“type”的意思。

这个命名约定来源于 POSIX 标准，这个标准定义了许多 Unix 和类 Unix 系统的接口。在 POSIX 中，所有的类型定义都以 `_t` 结尾，以区别于其他的标识符。这个命名约定后来被广泛接受，成为了 C 语言中的一种普遍实践。

所以，在 `ssize_t` 中的 `t`，就是表示这是一个类型定义的意思。`ssize_t` 是一个表示有符号大小的类型定义，在许多系统中，它通常被定义为 `long` 或 `int` 的别名。

在 C 语言及其库中，存在许多类似的类型定义，它们都是以 `_t` 结尾的。以下列举一些常见的例子：

1. **size_t**：这是一个无符号整数类型，用于表示大小，例如数组的长度或者 `malloc` 函数的参数。

2. **ptrdiff_t**：这是一个有符号整数类型，用于表示两个指针之间的差值。

3. **int8_t, int16_t, int32_t, int64_t**：这些是固定宽度的有符号整数类型，分别表示 8 位、16 位、32 位和 64 位的整数。

4. **uint8_t, uint16_t, uint32_t, uint64_t**：这些是固定宽度的无符号整数类型，分别表示 8 位、16 位、32 位和 64 位的整数。

5. **intptr_t, uintptr_t**：这些类型足够大，可以存储任何指针的值。`intptr_t` 是有符号的，`uintptr_t` 是无符号的。

这些类型定义都在标准库的头文件中定义，例如 `<stddef.h>`、`<stdint.h>` 和 `<sys/types.h>` 等。这些类型的具体定义可能会因为系统和编译器的不同而有所差异，但是他们的基本含义和用途是相同的。

## 指针与变量

变量和指针是 C 语言中两种基本的数据类型，它们在用途和工作方式上有一些关键的区别。

1. **变量**：变量在 C 语言中是一个存储值的位置。每个变量都有一个类型（例如 `int`，`float`，`char` 等），这个类型决定了变量可以存储什么样的值，以及变量占用的内存空间大小。你可以对变量进行赋值操作，并且可以通过变量名来获取和修改它的值。

```c
int var = 10; // 声明一个 int 类型的变量 var， 并赋值为 10
```

2. **指针**：指针是一个特殊类型的变量，它存储的是内存地址，而不是一个普通的值。这个内存地址指向内存中的一个位置，这个位置上存储的是指针所指向的值。指针的类型（例如 `int*`，`float*`，`char*` 等）决定了它可以指向什么样的值。

```c
int var = 10;   // 声明一个 int 类型的变量 var
int *ptr = &var; // 声明一个 int 类型的指针 ptr， 并让它指向 var 的地址
```

指针可以被用来实现多种高级的编程技术，例如动态内存分配，函数指针，和数据结构（例如链表和树）等。然而，指针也需要谨慎使用，因为错误的使用指针可能会导致一些复杂的问题，例如空指针解引用和内存泄漏等。

## 接收命令行参数

在C语言中，程序可以通过主函数的参数接收命令行参数。主函数有两个参数，通常命名为 `argc` 和 `argv`。`argc` 是命令行参数的数量，`argv` 是一个包含所有命令行参数的字符串数组。

以下是一个例子，这个程序会打印出它接收到的所有命令行参数：

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    for(int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
```

假设这个程序的名字是 `prog`，你在命令行中运行它，如下：

```shell
./prog arg1 arg2
```

程序将会输出：

```
argv[0] = ./prog
argv[1] = arg1
argv[2] = arg2
```

你会发现 `argv[0]` 通常是程序的名字，后面的 `argv[1]`、`argv[2]` 等等，就是命令行中给出的参数。`argc` 则是命令行参数的数量，包括程序名。

在这个例子中，如果你只想接收两个参数，你可以添加一些错误检查的代码，如下：

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc != 3) {
        printf("Usage: %s arg1 arg2\n", argv[0]);
        return 1;
    }

    printf("arg1 = %s, arg2 = %s\n", argv[1], argv[2]);
    return 0;
}
```

这个程序在 `argc` 不等于 3 时，即没有收到两个参数时，会打印出一个错误信息并退出。否则，它将打印出接收到的两个参数。