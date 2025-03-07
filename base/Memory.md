# 内存

内存是计算机的重要部件

## 虚拟内存

内存对物理内存进行了抽象

### 栈内存

栈内存是一块区域，用于存储函数的临时信息，例如变量，函数参数等。

**栈内存溢出**

如下代码所示，我们做了一个大数组，一个有 1MB 大小。Linux 系统默认的栈大小是 8MB，因此这个函数最多跑 7 次就会报错。

我们可以通过 Linux 命令 ulimit -s 20480 配置当前用户 Shell 下的栈限制。

所以对于大量的数据，要使用堆内存，也就是：malloc.

```c
#include <stdio.h>
#include <string.h>

// compile: gcc -o stack stack.c

void simulateStackOverflow(int depth) {
    // 分配大数据（1MB）在栈上
    char data[1024 * 1024]; // right way: char *data = (char*)malloc(1024 * 1024);
    // 防止编译器优化掉未使用的变量
    memset(data, 0, sizeof(data)); // right way: free(data);

    printf("Recursion depth: %d\n", depth);
    simulateStackOverflow(depth + 1);
}

int main(void) {
    simulateStackOverflow(1);
    return 0;
}
```
