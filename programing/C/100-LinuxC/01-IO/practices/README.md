# 练习

## readfile_writefile.c

### 题目

当然，我很乐意为你设计一道编程题来帮助你巩固理解：

编写一个 C 语言程序，接受两个命令行参数：源文件的名称和目标文件的名称。你的程序应该打开源文件，读取其内容，然后将这些内容写入到目标文件中。

以下是这个问题的一些详细要求：

- 如果源文件无法打开，你的程序应该打印一个错误消息并返回非零值。
- 如果目标文件已经存在，你的程序应该询问用户是否要覆盖它。如果用户选择不覆盖，那么你的程序应该立即退出。
- 你的程序应该使用适当大小的缓冲区来一次性读取源文件的一部分内容，然后将这些内容写入到目标文件中，直到源文件的所有内容都被复制过去。注意检查 `read` 和 `write` 的返回值，以确保读取和写入操作都成功完成。
- 你的程序在完成文件复制后应该关闭所有打开的文件，并返回 0 表示成功完成。

在完成这个问题后，你将更深入地理解 `open`、`read` 和 `write` 的工作原理，并掌握了如何在实际程序中使用这些系统调用。


### 写题过程中遇到的问题

1. 报错。

- 报错内容

```shell
readfile_writefile.c:14:10: error: array initializer must be an initializer list or string literal
    char write_filename[] = argv[2];
```

- 报错代码

```c
char write_filename[] = argv[2];
```

- 问题分析

在 C 语言中，你不能直接使用这种方式来初始化字符数组。`argv[2]` 是一个字符指针，而不是一个初始化列表或者字符串字面量。

要想把命令行参数（例如 `argv[2]`）的值复制到一个新的字符串（字符数组）中，你需要使用字符串复制函数 `strcpy()`。首先要为新的字符串分配足够的空间（记得包括字符串结尾的 '\0'），然后调用 `strcpy()` 函数进行复制。注意，你需要包含头文件 `<string.h>` 来使用 `strcpy()`。

以下是一个例子：

```c
#include <string.h>

int main(int argc, char *argv[]) {
    char write_filename[256];
    strcpy(write_filename, argv[2]);

    // 其他代码...

    return 0;
}
```

这里我们假设 `write_filename` 的长度不会超过 256 个字符。在实际编程中，你可能需要更好的错误处理和边界检查，以防止数组越界和缓冲区溢出。

另外，如果你只是想把 `argv[2]` 的值作为文件名，你并不需要复制它。你可以直接使用 `argv[2]`，因为 `argv[2]` 已经是一个指向字符串的指针。例如：

```c
int main(int argc, char *argv[]) {
    char *write_filename = argv[2];

    // 其他代码...

    return 0;
}
```

在这个例子中，`write_filename` 是一个指针，它指向 `argv[2]` 所指向的字符串。你可以用 `write_filename` 作为文件名，跟你用 `argv[2]` 作为文件名的效果是一样的。

- 问题解决代码

```c
char *write_filename = argv[2];
```

2. 报错

- 报错内容

```shell
readfile_writefile.c:20:33: error: too many arguments to function call, expected 1, have 2
        perror("open %s error", read_filename);
        ~~~~~~                  ^~~~~~~~~~~~~
/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h:169:7: note: 'perror' declared here
void     perror(const char *) __cold;
         ^
1 error generated.
```

- 报错代码

```c
perror("open %s error", read_filename);
```

- 问题分析

perror 不向 printf 那样可以接受两个以上参数给你做字符串格式化。我们只能另外做一个字符串给他传入。

如果需要创建一个新的字符串，可以使用`sprintf`函数：

- 问题解决代码

```c
if (read_file_fd == -1){
    char error_msg[256];
    sprintf(error_msg, "open %s error", read_filename);
    perror(error_msg);
    return 1; // main 函数返回 程序终止
}
```

3. 报错

- 报错内容

```shell
readfile_writefile.c:50:9: error: use of undeclared identifier 'write_file_fd'
    if (write_file_fd == -1){
        ^
1 error generated.
```

- 问题分析

你遇到的问题可能是由于 `write_file_fd` 变量只在 if 块中被声明和定义，而在 if 块之外是不可见的。在 C 语言中，变量的作用域（即它可以被访问的区域）是由它被声明的位置决定的。如果你在一个块（如 if、for、while 或任何花括号 `{}` 包围的代码块）内部声明一个变量，那么这个变量只在这个块内部可见。

例如，以下代码会导致编译错误：
```c
if (condition) {
    int x = 5;
}
printf("%d\n", x);  // Error: x is not declared in this scope
```
因为 `x` 变量是在 if 块内部声明的，所以它在 if 块之外是不可见的，也就是说，`printf` 语句不能访问 `x`。

如果你想让 `write_file_fd` 在 if 块之外也可见，你应该在 if 块之外声明它：
```c
int write_file_fd;
if (condition) {
    write_file_fd = open(...);
}
// Now you can use write_file_fd here
```
在这个例子中，`write_file_fd` 是在 if 块之外声明的，所以它在 if 块之外也是可见的。

请注意，这是一个通用的编程概念，适用于所有的 C-like 语言，包括 C++、Java、C# 等。


### 完成后批改

你的代码看起来已经很完善了，而且涵盖了所有的要求！但我发现了一个小错误：

在你的代码的最后部分，你两次关闭了 `write_file_fd`，而没有关闭 `read_file_fd`。这可能是一个笔误。你应该同时关闭 `read_file_fd` 和 `write_file_fd`。

另外，我发现在你的 while 循环中，你在读取文件内容之前就已经初始化了 `bytesRead`，但它并没有被赋予一个明确的初始值，这可能导致读取操作在首次进入循环时不会被执行。为了解决这个问题，你可以先执行一次读取操作，然后再进入循环，如下所示：

```c
ssize_t bytesRead = read(read_file_fd, readfile_buffer, BUFFER_SIZE);
while (bytesRead > 0){
    // 写入操作
    ssize_t bytesWritten = write(write_file_fd, readfile_buffer, bytesRead);
    if (bytesWritten != bytesRead) {
        // 错误处理
        perror("write file error");
        return 1;
    }
    bytesRead = read(read_file_fd, readfile_buffer, BUFFER_SIZE);
}
```
或者你也可以使用 do...while 循环，这样可以保证至少执行一次读取操作，然后再检查条件。

```c
ssize_t bytesRead;
do {
    bytesRead = read(read_file_fd, readfile_buffer, BUFFER_SIZE);
    // 检查是否读取到文件结束或者出错
    if (bytesRead == -1) {
        perror("read file error");
        return 1;
    }
    // 写入操作
    ssize_t bytesWritten = write(write_file_fd, readfile_buffer, bytesRead);
    if (bytesWritten != bytesRead) {
        // 错误处理
        perror("write file error");
        return 1;
    }
} while (bytesRead > 0);
```

总的来说，你的代码已经非常好了，只需要修复上述的一些小问题即可。再次祝贺你完成这个练习！
